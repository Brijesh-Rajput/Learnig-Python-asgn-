#Q1. Write a python script to create a String in 3 different possible ways
#Ans:-
s1="My 1st String"  #or  s1="""My 1st String"""  or s1='''My 1st string''' or s1='My 1st string'
s2=str() #empty string
s3=str("My 2nd string")
s4=str("""Hello,
        How are you ?
        """)
print(s1,s2,s3,s4,sep="\n")


#Q2. Write a python script to Get the characters from the start to position 5 (Given String “iNeuron” using the slice syntax)
#Ans:-
s1="iNeuron"
print(s1[:6:1]) #by default start=0 inclusively
#print(s1[0::1]) #by default end=last index inclusively that character will also print
#print(s1[::-1]) #to reverse a string


#Q3. Write a python script to Get the characters from position 2 to position 5 (Given String “Hello Learners” using the slice syntax)
#Ans:-
s1="Hello Learners"
print(s1[2:6:]) #as bydefault sep=1


#Q4. Write a python script to demonstrate String Concatenation adding space in between ( Given Strings a=”Learning” b=”Python” )
#Ans:-
a="Learning"
b="Python"
print(a+" "+b)


#Q5. Write a python script to get the count of total number of characters in String a=“iNeuron”
#Ans:-
a="iNeuron"
print("Total no. of characters in a given staring {}".format(a),len(a)) #don't write here count()  function instead of length function --> len() is an in-built functions


#Q6. Write a python script to reverse a String. (“iNeuron”)
#Ans:-
s1='iNeuron'
print("Reverse of a given string {} is {}".format(s1,s1[::-1]))


#Q7. Write a python script to determine whether a string contains a specific substring.
#Ans:-
string=input("enter a string :- ")
substring=input('Enter a substring to check whether it is present in the string or not ?')
print("Present in a string" if substring in string else "Not present in the string")


#Q8. Write a python script to check if a string contains only numbers.
#Ans:-
string=input("Enter a string to check whether it contains only a numbers or not")
print("string contains only digits" if string.isdigit() else "string contains other than number also")


#Q9. Write a python script to check if a string contains only characters of the alphabet.
#Ans:-
string=input('''Enter a String to check whether a string contains only alphabet or not :- ''')
print("Contains only alphabet" if string.isalpha() else "Contains other than charachters also")


#Q10. Write a python script to convert an integer to a string
#Ans:-
x=int(input("Enter an integer : "))
print("converted integer into a string is {}".format(str(x)))
#or
print("converted integer into a string is \"",str(x),"\"",sep="") #me:- Not good way
