import pandas as pd
import utils.cols as COLNAME


with open("lists/classes.txt") as file:
    classes = file.read().strip().split("\n")


with open("lists/timeslots.txt") as file:
    timeslots = file.read().strip().split("\n")


for timeslot in timeslots:
    sheet = pd.read_excel(f"finalisedInputs/{timeslot}.xlsx", index_col=0)

    for c in classes:
        data = []  # array of [name, class, gender, allocated module, venue, remarks]

        for index, row in sheet.iterrows():
            NAME = row[COLNAME.NAME]
            CLASS = row[COLNAME.CLASS]
            GENDER = row[COLNAME.GENDER_F]
            MODULE = row[COLNAME.MODULE]
            VENUE = row[COLNAME.VENUE]
            TEACHER = row[COLNAME.TEACHER]

            if c == CLASS:
                data.append([NAME, CLASS, GENDER, MODULE, VENUE, TEACHER])

        if data:
            df = pd.DataFrame(
                data,
                columns=[
                    "Name",
                    "Class",
                    "Gender",
                    "Allocated Module",
                    "Venue",
                    "Teacher",
                ],
            )

            df.to_excel(f"finalisedClassOutputs/{c}.xlsx")

            print(f"The sheet for {c} has been successfully generated!")
