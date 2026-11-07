def Student_markas():

    hindi = int(input("enter a hindi markas:"))
    mathe = int(input("enter a mathe makas:"))
    english = int(input("enter a english markas:"))

    total = hindi + mathe + english

    percentage = (total/300)*100

    print("Total Markas:",total)
    print("Percentage:",percentage)

Student_markas()


