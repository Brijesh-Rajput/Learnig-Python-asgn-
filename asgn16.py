"""
-> tuple can store hetergeneous and as well as duplicate values like list
-> tuple is immutable unlike list
"""

#Q1. Write a python script to store multiple items in a single variable ( Items are “Java” ,“Python”, “SQL”, “C” ) using tuple
#Ans:-
t1=("Java","Python","SQL","C") #or t1="Java","Python","SQL","C"
#t1=()  --> Empty tuple  or t1=(10,) --> it is also a tuple
t2=tuple(["Java","Python","SQL","C"])
print(t1,t2,sep="\n")


#Q2. Write a python program to store only one item using tuple.
#Ans:-
t2=(23,)
print(t2,type(t2),sep="\n")


#Q3. Write a python program to reverse the tuple.
#Ans:-
t2=(23,"abc",True,3+5j,None,25.89)
print(t2[-1:-1*len(t2)-1:-1])
#1st method:- print(t2[::-1])
#wrong---> print(t2[-1:-len(t2):])
#wrong:- t2[-1:-1*(len(t2)-1):-1]   ==>   output:-(25.89, None, (3+5j), True)


#Q4. Write a python program to Swap two tuples in Python.
#Ans:-
t1=("tuple1",2,3,6,98,34)
t2="tuple2",76,38,94,62
t1,t2=(t2,t1)
#(t1,t2) --> this is tuple of tuple(like 2d array or 2d list)
print("Tuple1 is {} and Tuple2 is {}".format(t1,t2))


#Q5. Write a python program to check if all items in the tuple are the same.
#Ans:-
t1=tuple([eval(e) for e in input("Enter a tuple(can have heterogeneous and duplicate value also) separating it by comma").split(',')])
print("all items in tuple are same" if len(t1)==t1.count(t1[0]) else "all items in tuple are not same")


#Q6. Write a python program to divide the tuple into four variables. tuple1=(100, 200, 300, 400)
#Ans:- ---------> Nice Question
tuple1=(100,200,300,400)
a,b,c,d=tuple1[0],tuple1[1],tuple1[2],tuple1[3]  #or a,b,c,d=100,200,300,400
print(a,b,c,d)


#Q7. Write a python program to copy elements 4 and 5 from the following tuple into a new tuple. tuple1=(1,2,3,4,5,6)
#Ans:-
tuple1=(1,2,3,4,5,6)
tuple2=tuple([e for e in tuple1 if e==4 or e==5])
print(tuple2)


#Best Question --|
#Q8. Write a python program to Sort a tuple of tuples by the second item. tuple1 = (('a', 21),('b', 37),('c', 11), ('d',29))
#Ans:-  Q. How to do this Question in less number of line --> or is there any sort-cut or predefined methods ?
tuple1=(('a',21),('b',37),('c',11),('d',29))
#using insertion sort
l2=[]
for e in tuple1:
    i=len(l2)-1
    while i>=0:
         if e[1]<l2[i][1]:
             i -= 1
         else:
             break
    l2.insert(i+1,e)
    #print(l2)
sorted_tuple=tuple(l2)
print(sorted_tuple)


#Q9. Write a python program to print the value 20 from given nested tuple. tuple1 = ("Python", [10, 20, 30], (2, 4, 16))
#Ans:-
tuple1 = ("Python", [10, 20, 30], (2, 4, 16))
print(tuple1[1][1])


#Q10. Write a python program to change the first item (22) of a list within the following tuple to 222. tuple1 = (11, [22, 33], 44, 55)
#Ans:-
tuple1 = (11, [22, 33], 44, 55)
tuple1[1][0]=222
print(tuple1)


""" Extra
#Q9. Write a python program to print the value 20 from given nested tuple. tuple1 = ("Python", [10, 20, 30], (2, 4, 16))
#Ans:-
tuple1 = ("Python", [10, 20, 30], (2, 4, 16))
print((tuple1[1])[2])
print(tuple1[0],tuple1[1],tuple1[2])
"""