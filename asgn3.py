#All Questions are done with using predefined functions

#Q1. Write a python script to convert a number into str type.
#Ans:-
x=56;
print(str(x));


#Q2. Write a python script to print Unicode of the character ‘m’
#Ans:-
print(ord('m')); #ord() function returns unicode of a given character.


#Q3. Write a python script to print character representation of a given unicode 100
#Ans:- ''' IMP'''
x=100;
print(chr(100));  #chr() function takes one argument & it must be an integer and return character of that particular unicode
#Don't write char()  instead of chr()


#Q4. Write a python script to print any number and its binary equivalent
#Ans:-
x=int(input("Enter a number : "));
#print("Binary equivalent of %d is %0b"%(x,bin(x)));  ---> it's a Blunder mistake 1)bin() function returns string not a binary number 2)there is no format specifier like %0b
print("Binary equivalent of %d is %s"%(x,bin(x)));


#Q5. Write a python script to print any number and its octal equivalent.
#Ans:-
x=int(input("Enter a number : "));
print("Octal equivalent of %d is %s"%(x,oct(x)));


#Q6. Write a python script to print any number and its hexadecimal equivalent.
#Ans:-
x=int(input("Enter a number : "));
print("Hexadecimal equivalent of %d is %s"%(x,hex(x)));


#Q7. Write a python script to store binary number 1100101 in a variable and print it in decimal format
#Ans:-
x=0b1100101;
print("Decimal Equivalent of %s is %d"%(bin(x),x));


#Q8. Write a python script to store a hexadecimal number 2F in a variable and print it in octal format.
#Ans:-
x=0x2F;
#print("Octal Equivalent of %s is %d"%(hex(x),oct(x))); """Why this gives me an error ?""" B'coz:- oct() function returns string so format specifier should be %s not %d
print("Binary Equivalent of %s is %s"%(hex(x),oct(x)));

#Q9. Write a python script to store an octal number 125 in a variable and print it in binary format.
#Ans:-
x=0o125;
#print("Binary Equivalent of %s is %d"%(hex(x),bin(x))); """Why this gives me an error ?""" B'coz:- oct() function returns string so format specifier should be %s not %d
print("Binary Equivalent of %s is %s"%(hex(x),bin(x)));


#Q10. Write a python script to add two numbers 25 (in octal) and 39 (in hexadecimal) and display the result in binary format
#Ans:-
x=0o25;
y=0x39;
sum=x+y; #B'coz internally it stores in binary form and prints in decimal form
print("Sum is %s"%bin(sum));

