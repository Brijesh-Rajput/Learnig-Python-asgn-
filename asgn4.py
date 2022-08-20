#Q1. Write a python script to take your name as input from the user and then print it.
#Ans:-
name=input("Enter your name : ");
print("Your name is %s"%name);


#Q2. Write a python script to take input from the user. Input must be a number.
#Ans:-
number=int(input("Enter a number : "));
print("number is %d"%number);


#Q3. Write a python script which takes two numbers from the user, then calculate their sum and display the result.
#Ans:-
a=int(input("Enter 1st number : "));
b=int(input("Enter 2nd number : "));
sum=a+b;
print("sum of %d and %d is %d"%(a,b,sum));


#Q4. Write a python script which takes the radius from the user and display area of a circle.
#Ans:-
radius=int(input("Enter the radius of a circle : "));
area=3.14*radius**2;
print("area of circle is %f"%area);
"""use inbuilt pi value
#E.g:-
import math
radius=int(input("Enter the radius of a circle : "));
area=math.pi*radius**2;
print("area of circle is %f"%area);
"""


#Q5. Write a python script to calculate the square of a number. Number is entered by the user.
#Ans:-
number=int(input("Enter a number : "));
square=number**2;
print("Square of %d is %d"%(number,square));


#Q6. Write a python script to calculate the area of Triangle. Number is entered by the user.
#Ans:-
a=int(input("Enter the three side of triangle :-\n Enter 1st side : "));
b=int(input("Enter 2nd side of triangle : "));
c=int(input("Enter 3rd side of triangle : "));
#Now using Heron's Formula to find the area of triangle
s=(a+b+c)/2; #semi perimeter
Area=(s*(s-a)*(s-b)*(s-c))**0.5;
print("Area of Triangle is %f"%Area);


#Q7. Write a python script to calculate average of three numbers, entered by the user
#Ans:-
a=int(input("Enter three numbers(press enter key after entering a number) : "));
b=int(input());
c=int(input());
avg=(a+b+c)/3; #True Division
print("Average of three numbers is %f"%avg);


#Q8. Write a python script to calculate simple interest
#Ans:-
Principal_amount=int(input("Enter Principal amount : "));
ROI=float(input("Enter Rate of Interest in % : "));
N=int(input("Enter rate of interest in yrs : "));
print("Simple interest is %f"%(Principal_amount*ROI*N/100));


#Q9. Write a python script to calculate the volume of a cuboid.
#Ans:-
len=int(input("Enter length of cuboid : "));
breadth=int(input("Enter breadth of cuboid : "));
height=int(input("Enter height of cuboid : "));
volume=len*breadth*height;
print("Volume of cuboid is %d"%volume);


#Q10. Write a python script to calculate area of a rectangle
#Ans:-
len=int(input("Enter length of a reactangle : "));
breadth=int(input("Enter breadth of reactangle : "));
area=len*breadth;
print("Area of rectangle is %d"%area);