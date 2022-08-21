#Q1. Write a python script to print MySirG N times on the screen
#ans:-
n=int(input("Enter the size of n to print MysirG n-times on screen : "));
i=1;
while i<=n:
    print("MySirG",end=" ");
    i+=1;
print()


#Q2. Write a python script to print first N natural numbers
#ans:-
n=int(input("Enter a Number : "));
print("First %d Natural numbers are :- "%n,end=" ")
i=1;
while i<=n:
    print(i,end=" ");
    i+=1;
print()


#Q3. Write a python script to print first N natural numbers in reverse order
#ans:-
n=int(input("Enter a Number : "));
print("First %d Natural numbers in reverse order are :- "%n,end=" ")
i=1;
while i<=n:
    print(n+1-i,end=" ");
    i+=1;
print()


#Q4. Write a python script to print first N odd natural numbers
#ans:-
n=int(input("Enter a Number : "));
print("First %d Odd Natural numbers are :- "%n,end=" ")
i=1;
while i<=n:
    print(2*i-1,end=" ");
    i+=1;
print()


#Q5. Write a python script to print first N odd natural numbers in reverse order
#ans:-
n=int(input("Enter a Number : "));
print("First %d Odd Natural numbers in reverse order are :- "%n,end=" ")
i=1;
while i<=n:
    print(2*n+1-2*i,end=" ");
    i+=1;
print()


#Q6. Write a python script to print first N even natural numbers
#ans:-
n=int(input("Enter a Number : "));
print("First %d even Natural numbers are :- "%n,end=" ")
i=1;
while i<=n:
    print(2*i,end=" ");
    i+=1;
print()


#Q7. Write a python script to print first N even natural numbers in reverse order
#ans:-
n=int(input("Enter a Number : "));
print("First %d even Natural numbers in reverse order are :- "%n,end=" ")
i=1;
while i<=n:
    print(2*n+2-2*i,end=" ");
    i+=1;
print()


#Q8. Write a python script to print squares of first n natural numbers
#ans:-
n=int(input("Enter a number : "));
print("square of first %d Natural numbers are :- "%n,end=" ")
i=1;
while i<=n:
    print(i**2,end=" ");
    i+=1;
print()


#Q9. Write a python script to print cubes of first n natural numbers
n=int(input("Enter a number : "));
print("cube of first %d Natural numbers are :- "%n,end=" ")
i=1;
while i<=n:
    print(i**3,end=" ");
    i+=1;
print()


#Q10. Write a python script to print first 10 multiples of n
#ans:-
n=int(input("Enter a number : "));
print("Table of %d"%n);
i=1;
while i<=10:
    print("%d * %d = %d"%(n,i,n*i));
    i+=1;
print()
