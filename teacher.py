import pandas as pd
import utils.cols as COLNAME


with open("lists/teachers.txt") as file:
    teachers = file.read().strip().split("\n")


with open("lists/timeslots.txt") as file:
    timeslots = file.read().strip().split("\n")


data_all = {
    "BF": [],
    "CC": [],
    "CJ": [],
    "CL": [],
    "DK": [],
    "GP": [],
    "IQ": [],
    "JT": [],
    "MO": [],
    "MY": [],
    "RT": [],
    "SH": [],
    "SK": [],
    "SY": [],
    "VC": [],
    "JL": [],
    "XX": [],
    "YY": [],
    "KL": [],
}


for timeslot in timeslots:
    sheet = pd.read_excel(f"finalisedInputs/{timeslot}.xlsx", index_col=0)

    for t in teachers:
        for index, row in sheet.iterrows():
            NAME = row[COLNAME.NAME]
            CLASS = row[COLNAME.CLASS]
            GENDER = row[COLNAME.GENDER_F]
            MODULE = row[COLNAME.MODULE]
            VENUE = row[COLNAME.VENUE]
            TEACHER = row[COLNAME.TEACHER]
            SLOT = timeslot

            try:
                TEACHER_I = row[COLNAME.TEACHER_I]
            except:
                TEACHER_I = row[COLNAME.TEACHER_I.upper()]

            if t == TEACHER_I:
                data = data_all[t]
                data.append([NAME, CLASS, GENDER, MODULE, VENUE, TEACHER, SLOT])
                data_all[t] = data


for initial in data_all:
    df = pd.DataFrame(
        data_all[initial],
        columns=[
            "Name",
            "Class",
            "Gender",
            "Allocated Module",
            "Venue",
            "Teacher",
            "Slot"
        ],
    )

    df.to_excel(f"finalisedTeacherOutputs/{initial}.xlsx")

    print(f"The sheet for {initial} has been successfully generated!")
