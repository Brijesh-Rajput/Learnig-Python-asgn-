#Question based on Match Case (Like Switch Case in C++)
#Q6 doesn't solve by me --> i don't know how to do that with match case. condition:- user can enter any no. of space anywhere(at starting of string or ending of string or between also)

#Q1. Write a python script to display the number of days in a given month number.
#Ans:-
match int(input("Enter a month number : ")): #can we write here expression ?Ans=>We can write here  #can we write expression at same place in c/c++ ?  ===> Compare this
    case 1: #we can't write here an expression. It should be constant
        print("31 days")
    case 2:
        print("28 days")
    case 3:
        print("31 days")
    case 4:
        print("30 days")
    case 5:
        print("31 days")
    case 6:
        print("30 days")
    case 7:
        print("31 days")
    case 8:
        print("31 days")
    case 9:
        print("30 days")
    case 10:
        print("31 days")
    case 11:
        print("30 days")
    case 12:
        print("31 days")
    case _: #Default case
        print("Invalid Month Number")
print()


#Q2. Write a menu driven program to perform following operations - Addition, Subtraction, Multiplication, Division
#Ans:-
print("---------Operations-------")
print("1.Addition","2.Subtraction","3.Multiplication","4.Division",sep='\n')
choice=int(input("Enter your choice : "));
a=int(input("enter 1st number : "));
b=int(input("enter 2nd number ; "));
match choice:
    case 1:
        #Addition Operation will perform
        #pass
        print(a+b);
    case 2:
        #Subtraction operation will perform
        #pass
        print(a-b);
    case 3:
        #Multiplication operation will perform
        #pass
        print(a*b);
    case 4:
        #Division operation will perform
        #pass
        print(a/b);
    case _: #Default case
        print("Invalid choice ");
print()


#Q3. Write a menu driven program with the following options:-
"""
a. Check whether a given set of three numbers are lengths of an isosceles triangle or not
b. Check whether a given set of three numbers are lengths of sides of a right angled triangle or not
c. Check whether a given set of three numbers are equilateral triangle or not 
d. Exit. 
"""
#Ans:-
print("a. Check whether a given set of three numbers are lengths of an isosceles triangle or not")
print("b. Check whether a given set of three numbers are lengths of sides of a right angled triangle or not")
print("c. Check whether a given set of three numbers are equilateral triangle or not ")
print("d. Exit")
a,b,c=int(input("Enter 1st side of triangle : ")),int(input("Enter 2nd side of triangle : ")),int(input("enter 3rd side of triangle : "))
choice=ord((input("Enter your choice : "))); #unicode of character will store in choice variable
match choice:
    case 97: #unicode of a
        pass
    case 98: #unicode of b
        pass
    case 99:
        pass
    case 100:
        pass
    case _:
        print("Invalid Choice")
print()


#Q4. Write a program which takes user’s age and display the category of person.
#Age below 10 years- Kid, Age below 20 - Teen, Age below 40 - young, Age below 60 -Experienced, Age above or equal 60 - Senior Citizen.
age=int(input("enter Your age : "))
if age<10:
    a=1
elif age<20:
    a=2
elif age<40:
    a=3
elif age<60:
    a=4
else:
    a=5
match a:
    #if age<10:  Note:-Don't write if instead of case
    case 1:
        print("Kid")
    case 2:
        print("Teen")
    case 3:
        print("Young")
    case 4:
        print("Experienced Person")
    case 5:
        print("Senior Citizen")
    case _:
        print("Enter your valid age")
print()
#Q. what will be the alternate solutions ?
#is there any method like in switch case for sequence of numbers ? switch x{ case 2...40: print(" ckj")}



#Q5. Write a program which takes a number from user.
#Print Saurabh Shukla if the number is even, print Prateek Jain if the number is negative odd number and print Aditya Choudhary if number is positive odd number.
#Ans:-
n=int(input("Enter a number : "))
match n&1:
    case -1:
        print("Prateek jain")
    case 1:
        print("Adiya choudhary")
    case 0:
        print("Saurabh Shukla")
print()


#Q6. Write a python program to check whether a given string is a multiword string or single word string using match case statement
#Ans:-
string=str(input("Enter a string : "));
#I don't know how to do this with match case
"""
But i can found the no. of words in a string with function E.g:-
def func(v):
    length=len(v)
    i=length-1
    count=0
    while length:
        if i==len(v)-1 and v[i]!=" " or v[i]==" " and v[i-1]!=" ":
            count+=1
        length-=1
        i-=1
        if length==1:
            break
    print(count)
"""



#Q7. Write a python program to check whether a given number is positive, negative or zero using match case statement
#ans:-
n=int(input("Enter a number : "));
if n==0:
    x=1 #so that we can't get division by error if n==0
else:
    x=-n
match n/x:
    case 1:
        print("Negative number")
    case -1:
        print("Positive number")
    case 0:
        print("number is Zero")
print()


#Q8. Write a python script to check whether two given strings are identical, first string comes before the second in dictionary order or first string comes after the second string in dictionary order using match case statement
#Ans:-
str1=str(input("Enter 1st string : "))
str2=str(input("Enter 2nd string : "))
match  (0 if str1==str2 else True) if str1>=str2 else False:  #IMP ---> precise coding
    case True:
        print("String 1 comes after String 2")
    case False:
        print("String 2 comes after String 1")
    case 0:
        print("Both string are identicals ")
print()


#Q9. Write a python script to check whether a given year is
"""
a. Non century leap year
b. Century leap year
c. Non century non leap year
d. Century non leap year
"""
#Ans:-
#century means multiple of 100
n=int(input("Enter a number : "))
match (11 if n%400==0 else 10) if n%100==0 else (1 if n%4==0 else 0): #if 1st digit is 1 then it means it's a century year and 0 means its a non-century year
    case 0:#means 00                                             #if 2nd digit is 1 then it's a leap year otherwise it's a non-leap year
        print("It's a Non-century non-leap year")                #leading zero in decimal integer literals are not permitted in python --> Error
    case 1:#means 01                                             #so we can also write 0 only instead of 00 and 1 instead of 01 where, here leading 0 denotes it's a non-century year
        print("It's a Non-century leap year")
    case 10:
        print("It's a century non-leap year")
    case 11: #we can also write default case instead of this
        print("It's a century leap year")
print()


#Q10. Write a program to display day name on the basis of user’s liking of a colour. Ask user for his favorite colour. User can answer in a sentence like “I like red colour”.
'''
Assuming all colour name entered by user is in lowercase. Use match case to display day name associated with the colour.
a. Yellow - Monday
b. Blue - Tuesday
c. Orange - Wednesday
d. White - Thursday
e. Black - Friday
f. Red - Saturday
g. All other colours - Sunday
'''
#Ans:-
x=str(input("Enter your favourite Colour in lowercase : "))
if "yellow" in x:
    choice=a
elif "blue" in x:
    choice=b
elif 'orange' in x:
    choice=c
elif '''white''' in x:
    choice=d
elif """black""" in x:
    choice=e
elif "red" in x:
    choice=f
match choice:
    case 97:
        print("Monday")
    case 98:
        print("Tuesday")
    case 99:
        print("Wednesday")
    case 100:
        print("Thrusday")
    case 101:
        print("Friday")
    case 102:
        print("Saturday")
    case _: #BUT What if someone doesn't give the colour name then also it prints the sunday
        print("Sunday") #for other colours
print()
