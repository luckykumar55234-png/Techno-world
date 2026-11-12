class Father:
    def show1(self):
        print("Father")

class Mother:
    def show2(self):
        print("Mother")

class son(Father,Mother):
    pass

s1 = son()
s1.show1()
s1.show2()
    


    