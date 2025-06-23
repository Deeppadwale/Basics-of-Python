# crete a class and print in simple format
class personalDetails():
    name='Deep'
    last='padwale'
    age=21
    college='DR. dy patil talsande'

my_details=personalDetails()
print(my_details.name)
print(my_details.last)
print(my_details.age)
print(my_details.college)


# create a class and print it in using of methods

class schoolDetail:
    s_name="Ajay "
    S_age=23
    S_last_name="patil"

    def pritn_detail(self):
        print(self.s_name)
        print(self.S_age)
        print(self.S_last_name)

        
xaa=schoolDetail()
xaa.pritn_detail()


# use the fuction methodes 

class person:
    def __init__(self,Name,age,salary):
        self.name=Name
        self.age=age 
        self.salary=salary

p1=person('Deep',24,100000)
print(p1.name)
print(p1.age)
print(p1.salary)



class newperson:
    def __init__(self,id,name,age):
        self.id=id
        self.name=name
        self.age=age

    def __str__(self):
        return f'ID:{self.id}  Nmae is :{self.name}  Age is {self.age}]'
    
p2=newperson(41,'ajay',25)
print(p2)


