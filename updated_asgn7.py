#updated some solutions of matchcase asgn-7
#we can use if condition with case in match case

#Q1. Write a python script to display the number of days in a given month number.
#Ans:-
month=int(input("Enter a month number : "))
match month:
    case month if month in (1,3,5,7,8,10,12): #it can be list or set
        print("31 days")
    case month if month in [4,6,9,11]:
        print("30 days")
    case 2:  #or case month if month in {2}:  #this is set
        print("28 or 29 days")
    case _:
        print("Enter a Valid month number ")
print()


#Q4. Write a program which takes user’s age and display the category of person.
#Age below 10 years- Kid, Age below 20 - Teen, Age below 40 - young, Age below 60 -Experienced, Age above or equal 60 - Senior Citizen.
age=int(input("enter Your age : "))
match age:
    case age if age<10:
        print("Kid")
    case age if age<20: #this case will select only when 10<age<20. if age is 10 then above case will select b'coz it comes first
        print("Teen")
    case age if age<40:
        print("Young")
    case age if age<60:
        print("Experienced")
    case age if age>=60:
        print("Senior Citizen")
    case _: #Acc. to me this by default case will never select.
        print("Enter your valid age")
print()
#is there any method like in switch case for sequence of numbers ? switch x{ case 2...40: print(" ckj")} --> above solutions



#Q5. Write a program which takes a number from user.
#Print Saurabh Shukla if the number is even, print Prateek Jain if the number is negative odd number and print Aditya Choudhary if number is positive odd number.
#Ans:-
n=int(input("Enter a number : "))
match n:
    case n if n%2==-1:
        print("Prateek jain")
    case n if n%2==1:
        print("Adiya choudhary")
    case n if n%2==0:
        print("Saurabh Shukla")
print()


#Q6. Write a python program to check whether a given string is a multiword string or single word string using match case statement
#Ans:-
string=str(input("Enter a string : ")).strip()
match string:
    case string if ' ' in string:
        print("Multiword-String")
    case string if ' ' not in string:
        print("SingleWord-String")
print()


#Q7. Write a python program to check whether a given number is positive, negative or zero using match case statement
#ans:-
n=int(input("Enter a number : "));
match n:
    case n if n<0:
        print("Negative number")
    case n if n>0:
        print("Positive number")
    case n if n==0:
        print("number is Zero")
print()


#Q8. Write a python script to check whether two given strings are identical, first string comes before the second in dictionary order or first string comes after the second string in dictionary order using match case statement
#Ans:-
str1,str2=input("Enter 1st string : "),input("Enter 2nd string : ")
match (str1,str2): #IMP ---> precise coding
    case (str1,str2) if str1>str2:
        print("String 1 comes after String 2")
    case (str1,str2) if str2>str1:
        print("String 2 comes after String 1")
    case (str1,str2) if str1==str2:
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
match n: #(11 if n%400==0 else 10) if n%100==0 else (1 if n%4==0 else 0): #if 1st digit is 1 then it means it's a century year and 0 means its a non-century year
    case n if n%100!=0 and n%4!=0:
        print("It's a Non-century non-leap year")
    case n if n%100!=0 and n%4==0:
        print("It's a Non-century leap year")
    case n if n%400!=0: #instead of n%100==0 and n%400!=0
        print("It's a century non-leap year")
    case n if n%400==0:
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
l1=["Yellow","Blue","Orange","White","Black","Red"]
for color in l1:
    if color in x:
        c=color
        break
else:
    c=other
match c:
    case "yellow": #Don't write this massive code  --> case c if c=="Yellow"
        print("Monday")
    case "Blue":
        print("Tuesday")
    case "Orange":
        print("Wednesday")
    case "White":
        print("Thrusday")
    case "Black":
        print("Friday")
    case "Red":
        print("Saturday")
    case "other":
        print("Sunday")
print()
