#Q1. Write a python script to check whether a given number is positive or non-positive
#Ans:-
print("Positive" if int(input("Enter a number : "))>0 else "Non-Positive");


#Q2. Write a python script to check whether a given number is divisible by 5 or not
#Ans:-
print("Not Diivisible by 5" if int(input("Enter a Number : "))%5 else "Divisible by 5");


#Q3. Write a python script to check whether a given number is even or odd
#Ans:-
x=int(input("Enter a Number : "));
if x&1:
    print("Odd Number");
if x&1==0:
    print("Even Number");


#Q4. Write a python script to print greater between two numbers. Print number only once even if the numbers are the same
#Ans:-
x=int(input("Enter 1st Number "));
y=int(input("Enter 2nd Number"));
if x>y:
    print("Greater Number is ",x); #print("Greater Number is %d"%x);
else:
    print("Greater Number is %d"%x);
"""OR #Below code is wrong!
x if int(input("Enter 1st Number : "))>int(input("Enter 2nd Number : ")) else y  
//Here, Single line if else does'nt fit suitable ---> wrong its suitable.
See below code to know how to write the code for single line if else  
"""


#Q5. Write a python script to print two given words in dictionary order
#Ans:-
x=input("Enter 1st word : ");
y=input("Enter 2nd word : ");
'''to print which word is greater 
print(x if x>y else y);  #NOTE:- No need to write here different print() function for both x and y
////
NOTICE BELOW CODE:-
x=input("Enter 1st word : ");
Enter 1st word : vvmv
y=input("Enter 2nd word : ");
Enter 2nd word :  vhjkj
print(x,y if x>y else y,x); #Think why ?-> I Know
vvmv  vhjkj vvmv
'''
if x>y:
    print(x,y);
else:
    print(y,x);


#Q6. Write a python script to check whether a given number is a three digit number or not.
#Ans:-
print("# digit Number" if 100<=int(input("Enter a Number : "))<=999 else "Not a 3 digit Number");

"""Shell script code -----> IMP
>>>x = print("Hello" if 3 > 4 else "HII");
>>>HII
>>>print(x)
>>>None
That means, print() function returns None:-

>>>x=print("Hello") if 3>4 else print("Hii")
>>>Hii
>>>print(x)
>>>None
"""


#Q7. Write a python script to check whether a given number is positive, negative or zero.
#Ans:-
x=int(input("Enter a Number : "));
if x>0:
    print("Positive Number");
elif x<0:
    print("Negative Number");
else:
    print("Number is Zero");


#Q8. Write a python script to check whether a given quadratic equation has two real & distinct roots, real & equal roots or imaginary roots
#Ans:-
print("Quadratic Equation :- ax^2+bx+c=0");
a=int(input("Enter the coffecient of x^2 that is value of a : "));
b=int(input("Enter the coffecient of x that is value of b : "));
c=int(input("Enter the value of c : "));
d=b**2-4*a*c;
if d==0:
    print("Roots are Real and Equal");
elif d>0:
    print("Roots are Real and unequal");
else:
    print("No Real Roots,Imaginary roots");


#Q9. Write a python script to check whether a given year is a leap year or not.
#ans:-
x=int(input("Enter a year : "));
if x%4==0 and (x%100!=0 or x%400==0):
    print("Leap Year");
else:
    print("Not a Leap Year");


#Q10. Write a python script to print greater among three numbers. Print number only once even if the numbers are the same
#Ans:-
x=int(input("Enter three Number(After entering 1st number press Enter Key) : "));
y=int(input());
z=int(input());
if x>y and x>z:
    print(x);
elif y>z and y>x:
    print(y);
elif z>x and z>y:
    print(z);
else:
    print(x);


#Q11. Write a python script to take the month value in numeric format and display the number of days in it.
#ans:-
''' 
jan,mar,may,jul,aug,oct,dec(1,3,5,7,8,10,12) --> 31 days
                           (4,6,9,11) ---> 30 days
                           (2) ---> 28 days Generally BUT in leap year there are 29 days 
'''
n=int(input("enter a month number : "));
if 1<=n<=12:
    if n==2:
        print("Have 28 days");
    elif n<8 and n&1==1 or n>=8 and n&1==0:
        print("Have 31 days");
    else:
        print("Have 30 days");
else:
    print("enter a Valid Month Numer");


#Q12. Write a python script to accept one complex number from the user and display the greater number between real part and imaginary part
#ans:-
x=complex(input("Enter one complex number but condition is that instead of i(iota) write j.\n For E.g:- a+bj \n Enter :- "));
if x.imag>x.real:
    print("imaginary part is greater ",x.imag);
else:
    print("x.real");
