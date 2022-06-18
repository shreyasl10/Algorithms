import pandas as pd


def Absent():
    df2F = pd.read_excel(r'/home/shreyas/Downloads/fullAtt.xlsx',
                         sheet_name="2-9-2020 FN")
    df2A = pd.read_excel(r'/home/shreyas/Downloads/fullAtt.xlsx',
                         sheet_name="2-9-2020 AN")
    df3F = pd.read_excel(r'/home/shreyas/Downloads/fullAtt.xlsx',
                         sheet_name="3-9-2020 FN")
    df3A = pd.read_excel(r'/home/shreyas/Downloads/fullAtt.xlsx',
                         sheet_name="3-9-2020 AN")
    df4F = pd.read_excel(r'/home/shreyas/Downloads/fullAtt.xlsx',
                         sheet_name="4-9-2020 FN")
    df4A = pd.read_excel(r'/home/shreyas/Downloads/fullAtt.xlsx',
                         sheet_name="4-9-2020 AN")
    df5F = pd.read_excel(r'/home/shreyas/Downloads/fullAtt.xlsx',
                         sheet_name="05-09-2020 FN")
    df5A = pd.read_excel(r'/home/shreyas/Downloads/fullAtt.xlsx',
                         sheet_name="05-09-2020 AN")
    df7F = pd.read_excel(r'/home/shreyas/Downloads/fullAtt.xlsx',
                         sheet_name="7-9-2020 FN")
    df7A = pd.read_excel(r'/home/shreyas/Downloads/fullAtt.xlsx',
                         sheet_name="7-9-2020 AN")
    df8F = pd.read_excel(r'/home/shreyas/Downloads/fullAtt.xlsx',
                         sheet_name="8-9-2020 FN")
    df8A = pd.read_excel(r'/home/shreyas/Downloads/fullAtt.xlsx',
                         sheet_name="8-9-2020 AN")
    df9F = pd.read_excel(r'/home/shreyas/Downloads/fullAtt.xlsx',
                         sheet_name="9-9-2020 FN")
    df9A = pd.read_excel(r'/home/shreyas/Downloads/fullAtt.xlsx',
                         sheet_name="9-9-2020 AN")
    df1 = pd.read_excel(
        r'/home/shreyas/Downloads/ccc1.xlsx')
    presentF2 = df2F['Roll No'].tolist()
    presentA2 = df2A['Roll No'].tolist()
    presentF3 = df3F['Roll No'].tolist()
    presentA3 = df3A['Roll No'].tolist()
    presentF4 = df4F['Roll No'].tolist()
    presentA4 = df4A['Roll No'].tolist()
    presentF5 = df5F['Roll No'].tolist()
    presentA5 = df5A['Roll No'].tolist()
    presentF7 = df7F['Roll No'].tolist()
    presentA7 = df7A['Roll No'].tolist()
    presentF8 = df8F['Roll No'].tolist()
    presentA8 = df8A['Roll No'].tolist()
    presentF9 = df9F['Roll No'].tolist()
    presentA9 = df9A['Roll No'].tolist()
    students = df1['Registration Number'].tolist()
    print("Absent for both sessions of 02-Sept")
    for i in students:
        if i not in presentF2 and i not in presentA2:
            print(i)
    print("Forenoon absentees of 02-Sept")
    for i in students:
        if i not in presentF2:
            print(i)
    print("Afternoon absentees of 02-Sept")
    for i in students:
        if i not in presentA2:
            print(i)
    print("Absent for both sessions of 03-Sept")
    for i in students:
        if i not in presentF3 and i not in presentA3:
            print(i)
    print("Forenoon absentees of 03-Sept")
    for i in students:
        if i not in presentF3:
            print(i)
    print("Afternoon absentees of 03-Sept")
    for i in students:
        if i not in presentA3:
            print(i)
    print("Absent for both sessions of 04-Sept")
    for i in students:
        if i not in presentF4 and i not in presentA4:
            print(i)
    print("Forenoon absentees of 04-Sept")
    for i in students:
        if i not in presentF4:
            print(i)
    print("Afternoon absentees of 04-Sept")
    for i in students:
        if i not in presentA4:
            print(i)
    print("Absent for both sessions of 05-Sept")
    for i in students:
        if i not in presentF5 and i not in presentA5:
            print(i)
    print("Forenoon absentees of 05-Sept")
    for i in students:
        if i not in presentF5:
            print(i)
    print("Afternoon absentees of 05-Sept")
    for i in students:
        if i not in presentA5:
            print(i)
    print("Absent for both sessions of 07-Sept")
    for i in students:
        if i not in presentF7 and i not in presentA7:
            print(i)
    print("Forenoon absentees of 07-Sept")
    for i in students:
        if i not in presentF7:
            print(i)
    print("Afternoon absentees of 07-Sept")
    for i in students:
        if i not in presentA7:
            print(i)
    print("Absent for both sessions of 08-Sept")
    for i in students:
        if i not in presentF8 and i not in presentA8:
            print(i)
    print("Forenoon absentees of 08-Sept")
    for i in students:
        if i not in presentF8:
            print(i)
    print("Afternoon absentees of 08-Sept")
    for i in students:
        if i not in presentA8:
            print(i)
    print("Absent for both sessions of 09-Sept")
    for i in students:
        if i not in presentF9 and i not in presentA9:
            print(i)
    print("Forenoon absentees of 09-Sept")
    for i in students:
        if i not in presentF9:
            print(i)
    print("Afternoon absentees of 09-Sept")
    for i in students:
        if i not in presentA9:
            print(i)


Absent()
