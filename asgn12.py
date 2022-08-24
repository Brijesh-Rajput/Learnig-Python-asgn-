#Q1. Write a python script to reverse a number.
#Ans:-
n=int(input("Enter a Number : "))
i=n #Don't forget this line if you want to print the n at last(after the while loop)
r_n=""
while n:
    r_n=str(n%10)+r_n
    n//=10
print("Reverse number of a given number %d is %s"%(i,r_n))  #NOTE:- we will use string b'coz of this type of edge cases  E.g:-n=13500  output:-00531
print()


#Q2. Write a python script to check whether a given number is Prime or not
#Ans:-
n=int(input("Enter a Number : "))
i=2
j=0
while i**2<=n:
    if n%i==0:
        break
    i+=1
else: #else block will execute when control will come out from the while loop without break(that means when while loop executed fully) stmt
    print("It's a Prime Number")
    j=1
if j==0: #Don't write here 1 instead of 0
        print("It's not a prime number")
print()
''' OR  --> try
using sqrt function from math.py modules 
for x in range(2,isqrt(n))
'''


#Q3. Write a python script to print all Prime numbers under 100
#Ans:-
for x in range(2,100):
    i=2
    while i**2<=x:
        if x%i==0:
            break
        i+=1
    else:
        print(x,end=" ")
print()


#Q4. Write a python script to print all Prime numbers between two given numbers (both values inclusive)
#Ans:-
a=int(input("Enter two number \n Enter 1st number : "))
b=int(input("Enter 2nd number : "))
"""
#sep=-1 if a>b else sep=1  ===> How to do this in one line ?  ---> This line gives me an error 
for x in range(a,b+1,sep):
    i = 2
    while i ** 2 <= x:
        if x % i == 0:
            break
        i += 1
    else:
        print(x, end=" ")
print()
"""
""" OR
if user inputs a value in order means 1st_input_number<2nd_input_number:- then below this code
print("Enter two number but condition is that 1st number should be greater than 2nd number")
for x in range(int(input("Enter 1st number : ")),int(input("Enter 2nd number  : ")))
    i = 2
    while i ** 2 <= x:
        if x % i == 0:
            break
        i += 1
    else:
        print(x, end=" ")
print()
"""


#Q5. Write a python script to find next prime number of a given number
#Ans:-
n=int(input("Enter a Number to find the next prime number : "))+1
'''
Note:- here, we will not use range b'coz when we give only one argument then that means loop from 0 to passedValue-1.
       And if we give two value that is value of beg and end then what value will we pass in end ? it should be infinity But what value ?
        and if user want to find the next prime number of that number which we have pass to the end Then Our Output will be false 
That's why we are using while loop         
'''
while n:
    i = 2
    while i ** 2 <= n:
        if n % i == 0:
            break
        i += 1
    else:
        print("Next Prime of given number is %d"%n)
        break
    n+=1
print()


#Q6. Write a python script to print first N prime numbers
#Ans:-
n=int(input("Enter a Number : "))
count=0
x=2 #Don't write here 1
while x:
    i = 2
    while i ** 2 <= x:
        if x % i == 0:
            break
        i += 1
    else:
        print(x, end=" ")
        count+=1
        if count==n:
            break
    x+=1
print()
#Think How can u do with range but condition is that you can't any higher value for end variable of in range. user can enter any high value. it can happen that user can enter value which is greater than end if you pass that value to the range function


#Q7. Write a python script to check whether a given pair of numbers are co-Prime numbers or not.
#Ans:-
a=int(input("Enter a Number : "))
b=int(input("Enter a Number : "))
#co-prime no.'s ===> Hcf is 1
#code for hcf
if a>b:
   a,b=b,a
smaller=a
while smaller:
     if not(a%smaller) and not(b%smaller) :
         hcf=smaller
         break
     else:
         smaller-=1
print("It's a Co-prime Numbers" if hcf==1 else "It's Not a Co-prime Numbers")
print()


#Q8. Write a python script to print first N terms of a Fibonacci series
#Ans:-
n=int(input("Enter a Number : "))
a=-1
b=1
print("First N terms of Fibonacci series are :- ",end=" ")
while n:
    sum=a+b
    print(sum,end=" ")
    a=b
    b=sum
    n-=1 #Don't forget otherwise infinite times loop will execute 
print()


#Q9. Write a python script to calculate LCM of two numbers
#Ans:-
#LCM(a,b)=(a*b)/HCF(a,b)
a=int(input("Enter a Number : "))
b=int(input("Enter a Number : "))
if a>b:
    a,b=b,a
highest=b
while highest:
      if not(highest%a) and not(highest%b):
          lcm=highest
          break
      else:
          highest+=1
print("LCM of two numbers %d and %d is %d"%(a,b,lcm))
print()


#Q10.  Write a python script to calculate HCF of two number
#Ans:-
a=int(input("Enter a Number : "))
b=int(input("Enter a Number : "))
if a>b:
   a,b=b,a
smaller=a
'''cnf it ==> hcf=1 #don't forget to initalize hcf outside the loop otherwise it will throw an error b'coz hcf is exist upto that block where it's created acc. to me'''
while smaller:
     if not(a%smaller) and not(b%smaller) :
        hcf=smaller #no need to declare outside if we want to use it outside. cnf it ?
        break
     else:
       smaller-=1
print("Hcf of two number %d and %d is %d"%(a,b,hcf)) #here,no need of while else
print()
"""OR
To reduce the time complexity :- use below code
import math
hcf=1
for i in range(1,math.isqrt(a)): #by default value of sep is 1
    if a%i==0 and b%i==0:
        x=a//i
	    y=b//i
        if x==y:
           hcf=x #or hcf=y
           break
        elif a%x==0 and b%x==0:
           hcf=x
           break
        elif a%y==0 and b%y==0:
           hcf=y
           break
print("Hcf of two number %d and %d is %d"%(a,b,hcf)) #here,no need of while else
print()
"""