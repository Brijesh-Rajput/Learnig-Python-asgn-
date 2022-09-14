#Q8. interseting question on sorting on some base value

# Q1. Write a python program to create a user class with 3 properties : name, age, email.
# Ans:-
class user1:
    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email

    def showData(self):
        print("Name :- {}  Age :- {}   Email:- {} ".format(self.name, self.age, self.email))


user = user1("Gulshan", 22, "gulshan@gmail.com")
user.showData()
print()


# Q2. Write a python program to create a user class with a method to greet the user.
# Ans:-
class user2:
    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email

    def showData(self):
        print("Name :- {}  Age :- {}   Email:- {} ".format(self.name, self.age, self.email))

    def greet(self):
        print("Good Morning")


user = user2("Mahesh", 21, "Mahesh@gmail.com")
user.greet()
print()


# Q3. Write a python program to create 2 objects of the user class and assign different values.
# Ans:-
class user3:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def showData(self):
        print("Name :- {}  Age :- {} ".format(self.name, self.age))


userA = user3("Mahesh", 21)
userB =user3("Ramesh",19)
userA.showData()
userB.showData()
print()


#Q4. Write a python program to init default values for user object using __init__ method.
#Ans:-
class user4:
    def __init__(self):
        self.name="Unknown"
        self.age=18
        self._gender="Male"
        self.__goal="xyz"  #by this way we can hide the instance variable of a class
    def __set_goal(self):
        self.__goal="abc"
u1=user4()
print("Default Name:-",u1.name," And Default Age:-",u1.age)
# print(u1.__goal)  --> Error:- it can't be access
# u1.__set_goal() # --> Error :- can't be access by an object
# print(user4.__set_goal(u1))  --> can't be access
#NOTE:- __(double underscore) behave as a private member
print(u1._gender) #it is accessble but use for telling that don't use this outside the class directly.treat this like a private member.Those attribute is started with _(single underscore)
print()


#Q5. Write a python program to delete the age property of the user.
#Ans:-
class user5:
    def __init__(self,name,age):
        self.name=name
        self.age=age
u2=user5("Brijesh",21)
print("Before Deletion of age property :- Name=",u2.name," Age=",u2.age)
del u2.age
# print("After Deletion of age property of user:- Name=",u2.name,"Age=",u2.age) # Error:- NameError: name 'age' is not defined
print()


#Q6. Write a python program to create 3 user objects and find the youngest of all.
#Ans:-
class user6:
    def __init__(self,name,age):
        self.name=name
        self.age=age
u1,u2,u3=user6("abc",20),user6("pqr",19),user6("abc",22)
print("user name=",(u1.name if u1.age>u3.age else u3.name) if u1.age>u2.age else (u2.name if u2.age>u3.age else u3.name)," Whose age is greater than among all three user")
print()


#Q7. Write a python program to create a Laptop class with 4 attributes (brand, ram, cpu, hdd) and 2 methods (showConfig() to print the values, __init__() to initialize the values).
#Ans:-
class Laptop:
    def __init__(self,brand,ram,cpu,hdd):
        self.brand=brand
        self.ram=ram
        self.cpu=cpu
        self.hdd=hdd
    def showConfig(self):
        print("Brand={}  ram={}  cpu={}  hdd={}".format(self.brand,self.ram,self.cpu,self.hdd))
l1=Laptop("Dell","4gb","i3","SSD")
l1.showConfig()
print()


#Q8.  WRT 7th Question, create 3 Laptop objects and add them to the list in the sorted order based on the ram size.
#Ans:-
class Laptop:
    def __init__(self,brand,ram,cpu,hdd):
        self.brand=brand
        self.ram=ram
        self.cpu=cpu
        self.hdd=hdd
    def showConfig(self):
        print("Brand={}  ram={}  cpu={}  hdd={}".format(self.brand,self.ram,self.cpu,self.hdd))
l1=Laptop("Dell",4,"i3","SSD")
l2=Laptop("HP",8,"i5","HDD")
l3=Laptop("Lenovo",16,"i9","HDD")
laptopList=[l3,l2,l1]
length=len(laptopList)
#Bubblesort is used
for round in range(0,length-1):
    for i in range(0,length-1):
        j=i+1
        if laptopList[i].ram>laptopList[j].ram:
            laptopList[i],laptopList[j]=laptopList[j],laptopList[i]
for e in laptopList:
    e.showConfig()
print()
# # sorted_list=[] #or sorted_list=list()
# # for e in laptopList:
# d1={e.ram:e for e in laptopList}
# sorted(d1)


#Q9. Write a python program to create a School class and 3 instance variables and 1 class variable.
#Ans:-
class School:
    schoolName="NHS"
    def __init__(self):
        self.Totalteachers=30
        self.TotalStudents=1000
        self.schoolDays=("Monday","Tuesday","Wednesday","Thrusday","Friday")


#Q10. Define a class Employee with instance object variables empid, name, salary. Write __init__() method in the class to initialize instance object variables.
# Also define instance methods to input fields and display field value
#Ans:-
class Employee:
    def __init__(self,empid,name,salary):
        self.name=name
        self.empid=empid
        self.salary=salary
    """
    def set_employee(self,empid,name,salary): #What is the benefit of making this ? if we can call again init method with the existing object of that same class.
        self.name = name
        self.empid = empid
        self.salary = salary
    """
    def setEmployee(self):
        self.name=input("Enter a Name : ")
        self.empid=int(input("Enter your Employee id :- "))
        self.salary=float(input("Enter your salary :- "))
    def display(self):
        print("Name:-{}  Empid:-{}  Salary:-{}".format(self.name,self.empid,self.salary))
e1=Employee(12302,"Ramu",56982.213)
e1.display()
e1.setEmployee()
e1.display()
print()


























