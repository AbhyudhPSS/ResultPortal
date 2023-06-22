class Student:
    def GetStudentInfo(self):
        self.__rollno = int(input("Enter Admission Number:"))
        if self.__rollno == 1403:
            self.__name = "Abhyudh"
            self.__class = 7
            self.__physics = 90
            self.__chemistry = 95
            self.__maths = 100
        elif self.__rollno == 4494:
            self.__name = "Arav"
            self.__class = 7
            self.__physics = 12
            self.__chemistry = 32
            self.__maths = 14
        else:
            print("Not a valid admission number")
    def printResult(self):
        totalresult = ((int)( (self.__physics+self.__chemistry+self.__maths)/300*100))
        print(" ",self.__class,"   ",self.__rollno," ",self.__name," ",totalresult,"%")
        print("Physics:",self.__physics)
        print("Chemistry:",self.__chemistry)
        print("Maths:",self.__maths)
        if totalresult >= 35:
            print("Result: Pass and promoted to class 8")
            print("Congratulations!",self.__name)
        else:
            print("Result: Fail")
            print("Better Luck Next Time",self.__name)
       

StudentArray = []
while(True):
    student = Student()
    student.GetStudentInfo()
    StudentArray.append(student)
    ch = input("Add More yes/no?")
    if(ch=='no'):break

print("Result : ")
print("Class  RollNo.  Name   Percentage")
for student in StudentArray:
    student.printResult()
