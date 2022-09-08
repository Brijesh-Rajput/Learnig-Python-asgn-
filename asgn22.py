#Q1. Write a recursive python function to calculate sum of first N natural numbers
#Ans:-
def sumN(n):
    if n<=0:  #Here, no need of < (less than) symbol
        return 0
    return n+sumN(n-1)
print(sumN(10))


#Q2. Write a recursive python function to calculate sum of first N odd natural numbers
#Ans:-
def sumOdd(n):
    if n<=0:
        return 0
    return 2*n-1+sumOdd(n-1)
print(sumOdd(5))


#Q3. Write a recursive python function to calculate sum of first N even natural numbers
#Ans:-
def sumEven(n):
    if n<=0:
        return 0
    return 2*n+sumEven(n-1)
print(sumEven(5))


#Q4. Write a recursive python function to calculate sum of squares of first N natural numbers
#Ans:-
def sumSquareN(n):
    if n==0:
        return n
    return n**2+sumSquareN(n-1)
print(sumSquareN(5))


#Q5. Write a recursive python function to calculate sum of cubes of first N natural numbers
#Ans:-
def sumCubesN(n):
    if n==0:
        return 0
    return n**3+sumCubesN(n-1)
print(sumCubesN(5))


#Q6. Write a recursive python function to calculate the factorial of a number.
#Ans:-
def fact(n):
    if n==1:
        return n
    return n*fact(n-1)
print(fact(5))


#Q7. Write a recursive python function to calculate sum of the digits of a given number
#Ans:-
def digit_sum(number):
    if number==0:
        return 0
    return number%10+digit_sum(number//10)
print(digit_sum(102354600))


#Q8. Write a recursive python function to print binary of a given decimal number.
#Ans:-
def binary(number):
    if number==1:
        return str(number)
    return binary(number//2)+str(number%2)
print(binary(25))


#Q9. Write a recursive python function to print octal of a given decimal number
#Ans:-
def octal(number):
    if 0<number<8:
        return str(number)
    return octal(number//8)+str(number%8)
print(octal(253))


#Q10. Write a recursive python function to find the Nth term of the Fibonacci series
#Ans:-
def fibbo(n):
    if n==1 or n==2:
        return n-1
    return fibbo(n-1)+fibbo(n-2)
print(fibbo(5))




