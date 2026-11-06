
def student_result():
    students = []

    n = int(input("Enter number of students: "))

    for i in range(n):
        print("\nStudent", i + 1)

        name = input("Enter student name: ")
        hindi = int(input("Enter Hindi marks: "))
        english = int(input("Enter English marks: "))
        maths = int(input("Enter Maths marks: "))

        total = hindi + english + maths
        percentage = total / 3

        if hindi >= 33 and english >= 33 and maths >= 33:
            result = "Pass"
        else:
            result = "Fail"

        student = {
            "name": name,
            "hindi": hindi,
            "english": english,
            "maths": maths,
            "total": total,
            "percentage": percentage,
            "result": result
        }

        students.append(student)

    print("\nSTUDENT RESULT")

    for s in students:
        print("\nName:", s["name"])
        print("Hindi:", s["hindi"])
        print("English:", s["english"])
        print("Maths:", s["maths"])
        print("Total:", s["total"])
        print("Percentage:", round(s["percentage"], 2))
        print("Result:", s["result"])

    topper = students[0]

    for s in students:
        if s["total"] > topper["total"]:
            topper = s

    print("\nCLASS TOPPER")
    print("Name:", topper["name"])
    print("Total Marks:", topper["total"])
    print("Percentage:", round(topper["percentage"], 2))


student_result()



    

    

        




