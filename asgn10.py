#Q1. Write a python script to print MySirG N times on the screen
#Ans:-
for x in range(int(input("Enter a Number : "))):  # bydefault beg=0 and sep=1 when one argument is pass to the range
    print("MySirG", end=" ")
print()


#Q2. Write a python script to print first N natural numbers
#Ans:-
for x in range(int(input("Enter a Number : "))):
    print(x + 1, end=" ")
print()


#Q3. Write a python script to print first N natural numbers in reverse order
#Ans:-
for x in range(int(input("Enter a Number : ")), 0, -1):
    print(x, end=" ")
print()
""" Try to find out another method     
Q. is there any method by which we can solve this problem ? But condition is that we will take input directly in range parenthesis(only one argument in range) ==> if 2 argument in range then we can do easily. see the code in same asgn
range(10) ----> 1,2,3,4,5,6,7,8,9,10
                10,9,8,7,6,5,4,3,2,1
"""


#Q4. Write a python script to print first N odd natural numbers
#Ans:-
for x in range(int(input("Enter a Number : "))): #Note here output
    print(2 * x + 1, end=" ")
print()


#Q5. Write a python script to print first N odd natural numbers in reverse order
#Ans:-
n = int(input("Enter a Number : "))
for x in range(n):
    print((n - 1) * 2 + 1 - 2 * x, end=" ")
print()
"""
OR
for i in range(int(input("Enter a Number : )),0,-1):
    print(2*i-1,end=" ")
"""
"""NOTE:-
# for printing some sequence of numbers. But not in reverse order then we can do easily by writing input stmt inside range function
# But if we want to print same sequence of number in reverse order then we must have to write input stmt outside the range function.{we can't do by only one argument in range function that is input() stmt}
# we can't write it(input stmt) inside a range function b'coz we want to know the last number from which it will print in reverse order
# That's Why
"""


#Q6. Write a python script to print first N even natural numbers
#Ans:-
for x in range(int(input("Enter a Number : "))):
    print(x * 2 + 2, end=" ")
print()
'''
Or
for x in range(int(input("Enter a Number : ")) + 1):
    print(x * 2, end=" ")
'''


#Q7. Write a python script to print first N even natural numbers in reverse order
#Ans:-
n = int(input("Enter a Number : "))
for x in range(n):
    print(2 * n - 2 * x, end=" ")
print()
'''
OR
for i in range(int(input("Enter a Number : )),0,-1):
    print(2*i,end=" ")
'''


#Q8. Write a python script to print squares of first N natural numbers
#Ans:-
for x in range(int(input("Enter a Number : "))):
    print((x + 1)**2, end=" ")
print()


#Q9. Write a python script to print cubes of first N natural numbers
#Ans:-
for x in range(int(input("Enter a Number : "))):
    print((x + 1)**3, end=" ")
print()


#Q10. Write a python script to print first 10 multiples of N
#Ans:-
n=int(input("Enter a Number : "))
for i in range(10):
    print("%d * %d = %d"%(n,i+1,n*(i+1)))
print()
