class person:
    def __init__(self,name,last_name):
        self.name=name
        self.last_name=last_name



class student(person):
    def __init__(self,name,last_name,year):
        super().__init__(name,last_name)
        self.thiseyear=year

    def welcome(self):
        print(f"welcome to the school in year {self.name} {self.last_name}{self.thiseyear}")

x=student("deep", "PADWALE" ,2024)
x.welcome()

#  Scenario: A School Management System
# You're building a system for a school. You need to represent different types of people: Teachers, Students, and Administrators. All of them share some common information, like name, age, and email.

# But they also have role-specific attributes:


class person:
    def __init__(self, name,age,email,):
        self.name=name
        self.age=age
        self.email=email


class student(person):
    def __init__(self,name,age,email,grade,rollno):
        super().__init__(name,age,email)
        self.grade=grade
        self.rollno=rollno

    def student_info(self):
        print(f"welcome to the student section  The name of the student is:{self.name} and age is:{self.age}== {self.grade} ")    

class  teacher(person):
    def __init__(self, name,age,email,subject,employee_id ) :
        super().__init__(name,age,email)
        self.subject=subject
        self.employee=employee_id

    def teacher_info(self):
        print(f"welcome to our school find techer roll : {self.name} {self.age} {self.email} {self.subject} {self.employee}")

s1= student("Deep",24,"deeppadwale@gemail.com","A",12)
s1.student_info()

t1=teacher("xyx",45,"xyz@gmail.com","Maths",1001)
t1.teacher_info()