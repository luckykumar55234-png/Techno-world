import uuid
import json

class Students:

    def __init__(self):
        pass

    def StudentsReg(self):

        self.Studentsdata = {}

        self.Studentsdata["id"] = str(uuid.uuid4())[:8]
        self.Studentsdata["name"] = input("Enter your name:")
        self.Studentsdata["age"] = input("Enter your age:")
        self.Studentsdata["class"] = input("Enter your class:")
        self.Studentsdata["Email"] = input("Enter your Email:")

        with open("student.json","w") as file:
            json.dump(self.Studentsdata,file,indent=4)

            print("Student data saved successfully")

    def showdata(self):

                print(json.dumps(self.Studentsdata,indent=4))

class Studentsv2(Students):

    def search(self):
        print("*"*20)
        print("SEARCH METHOD")
        print("*"*20)

s1 = Studentsv2()

s1.StudentsReg()
s1.showdata()
s1.search()



                

        

    

        




     

        



