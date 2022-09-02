#Q1. Write a python script to store multiple items in a single variable ( Items are “Java”,“Python”, “SQL”, “C” ) using list
#Ans:-
#1st Method:-
l1=[]
l1.append("Java")
l1.append("Python")
l1.append("SQL")
l1.append("C")
print(l1)
#2nd Method:-
l1=list(["java","python","SQL","C"])
print(l1)
#3rd Method:-
l1=eval("['java','python','SQ','C']")
print(l1)
#4th method:-
#-------------------> Error  =====>       l1=list("java","Python","SQL","C")   ---> atmost one argument and that should be an iterable object


#Q2. Write a python script to get the data type of a list.
#Ans:-
l1=[]  #or l1=[1,"1bc",3+5j,True]
print(type(l1))


#Q3. Write a python script to get the last item of the list ( mylist = ["Java", "C", "Python"])
#Ans:-
mylist=["Java","C","Python"]
print(mylist[-1])


""" Q. How to access the elements of a list ?
mylist=["Java","C","Python"]
#1st Method:-
for e in mylist:
    print(e,end=" ")
#2ndMethod:-
i=0
while i<len(mylist):
    print(mylist[i],end=" ")
#2rd Method:-
print(mylist)
"""

#Q4. Write a python script to Change the values "SQL" and "Reactnative" with the values "NoSQL" and "Flutter" (List is thislist = ["Java", "SQL", "C", "Reactnative", "Javascript", "Python"]
#Ans:-
l1 = ["Java", "SQL", "C", "Reactnative", "Javascript", "Python"]
l2=[]
for e in l1:
    if e=="SQL":
        l2.append("NoSQL")
    elif e=="Reactnative":
        l2.append("Flutter")
    else:
        l2.append(e)
print(l2)


#Q5. Write a python script to add an item to the end of the list (item “Python”. (mylist = ["Java", "SQL", "C", "Reactnative"])
#Ans:-
mylist=["Java","SQL","C","Reactnative"]
mylist.append("Python")  #or mylist.insert(100,"Python")
print(mylist)

#Q6. Write a python program to append elements from another list to the current list.( firstlist = ["Java", "Python", "SQL"] secondlist = ["C", "Cpp", "NoSQL"] )
#Ans:-
firstlist = ["Java", "Python", "SQL"]
secondlist = ["C", "Cpp", "NoSQL"]
for e in secondlist:
    firstlist.append(e)
print(firstlist)
#or for e in firstlist: print(e,end=" ")


#Q7. Write a python program to Print all items by referring to their index number (thislist = ["Java", "SQL", "C", "Reactnative", "Javascript", "Python"]
#Ans:-
thislist = ["Java", "SQL", "C", "Reactnative", "Javascript", "Python"]
i=0
while i<len(thislist):
    print(thislist[i],end=" ")
    i+=1   #Don't forget to increment this
print()


#Q8. Write a python program to sort the list alphanumerically – thislist = ["Java", "SQL", "C", "Reactjs", "Javascript", "Python"]
#ans:-
thislist = ["Java", "SQL", "C", "Reactjs", "Javascript", "Python"]
l2=sorted(thislist) #or thislist.sort()
print(l2)


#Q9.  Write a Python script to create a list of city names taken from the user.
#Ans:-
x=int(input("How many Number of city names you will enter ? "))
#user can enter one by one as in c language using for loop ---> as usual method  --> requires to ask the user that how many numbers of city names he will enter
#user can enter city names by using comma ---> we have learn split and join function in string class
#user can enter directly list  ---> for this we will use eval function --> Here we don't want to ask the user that how many no. of city names he will print
print("Enter {} city names in a list :- ".format(x))      #or "enter %d city names"%x
l2=eval(input())
print(l2)


#Q10. Write a Python script to create a list, where each element of the list is a digit of a given number
#Ans:-  #let number is 386 --> output want:- [3,8,6]
l1=list(input("Enter a Number : "))  #output:- ["3","8","6"]
l2=[int(e) for e in (input("Enter a Number : "))] #list comprehensive is used here
print(l2)

