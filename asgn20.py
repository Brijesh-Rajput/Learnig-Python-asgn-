#Q1. Write a python program to create a function that takes a list and returns a new list with the original list's unique elements.
#Ans:-
def unique_elements(list1):
    x=dict(list1)
    return list(dict)
print(unique_elements([10,15,18,19,24,36,84,92,67,37,28,43,49,18,19,15,28]))


#Q2. Write a python program to create a function that takes a number as a parameter and checks if the number is prime or not.
#Ans:-
def isprime(number):
    for i in range(2,number): #actually loop upto sqrt(number)
        if number%i:
            return 1
        else:
            return 0
print(isprime(91))


#Q3. Write a python program to create a function that prints the even numbers from a given list. Sample List : [1, 2, 3, 4, 5, 6, 7, 8, 9]
#Ans:-
def print_even(list1):
    for i in list1:
        if i%2==0:
            print(i,end=" ")
    print()
print(print_even([1, 2, 3, 4, 5, 6, 7, 8, 9]))


#Q4. Write a python program to create a function that checks whether a passed string is palindrome or not.
#Ans:-
def isPalidrome(string):
    if string==string[::-1]:   # Wrong logic ---> ",".join([e for e in string[::-1]])
        return 1
    else:
        return 0
print(ispalidrome("NamaN"))


#Q5. Write a python program to create a function to find the Min of three numbers.
#Ans:-
def minimum(a,b,c):
    if a<b and a<c:
        return a
    elif b<c and b<a:
        return b
    else
        return c
    #Wrong----->return a if a<b and a<c else (return b if b<c and b<a else return c)
print(minimum(15,89,34))


#Q6. Write a python program to create a function and print a list where the values are square of numbers between 1 and 30.
#Ans:-
def print_list():
    print([e*e for e in range(1,31)])
print_list()


#Q7. Write a python program to access a function inside a function.
#Ans:-
def print_Hello():
    print("Hello")
def use():
    print_Hello()
print_Hello()


#Q8. Write a python program to create a function that accepts a string and calculate the number of upper case letters and lower case letters.
#Ans:-
def string(string):
    lower_letters,upper_letters=0,0
    for e in string:
        if 'a'<e<'z':
            lower_letters+=1
        elif 'A'<e<'Z':
            upper_letters+=1
    print(upper_letters,lower_letters)
string("   hebde dmclk 383 40 ? !@ $ llkdlcnnCADVFBGN      ")


#Q9. Write a python program to create a function to check whether a string is a pangram or not.
#Ans:-
#pangram string means :- string which contains all the alphabets
#My Codition :- Don't consider case sensitive
def ispangram(string):
    for e in range(65,98):
        if char(e) not in string and char(e).lower() not in string:
            return 0
    return 1
print(ispangram("The Quick Brown Fox Jumps Over the Lazy Dog > ? #@ 121 "))


#Q10. Write a python program to create a function to check whether a string is a angram or not.
#Ans:-
#angram string means :- strings whose order is changed but contains same alphabets on both the string
def isangram(string1, string2):
    string1=sorted(string1)
    string2=sorted(string2)
    if string1==string2:
        return 1
    return 0


"""
Q10. wrong answer
def isangram(string1, string2):
    if len(string1)!=len(string2):
        return 0
    for e in string1:
        if e not in string2:
            return 0
    return 1
#Note taste cases :- string1="Helolo"  string2="HeloMn"  ====> these are not angram string 

"""
"""
Q8. Wrong ===> some taste cases like "   hebde dmclk 383 40 ? !@ $ llkdlcnnCADVFBGN      "
def string(string):
    #wrong code 
    length=len(string)
    l1=sorted(string)
    upper_case_letters,lower_case_letters=0,0
    for e in l1:
        if 'a'<e<'z':
            upper_case_letters=l1.index(e)
        else:
            lower_case_letters=length-upper_case_letters
            break
            #doesn't work ---> upper_case_letters=l1.index(e) if 'a'<e<'z' else break;
    print("No. of Upper case letters = %d and No. of Lower case letters = %d"%(upper_case_letters,lower_case_letters))
#or traverse all string and count upper and lower case letters
string("Hello Everyone How are you ? # $ ")

"""
