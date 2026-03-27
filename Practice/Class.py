


#OOP


class Student:
    Name = "Daniel"
    Age = 18
    Gender = "Male"
    RollNo = 101
    Stream = "Electrical"

    def study(self):
        print(f"{self.Name} is studying")    

    def getAttendencePercentage(self, days):
        totalDay = 30
        attendencePercentage = (days/totalDay)*100
        print(f"{self.Name} has attendence percentage of {attendencePercentage}%")


# public void Study()
# {
#     console.WriteLine("Student is studying");
# }

student1 = Student()
student1.Name = "John"
student1.study()
student1.getAttendencePercentage(25)


