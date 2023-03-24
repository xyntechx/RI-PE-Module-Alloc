import pandas as pd
import sys
import re

import utils.cols as COLNAME
from utils.rank import index_to_rank
from utils.sports import raw_to_key


arg = sys.argv[1]  # cmd line arg to select timeslot

match arg:
    case "mon0825":
        from utils.reqs import mon0825 as REQS
    case "mon0920":
        from utils.reqs import mon0920 as REQS
    case "mon1015":
        from utils.reqs import mon1015 as REQS
    case "tues0825":
        from utils.reqs import tues0825 as REQS
    case "tues0920":
        from utils.reqs import tues0920 as REQS
    case "tues1015":
        from utils.reqs import tues1015 as REQS
    case "thurs0825":
        from utils.reqs import thurs0825 as REQS
    case "thurs0920":
        from utils.reqs import thurs0920 as REQS
    case "fri0825":
        from utils.reqs import fri0825 as REQS
    case "fri0920":
        from utils.reqs import fri0920 as REQS
    case "fri1015":
        from utils.reqs import fri1015 as REQS
    case _:
        sys.exit("Invalid argument")


sheet = pd.read_excel(f"inputs/{arg}.xlsx", index_col=0)

allocated_names = []  # students already assigned a sport

data = []  # array of [name, class, gender, allocated module, venue, remarks]


for choice_rank in range(1, 8):
    # shuffle the input sheet to randomise the student order
    sheet = sheet.sample(frac=1).reset_index(drop=True)

    # columns of the selected timeslot and choice rank (e.g. Mon 0825 1st)
    CHOICE_COLS = [
        col
        for col in sheet
        if " ".join(re.split("(\d+)", arg)).upper() in col
        and index_to_rank(choice_rank) in col
    ]

    # columns containing the student's 1st, 2nd, ... choices
    RELEVANT_COLS = []

    for index, row in sheet.iterrows():
        NAME = row[COLNAME.NAME]
        CLASS = row[COLNAME.CLASS]
        GENDER = row[COLNAME.GENDER]

        try:
            REMARKS = str(row[COLNAME.REMARKS_1]) + "\n" + str(row[COLNAME.REMARKS_2])
        except:
            REMARKS = str(row[COLNAME.REMARKS_2])

        for choice_col in CHOICE_COLS:
            RAW_CHOICE = (
                row[choice_col] if type(row[choice_col]) == str else ""  # NaN -> ""
            )

            if RAW_CHOICE:
                q_index = choice_col.split()[0]  # question number (e.g. Q10)
                RELEVANT_COLS = [col for col in sheet if q_index == col.split()[0]]
                break

        if RAW_CHOICE:
            CHOICE = raw_to_key(RAW_CHOICE, GENDER)

            if (NAME not in allocated_names) and (REQS[CHOICE][0] > 0):
                REQS[CHOICE] = [
                    REQS[CHOICE][0] - 1,  # -1 for available spaces for the sport
                    REQS[CHOICE][1],
                    REQS[CHOICE][2],
                ]

                VENUE = REQS[CHOICE][1]
                TEACHER = REQS[CHOICE][2]

                allocated_names.append(NAME)

                STUDENT_CHOICES = []
                STUDENT_CHOICES = [row[col] for col in RELEVANT_COLS]

                data.append(
                    [
                        NAME,
                        CLASS,
                        GENDER,
                        RAW_CHOICE,
                        VENUE,
                        TEACHER,
                        *STUDENT_CHOICES,
                        REMARKS,
                    ]
                )


df = pd.DataFrame(
    data,
    columns=[
        "Name",
        "Class",
        "Gender",
        "Allocated Module",
        "Venue",
        "Teacher",
        *REQS["CHOICE_COUNT"],
        "Remarks",
    ],
)

df.to_excel(f"outputs/{arg}.xlsx")


print(f"Allocations for {arg} have been successfully generated!")
