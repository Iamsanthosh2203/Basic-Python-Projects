'''This is the basic project of python
Which I learned from FreeCodeOrg !!!

Project 1 -MadLibsGenerator'''

#different types of string concatination
user_name =input("Enter Your Name ")#getting input from user

print("Hello "+user_name) #type1
print("Hello {}".format(user_name)) #type2
print(f"Hello {user_name}")#type3

#i am going to use type3 for this MadLibsGenerator

profession=input("Enter your profession")
age = input("Your Age Please!!!")
dob=input("Whad is your DOB?")
hoobie=input("Your hoobies?")
school=input("Your school name?")

print(f"Hi my name is {user_name}.I am {profession}.I am {age} years old.I was born in {dob}.I like {hoobie}.I finished my schooling at {school}.")
