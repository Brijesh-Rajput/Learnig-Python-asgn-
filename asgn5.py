#Q1. Write a python script to remove the last digit from a given number. (for example, if user enters 2534 then your output should be 253)
#Ans:-
n=int(input("Enter a number : "));
print(n//10);

#Q2. Write a python script to get the last digit from a given number. (for example, if user enters 2089 then your output should be 9)
#Ans:-
n=int(input("Enter a number : "));
print(n%10);

#Q3. Write a python script to swap data of two variables
#Ans:-
a,b=int(input("Enter two value(After entering a value press Enter key): ")),int(input()); #work of input() function completes when we press enter key
#a,b=5,6
b,a=a,b; #work like as a variable:- for E.g:- a=a+2
print(a,b);

#Q4. Write a python script to find x power y, where values of x and y are given by user
#Ans:-
x=int(input("Enter a number : "))
y=float(input("Enter power of number %d"%x)) """IMPORTANT"""
print(x**y);

#Q5. Write a python script which takes a three digit number from the user and displays only its first digit.
#Ans:-
x=int(input("Enter ony three digits number : "));
if 100<=x<=999:
    #pass;
    print("First Digit is %d"%(x//100));
else:
    print("Invalid Input");

#Q6. Write a python script which takes a three digit number from the user and displays only its middle digit.
#Ans:-
x=int(input("Enter ony three digits number : "));
if 100<=x<=999:
    #pass;
    print("Middle Digit is %d"%(x%100)//10)); #Or print((x//10)%10);
else:
    print("Invalid Input");

#Q7. Write a python script which takes a three digit number from the user and displays only its last digit.
#Ans:-
x=int(input("Enter ony three digits number : "));
if 100<=x<=999:
    #pass;
    print("Last Digit is %d" % (n % 10));
else:
    print("Invalid Input");


#Q8. Write a python script to use IN operator to display the data present in the list
#Ans:-  in & not in operator are used in iterable container(multiple values stores). E.g:- string,range,tuple,set,dictionary
#in oprtr in string
x=input("Enter a String : ");
y=input("Enter a part of string to check whether it is present in the string or not : ");
if y in x:
    print("Present");
else:
    print("Not present in the string ");

#Q9. Write a python script to use NOT IN operator to display the data not present in list
#Ans:-
x=input("Enter a String : ");
y=input("Enter a part of string to check whether it is present in the string or not : ");
if y not in x:
    print("True, it's Not present in string");
else:
    print("present in the string ");

#Q10. . Write a python script to use IS operator to display if both variables are the same object or not?
#Ans:-
x,y=5,5;
a,b,c,d="Hello","""Hello""",'Hello','''Hello''';
if x is y:
    print(True);  #True is not a string value
else:
    print(False);
"""   OR --------> IMP
if id(x)==id(y):
    print(True);
else :
    print(False);
"""
if a is not b is not c is not d :
    print(True);
else:
    print(False);