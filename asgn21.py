#Q1. Write a recursive python function to print first N natural numbers.
#Ans:-
def print_NaturalNumbers(n):
    if n>0:
        print_NaturalNumbers(n-1)
        print(n,end=" ")
print_NaturalNumbers(48)
print()


#Q2. Write a recursive python function to print first N natural numbers in reverse order
#Ans:-
def print_rNaturalNumbers(n):
    if n>0:
        print(n,end=" ")
        print_rNaturalNumbers(n-1)
    """
    n  n-1 n-2 n-3 n-4 ... 1
    n n-1 n-2 n-3 n-4 ... 2
    """
print_rNaturalNumbers(5)
print()


#Q3. Write a recursive python function to print first N odd natural numbers
#Ans:-
def print_odd(n):
    if n>0:
        print_odd(n-1)
        print(2*n-1,end=" ")
print_odd(5)
print()


#Q4. Write a recursive python function to print first N odd natural numbers in reverse order
#Ans:-
def print_rodd(n):
    if n>0:
        print(2*n-1,end=" ")
        print_rodd(n-1)
print_rodd(5)
print()


#Q5. Write a recursive python function to print first N even natural numbers.
#Ans:-
def print_even(n):
    if n>0:
        print_even(n-1)
        print(2*n,end=" ")
print_even(5)
print()


#Q6. Write a recursive python function to print first N even natural numbers in reverse order.
#Ans:-
def print_reven(n):
    if n>0:
        print(2*n,end=" ")
        print_reven(n-1)
print_reven(5)
print()


#Q7. Write a recursive python function to print squares of first N natural numbers
#Ans:-
def print_square(n):
    if n>0:
        print_square(n-1)
        print(n**2,end=" ")
print_square(5)
print()


#Q8. Write a recursive python function to print cubes of first N natural numbers
#Ans:-
def print_cubes(n):
    if n>0:
        print_cubes(n-1)
        print(n**3,end=" ")
print_cubes(5)
print()


#Q9. Write a recursive python function to print first N multiples of a given number.
#Ans:-
def multiples(n,number):
    if n>0:
        multiples(n-1,number)
        print(n*number,end=" ")
multiples(5,5)
print()


#Q10. Write a recursive python function to print a number in reverse order.
#Ans:-
def reverseNumber(number):
  if number%10!=0: #test case:- 4500
    x=str(number)[::-1]
    print(int(number))
  else:
      print(str(number)[::-1])
reverseNumber(50036)
reverseNumber(2649000)


