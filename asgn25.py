#Q1. Write a python script to create a Profile class with 3 attributes (name, email, age).
#Ans:-
class Profile:
    def __init__(self,name,email,age):
        self.name=name
        self.email=email
        self.age=age
    def showProfile(self):
        print(self.name,self.email,self.name,sep="   ")

#Q2. Write a python script to update the above Profile class with encapsulation.
#Ans:-
class Profile1(Profile):  #by default init function of parent will run b'coz child class has no init function
    def updateProfile(self):
        self.name=input("Enter your name:-")
        self.email=input("Enter your email:-")
        self.age=int(input("Enter your age:-"))


#Q3. Write a python script to update 2nd Question, change email and age to __email and __age.
#ans:-
class Profile2(Profile1):
    def __init__(self,name,email,age):
        self.name=name
        self.__email=email  #can't be access from outside
        self.__age=age  #can't be access directly from outside the profile class
    def showProfile(self): #this function will inherit from Profile class but there will be no attribute like email and age. Here __email and __age is an attribute
        print(self.name,self.__email,self.__age,sep="   ")
p1=Profile2("Ritesh","ritesh@2002gmail.com",20)
p1.showProfile()


#Q4. Write a python script to update 2nd Question, add a class variable (platform) and create a classmethod to access it.
#Ans:-
class Profile4(Profile2):
    platform="xyz Company"
    def updateProfile(self):
        self.name=input("Enter your name:-")
        self.email=input("Enter your email:-")
        self.age=int(input("Enter your age:-"))

    @classmethod
    def get_platform(cls):
        return cls.platform

# u4 = Profile4("Brijesh","brijesh@gmail.com",20)
# u4.get_platform()
print(Profile4.get_platform())


#Q5. Write a python script to create a Calculator class with 2 methods for adding and subtracting 2 values.
#Ans:-
class Calculator:
    def __add__(self,n1,n2):  #or we can use add function  #Here,We are not using  'self and other' as an argument b'coz for that we have to create a variable inside an object so that this self+other operation will perform
        return n1+n2  #as i'm assuming that both self and other are of int type data

    def __sub__(self, n1,n2):
        return n1-n2


#Q6. Write a python script to create a Calculator 2.0 class with 2 methods for multiplication and division of 2 values and inherit it from the Calculator class.
#Ans:-
class  Calculator2(Calculator):   #Calculator_2.0_:  --> We can't use . point here
    def __mul__(self,n1,n2):
        return n1*n2
    def __floordiv__(self, n1, n2):
        return n1//n2
    # def __divmod__(self, other):  #==> Why this function is used ? this function is for which operator ?
    #     return self/other
    def __truediv__(self, n1,n2):
        return n1/n2


#Q7. Write a python script to create a Phone class with 2 methods to print the features (calling and sms).
#Ans:-
class Phone:
    def call(self):
        print("Calling...")
    def message(self):
        print("Message...")


#Q8. Write a python script to create a SmartPhone class by inheriting Calculator 2.0 and Phone Class.
#Ans:-
class SmartPhone(Calculator2,Phone): #Acc. to me, it cn't be inherit b'coz Smartphone has a calulator NOT Smartphone is a calculator.
    def smart(self):
        print("This SmartPhone has a smart Features")
sp1=SmartPhone()
sp1.call()
sp1.smart()
print(sp1.__add__(5,8))


#Q9. Write a python script to create an application like Truecaller where names and numbers are stored.
# Truecaller class will have 2 methods (1st to fetch the name of a number and 2nd to add a new entry).
#Ans:-
class Truecaller:
    def __init__(self):
        self.dict1 = {} #or dict1=dict()
    def add(self,name,number):
        self.dict1[number]=name  #Don't do this --> dict1[name]=number B'coz in dict key should be unique and if name is key then it will not be an unique. As we know that Number is always an unique.
    def fetchName(self,Number):
        return self.dict1[Number]


#Q10. Write a python script to add the new method in SmartPhone class which accepts Truecaller object as a parameter and call the fetch method of Truecaller.
#Ans:-
class SmartPhone1(Calculator2,Phone):  #same code as in SmartPhone Class
    def smart(self):
         print("This SmartPhone has a smart Features")
    def FetchName(self,object,Number):
        return object.fetchName(Number)
sp12=SmartPhone1()
t1=Truecaller()
t1.add("Mahesh",351654)
t1.add("Ramesh",351655)
print(sp12.FetchName(t1,351654))

























