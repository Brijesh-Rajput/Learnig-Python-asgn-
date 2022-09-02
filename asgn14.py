#Q1. Write a Python script to create a list of first N natural numbers.
#Ans:-
l1=list(range(1,int(input("Enter a Number : "))+1)) #bydefault value of sep=1
#or
l2=[e+1 for e in range(0,int(input("Enter a Number : ")))]
print(l1)
print(l2)


#Q2. Write a Python script to create a list of first N odd natural numbers.
#Ans:-
l1=[2*e+1 for e in range(0,int(input("Enter a Number : ")))]
print(l1)


#Q3. Write a Python script to create a list of first N even natural numbers.
#Ans:-
l2=[2*e for e in range(1,int(input("Enter a Number : "))+1)]
print(l2)


#Q4. Write a Python script to find the greatest number in a given list of numbers.
#Ans:-
l1=eval(input("Enter a list of numbers by using a square bracket:- "))
print("Max Element is {}".format(max(l1)))


#Q5. Write a Python script to find the smallest number in a given list of numbers.
#Ans:-
l1=eval(input("Enter a list of numbers (by using a square bracket) :- ")) #list represents by square bracket
print("Min Element is {}".format(min(l1)))


#Q6. Write a Python script to calculate the sum of elements in a given list of numbers.
#Ans:-
l1=[int(e) for e in input("Enter a list of numbers separated by comma : ").split(',') ]
print(l1)
print("Sum of elements of a list is %d"%sum(l1))


#Q7. Write a Python script to remove all non int values from a list.
#Ans:-
l2=eval(input("Enter a list of hetergenous value : "))
l1=[e for e in l2 if type(e)==int]
print(l1)


#Q8. Write a Python script to print distinct elements along with their frequencies of occurrence in the list.
#Ans:-
l1=eval(input("Enter a list of heterogenous and as well some dupicate of it also : "))
l1=eval(input("Enter a list of heterogenous and as well some dupicate of it also : "))
l2=[]
for e in l1:
    if e not in l2:
       l2.append(e)
       print("Element is {} and frequencies of that element is {} ".format(e,l1.count(e))) #here, we can't use the %d as we don't know that the element is of which type ?
print()


#Q9. Write a Python script to print indices of all occurrences of a given element in a given list.
#Ans:-
#1st method ---> as usal we do in c language, traversing whole list
#2nd method:-
l1=eval(input("Enter a list :- "))
x=eval(input("Enter an element of a given list to know all the indices of given element in a list :- "))
count=l1.count(x)
startindex=0
while count: #instead of while loop we can use range
    index=l1.index(x,startindex)
    print(index,end=" ")
    startindex=index+1
    count-=1
print()


#Q10.  Write a python script to sort a list.
#Ans:-
l1=eval(input("Enter a list of similar types : "))
l1.sort()
print(l1)

"""
Extra:- Experiment 
l1=[2,37,48]
#print(l1.index(19)) #valueerror as 19 is not present in the list
print(l1.count(18)) #return 0
l1.index(value,startindex,endindex)
"""


""" MY WRONG ANSWER and my mistake 
Q8. 
l2=[e for e in l1 if l2.count(e)==0] #contains distinct elements
for e in l2:
    print("Element is :- ",e,"frequencies is :- ",l1.count(e))  #sep=" "  end=" "
Q9. try but wrong solution
l1=[2,37,48]
#print(l1.index(19)) #valueerror
print(l1.count(18))
======
l1=eval(input("Enter a list :- "))
x=eval(input("Enter an element of a given list to know all the indices of given element in a list :- "))
count=l1.count(x) #count() required as remove function throws an error if value is not present in the list
while count:
    print(l1.index(x),end=" ")
    l1.remove(x)
    count-=1
print()

"""