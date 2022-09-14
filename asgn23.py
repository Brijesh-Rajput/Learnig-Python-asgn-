#Doubt in Ques 9. ==> check Q10 also
#Q9. Error:-   File "E:\MYCODE\Try.py", line 145, in <module>
#     triangle(5,8,6)
# TypeError: 'NoneType' object is not callable  ==> These error occurs due to my silly mistake which i mention in the code also.
#Finally,Problem Solve!!

#Q1. Use iter and next method to access all the elements of a given set using while loop
#Ans:-
set1={1:"Ritesh",2:"Rahul",3:"Brijesh",4:"Saurabh"}
it=iter(set1)
set_length=len(set1)
while set_length:
    key=next(it)
    print("Key : {} and Value : {}".format(key,set1[key]))
    set_length-=1
print()


#Q2. Create a generator to produce first n odd natural numbers
#Ans:-
def generate_odd_numbers(n):
    i=1  #instead of this big code we can use range to traverse from n to 1. see Q4 wrong commented Answer
    while i<=n:
        #print("Hello")  --> this stmt will not execute untill we will not use next function
        yield 2*i-1
        i+=1
n=int(input("Enter a number : "))
it=generate_odd_numbers(n)
while n:
    print(next(it),end=" ")
    n-=1
print()


#Q3. Create a generator to produce first n even natural numbers
#Ans:-
def generate_even(n):
    for i in range(1,n+1):
        yield 2*i
for e in generate_even(int(input("Enter a Number : "))):  #NOTE:- We can use for loop only on iterable object and on generator function
    print(e,end=" ")
print()


#Q4. Create a generator to produce squares of first N natural numbers
#Ans:-
def generate_square(n):
    for e in range(1,n+1):
        yield e*e
for e in generate_square(int(input("enter a Number : "))):
    print(e,end=" ")
print()
""" Wrong code
def generate_square(n):
    for e in range(n,-1,-1): #sep=-1
        yield e
for e in generate_square(int(input("enter a Number : "))):
    print(e,end=" ")
"""


#NOTE:- yield keyword is responsible to pause the function and generate a new value


#Q5. Create a generator to produce first n terms of Fibonacci series
#Ans:-
def generate_fiboSeries(n):
    a,b=1,0
    for e in range(0,n):
        yield b   #print(b,end=" ") --> Don't do this mistake instead of writing yield. if done then this function will not called as generate until we will not use yield keyword
        a,b=b,a+b
it=generate_fiboSeries(int(input("Enter a Number : ")))
for e in it:
    print(e,end=" ")
print()
"""
Or 
for e in generate_fiboSeries(int(input("Enter a Number : "))):
    print(e,end=" ")
print()
"""


#Q6. Create a generator to produce first n prime numbers
#Ans:-  ---> is there any short answer of that ?
def generate_prime(n):
    i=2
    count=0
    while count<n:
       for e in range(2,i):
           if i%e==0:
               break
       else:
           yield i
           count+=1  #to stop the loop when n times prime number is generated the loop will stop
       i+=1
for e in generate_prime(int(input("Enter a Number : "))):
    print(e,end=" ")
print()


#Q7. Create an endless iterator using generator method to produce terms of Fibonacci series
#Ans:-
def generate_Endless_fiboSeries():
    a,b=1,0
    while True:
        yield b
        a,b=b,a+b
it=generate_Endless_fiboSeries()
l1=list() #empty list
while True:
    choice = input("Do you Want to generate Next Fibonacci series[Y/N] : ")
    if choice=="y" or choice=="Y":
        x=next(it)
        l1.append(x)
        print("{} is generated".format(x))
    else:
        print("Generated list is {}".format(l1))
        break
#Don't use while-else loop b'coz if does then else block of while loop will never execute. else block of loop execute when loop is executed fully without any break situation
print()


#Q8. Create an endless iterator using generator method to produce Prime numbers
#Ans:-
def generate_endless_prime():
    i=2
    while True:
        for e in range(2,i):
            if i%e==0: #e&1==1 --> condition for odd number
                break
        else:
            yield i
        i+=1
it=generate_endless_prime()
l1=list() #empty list
while True:
    choice = input("Do you Want to generate Next Prime Number[Y/N] : ")
    if choice=="y" or choice=="Y":
        x=next(it)
        l1.append(x)
        # l1.append(next(it)) #Why this gives me an error ?
        print("Generated list is {}".format(l1))
    else:
        print("Generated list is {}".format(l1))
        break
print()


#Q9. Define a function which takes lengths of three sides of a triangle as arguments and display the perimeter or triangle.
# Define and apply a decorator which checks for the validity of the triangle on the basis of lengths of the side.
# This makes the perimeter to be displayed when the triangle can exist with the given lengths of the sides.
#Ans:-
def decor_triangle(triangle):
    def isvalidTriangle(a,b,c):
        if a<=0 or b<=0 or c<=0 :
            print("Invalid triangle")
        else:
            print("Valid Triangle")
            return triangle(a,b,c)
        # return isvalidTriangle  --> wrong  ===> Don't do these mistakes
    return isvalidTriangle #-->right    --> this return stmt is written inside a decor_triangle function()  NOT in isvalidTriangle() function

#When user call triangle() function then function which return by a decor_triangle() function will execute instead of triangle() function
@decor_triangle
def triangle(a,b,c):
    print("Perimeter of triangle is ",a+b+c)

print()
triangle(5,8,3)
triangle(1,0,59)
triangle(-1,5,8)


#Q10. Define a function which calculates HCF of two numbers. Define and apply a decorator to check whether two given numbers are co-prime or not.
#Ans:-
def decor_hcf(hcf):
    def isCoprime(a,b):  #coprime means Whose hcf is one
        # for e in range(2,a+1 if a<b else b+1):  --> Here, im writing brut-force code to check, whether both two numbers are coprime or not ?
        if hcf(a,b)==1:
            print("Both numbers are co-prime number")
        else:
            print("Both numbers are not a co-prime number")
    return isCoprime(a,b)

@decor_hcf
def hcf(a,b):  #Brut-force
    for e in range( a if a<b else b , 0 , -1): #sep=-1
        if a%e==0 and b%e==0:
            return e
hcf(4,15)
hcf(10,15)

