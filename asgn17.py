"""
set stores heterogeneous element but it should be hasable object only. set can't store duplicates value.
set doesn't store elements in oredered way or in sequence.
e.g:- set will contain unhasabhle elements like list.
s1=set() ---> for empty set
s1={}  ---> it's a dict. Not a set
"""

#Q1. Write a python program to store all the programming languages known to you using Set.
#Ans:-
s1={"C","C++","Python","Java","JS","Kotlin","Swift","Flutter"}
print(s1)


#Q2. Write a python program to store your own information {name, age, gender, so on..}
#Ans:-
myInfo={"Brijesh",20,"Male","Pursuing B.Tech"}
myInfo.update(["now in 5th sem","GEC Patan clg"])   #myInfo.add(["GEC Patan clg"]) --> error b'coz list is unhasable. so it can't be add to the set
print(myInfo)


#Q3. Write a python script to get the data type of a Set.
s1={2,3.5,3+5j,True,"MySir",(19,'a'),range(3,8,2)}  #list will not be an element of a set
print(s1,"Type of s1 object is ",type(s1))  #b'coz, in python everythings are in object


#Q4. Write a Python script to find if “Python” is present in the set thisset = {"Java", "Python", "Django"}
#Ans:-
thisset = {"Java", "Python", "Django"}
print("yes,'Python' is present in the set" if "Python" in thisset else "No,set doesn't contain 'Python'")
#or
s1={"Python"}
print("yes,'Python' is present in the set" if s1.issubset(thisset) else "No,set doesn't contain 'Python'")  #instead of issubset() function, you can use issuperset() function also


#Q5. Write a python program to add items from another set to the current set. thisset = {"Java", "Python", "SQL"}  secondset= {"C", "Cpp", "NoSQL"}
#Ans:-
#as we know that, concatenation operator and as well as repetetion operator doesn't work on set. AND set contains only distinct element NOT duplicate value
thisset = {"Java", "Python", "SQL"}
secondset= {"C", "Cpp", "NoSQL"}
print(thisset.union(secondset))


#Q6. Write a python program to add elements of list to a set. thisset = {"Python", "Django", "JavaScript"}  mylist = ["Java", "C"]
#Ans:-
thisset = {"Python", "Django", "JavaScript"}
mylist = ["Java", "C"]
print(thisset.union(set(mylist)))


#Q7.Write a python program to remove last item of the given set. thisset = {"Python", "Django", "JavaScript", “SQL”}
#Ans:-
thisset = {"Python", "Django", "JavaScript", "SQL"}
#we can delete "SQL" by two ways :- 1. using discard() method   2. using remove() function
#difference is that, if element is not present in the set and we try to remove it by using remove function then it will give an error whereas discard() function doesn't gives an error
thisset.remove("SQL")  #As we already know that, "SQL" is present in the set. Therefore, here i have used remove instead of discard() function

#Q8. Write a python program to delete the set completely.
#Ans:-
thisset = {"Python", "Django", "JavaScript", "SQL"}
thisset.clear()
print(thisset)


#Q9. Write a python program to loop through the set and print values. thisset = {"Python", "Django", "JavaScript", “SQL”}
#Ans:-
thisset = {"Python", "Django", "JavaScript", "SQL"}
for e in thisset:
    print(e,end=" ")
print()


#Q10. Write a python program to find the maximum and minimum value in a set.
#Ans:-
thisset={23,45,87,70,95,27,39,40}
print("Maximum value in the set is ",max(thisset))
print("Minimum value in the set is",min(thisset))