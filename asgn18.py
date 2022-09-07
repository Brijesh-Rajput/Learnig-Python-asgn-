"""
Q8 is interesting Question Acc. to me
--> dict is same as set
--> Difference is that, dict store key and value as an element(they are associate to each other)
"""

#Q1. Write a python program to create and print a dictionary which stores your information. (name, age, gender .....)
#Ans:-
d1={"name":"Brijesh","age":21,"gender":"Male","sem":5,"Branch":"CSE"}
print(d1)


#Q2. Write a python program to access the items of a dictionary by referring to its key name.
#Ans:-
d1={3:"Hello","My":56.9,2.4:25,5:78}
for k in d1:
    print(k,d1[k])
#or
for k,v in d1.items(): #d1.items() returns an object of dict_items class which contains list of each element of dictionary in tuple
    print(k,v)


#Q3. Write a python program to get a list of the values from a dictionary.
#Ans:-
d1={1:"Rahul",2:"Ritesh",3:"Brijesh"}
print(d1.values()) #print an object of dict_values class
print(list(d1.values())) #print list of values of a dictionary


#Q4. Write a python program to change the value of a specific item by referring to its key name.
#Ans:-
d1={1:"Rahul",2:"Ritesh",3:"Brijesh"}
d1[3]="Birju"
print(d1)


#Q5. Write a python program to print all key names in the dictionary, one by one.
#Ans:-
d1={1:"Rahul",2:"Ritesh",3:"Brijesh"}
for k in d1:
    print(k,end=" ")
print()
#or print(d1.keys())  But, it prints an object of dict_keys class which contains a list of all keys of this d1 dictionary


#Q6. Write a python program to create a dictionary that contains three dictionaries. (nested)
#Ans:-
d1={1:{1:"Ritesh",2:"Rahul",3:"Brijesh"},2:{1:"Mummy",2:"Papa",3:"Bhai"},3:{1:"Hello",2:"Everyone"}}
print(d1)
#or
for k,v in d1.items():
    print(k,v)
#or
for list_values in list(d1.values()):
    for k,v in list_values.items(): #don't forget to write .items() function b'coz list_values stores a dictionary
        print(k,v)
""" Wrong Answer
for v in d1.values():
    for k,v in d1.items():
        print(k,v)
print()
"""


#Q7. Write a python program to create three dictionaries, then create one dictionary that will contain the other three dictionaries.
#Ans:-
d1={123:"Noor",134:"Nisha",135:"Noori"}
d2={132:"Mahesh",47:"Sumit",356:"Saurabh"}
d3={24:"Harish",123:"Gunjesh",456:"kartikeya"}
d={} #empty dictionary
d[1]=d1
d[2]=d2
d[3]=d3
print(d)


#Q8.  Write a python program to convert two lists into a dictionary in a way that item from list1 is the key and item from list2 is the value.
#Ans:-
l1=[1,2,3]
l2=["Rahul","Ritesh","Brijesh"]
#Note :- length of both list must be same and all elements of l1 list must be distinct as key must be unique in dict
d1={}
x=len(l1)
while x:
    d1[l1[x-1]]=l2[x-1]  #assuming that sequence will not be matter in dictionary
    x-=1
print(d1)
"""
#or
{ key:value for (key,value) in zip(l1,l2) } #copied from gfg to do precise coding
"""


#Q9. Write a python program to merge two python dictionaries into one dictionary.
#Ans:-
d1={1:"Raju",2:"Mahesh",3:"Birju"}
d2={4:"Kalu",5:"Ramu"}
for key in d2.keys():
    d1[key]=d2[key]  #if key is already present in the d1 then value of that key will update in dictionary d1
print(d1)


#Q10. Write a python program to get the key of lowest value from the dictionary. sample_dict = { 'C': 92, 'Java': 66, 'Python': 85 }
#Ans:-
sample_dict = { 'C': 92, 'Java': 66, 'Python': 85 }
#brut force
lowest_value=min(sample_dict.values())
for key in sample_dict.keys():
    if sample_dict[key]==lowest_value:
        print(key,lowest_value)
        break
print()


"""
Question 8 
Wrong Code/answer 
for key in l1:
    for value in l2:
        d1[key]=value
print(d1)
"""