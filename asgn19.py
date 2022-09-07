#Q1. Write a python program to create a simple function which prints “MySirG” .
#Ans:-
def prints():
    print("MySirG")
prints()


#Q2. Write a python program to create a function which expects two arguments and print them in the function body.
#Ans:-
def fun1(a,b):
    print(a,b)
fun1(20,59)


#Q3. Write a python program to create a function which expects an unknown number of arguments.
#Ans:-
def fun2(*t):
    for v in t:
        print(v,end=" ")
    print()
fun2(10,20,30,40)
fun2(20,89,76)
fun2(15,89,7,14,169,17)


#Q4. Write a python program to create a function which expects kwargs arguments.
#Ans:-
#kwargs full form is keyword arguments
def fun1(a,b,c):
    print(a,b,c)
fun1(15,c=67,b=23)


#Q5. Write a python program to create a function which expects a list as an argument.
#Ans:- #NOTE:-
#Question:- is there any method or not ?
def fun1(l1):
    print(l1)
fun1([15,78,49,76,34])


#Q6. Write a python program to create a function that finds a maximum of four numbers.
#Ans:-
def max_(a,b,c,d):
    l1=[a,b,c,d]
    print(max(l1))
max_(15,89,76,14)


#Q7. Write a python program to sum all the numbers in a list.
#Ans:-
def fun(l1):
    print(sum(l1))
fun([48,79,15,23,14,16,24,31])


#Q8. Write a python program to multiply all the numbers in a list.
#Ans:-
def fun(l1):
    mul=1
    for x in l1:
        mul*=x
    print(mul)
fun([48,79,15,23,14,16,24,31])


#Q9. Write a python program to create a function to check whether a number falls in a given range.
#Ans:-
def fun1(a,beg,end):
    if beg<=a<=end:
        return 1
    return -1
fun1(12,2,49)


#Q10. Write a python program to create a function to check whether a given number is even or odd.
#Ans:-
def iseven(a):
    if a%2:
        return 0
    else:
        return 1
print(iseven(8))





















