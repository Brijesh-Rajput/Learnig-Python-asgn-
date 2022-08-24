#Q1. Write a python script to calculate sum of first N natural numbers
#Ans:-
sum=0
for i in range(eval(input("Enter only a Number : "))):  #here i have used eval function instead of int function
    sum+=i
print("Sum of Natural numbers is %d"%sum)
print()


#Q2. Write a python script to calculate sum of square of first N natural numbers
#ans:-
n=int(input("Enter a Number : "))
sum=0
for i in range(n):
    sum+=(1+1)**2
print("Sum of square of 1st %d Natural Numbers is %d"%(n,sum));
print()


#Q3. Write a python script to calculate sum of cubes of first N natural numbers
#Ans:-
n=int(input("Enter a Number : "))
sum=0
i=n
while n:
    sum+=n**3
    n-=1
print("Sum of cubes of 1st %d Natural numbers is %d"%(i,sum))
print()


#Q4. Write a python script to calculate sum of first N odd natural numbers
n=int(input("Enter a Number : "))
sum=0    #we pass the value of end
for x in range(n):  #by default beg=0,sep=1
    sum+=2*x+1
print("Sum of 1st %d odd natural numbers is %d"%(n,sum))
print()


#Q5.  Write a python script to calculate sum of first N even natural numbers
#Ans:-
n=int(input("Enter a Number : "))
sum=0    #we pass the value of end=n and beg=1
for x in range(1,n+1):  #by default sep=1
    sum+=2*x
print("Sum of 1st %d even natural numbers is %d"%(n,sum))
print()


#Q6. Write a python script to calculate factorial of a given number
fact=1;
for x in range(1,int(input("Enter a Number : "))+1): #or range(n,0,-1)
    fact*=x;
print("Factorial of a given number is %d"%fact)
print()


#Q7. Write a python script to count digits in a given number
#Ans:-
count=0
n=int(input("Enter a Number : "))
for i in str(n):  #b'coz string is also an iterable object. we can use for loop only on iterable object
    count+=1
print("There are %d digits in a given number %d"%(count,n))
print()


#Q8. Write a python script to calculate sum of digits of a given number
#Ans:-  IMP NOTE:- here we have convert i into int in for loop b'coz i contains character which is of str type(you can see the type by using type() function inside a loop) not a int type value
sum=0
n=int(input("Enter a Number : "))
for i in str(n):
    sum+=int(i)
print("Sum of digits in a given number %d is %d"%(n,sum))
print()


#Q9. Write a python script to print binary equivalent of a given decimal number. (do not use bin() method)
#Ans:-
n=int(input("Enter a Number : "))
i=n
binary=''
while n:
    binary=str(n%2)+binary
    n//=2  #Don't write / b'coz this is true division NOT Floor division  ==> Don't do this mistake. it's a Blunder
print("Binary equivalent of a given number %d is %s"%(i,"0b"+binary))
print()


#Q10. Write a python script to print the octal equivalent of a given decimal number. (do not use oct() method)
#Ans:-
n=int(input("Enter a Number : "))
i=n
Octal=""
while n:
    Octal=str(n%8)+Octal
    n//=8
print("Octal equivalent of a given number %d is %s"%(i,"0o"+Octal))
print()


