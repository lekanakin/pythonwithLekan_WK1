'''
This package called 'Platformio-ide-terminal' is required to have a terminal in Atom text editor

Let's start with DATA TYPES

#Variable
#Variables are containers where you can store data in. It keep your code more organized

# greetings = input("What is your name?")
# print("Welcome",greetings)

#Numbers
# #This refers to integers and floats
# a = 3
# b = 3.2
# print("Welcome, I will add 50 to your age")
# age = input("What is your age?")
# print("Your new age is",int(age)+50)

#Operators
#This refers to mathematical processes such as addition, subtraction, multiplication, mathematical

#Strings
#This refers to text. Strings have methods attached to them. use dir(string) to see all the methods attached to them. You can use help(c.replace) function to check what is possible with any method.
#string must always be quoted
#Python attaches nmbers to all string
# c = "Lekan"
# print(c.replace("e","r"))
# c[1] #to get the value in position 1. Python starts from 0
# #Spliting is upper bound exclusive
# c[0:2] #will select first 2
# #You can also split from the back using -
# c[-2:]


#List
#List can accomodte various data Types
# c = ["Two",2]
#strings have methods use dir(list)

#Tuple are similar to list. However they are not mutable, you can not remove vlues from them.
#They may contain different data Types
#t = ("Lekan",5)

#dictionary. You need a {} to create a dictionary. A dictionary has a key, value
# d = {"Name":"Lekan", "Surname":"Akin"}
# print(d["Name"])

#Functions
#Functions are used to keep your code organized.They are procedures/blueprints. They have inputs defined as arguments. Just like built in functions, they are able to perform intructions.
#to build functions you start with the def key word
#you return the output of functions with key word return
#you can call the instance of the function for them to work
# def currency_converter(money,rate):
#     value = int(money) * int(rate)
#     return value
#
# print("This will convert dollar to naira at any given rate")
# dollar = input("How much do you want to convert?")
# rate = input("What is the rate?")
# theValue = currency_converter(dollar,rate)
# print("The value of your money is",theValue)


# Conditional
#x > y                # x is greater than y
##x < y                # x is less than y
#x >= y               # x is greater than or equal to y
#x <= y               # x is less than or equal to y
#This perform an action based on a given instruction

# age = input("How old are you?")
# age =int(age)
# if age < 12:
#     print("Hey, you are a Kid")
# elif 12 < age < 20:
#     print("Hey, you are a Teenager")
# else:
#     print("You are an adult")


##LOOPS
#For Loop and While Loop
#FOR loop goes through items in a list.

# emails = ['ola@dsn.com','james@gmail.com', 'ben@gmail.com']
#
# for email in emails:
#     if 'gmail' in email:
#         print(email)


#While LOOPS
#This carries out an action as far as a condition is fulfilled
#This is usually used in common authentication logic

# password = ''
# while password != 'lekan123':
#     password = input("Please type a password: ")
#     if password == 'lekan123':
#         print("You are now logged in")
#     else:
#         print("Please try again")


# names = ['lekan','joshua','tola']
# surname = ['Akin','Baba','seun']
#
# for i,j in zip(names,surname):
#     print(i,j)

#Open files in Python
#file = open('name of file', 'r')
#content = file.read()
#print content
#file.seek(0) to go back to first line
#content = file.readline()
#content = [i.rstrip("\n") for i in content]
#print(content)

#Create new files
#file = open("exa.txt",'w')
#file.write("Line 1")
#file.close()

# names = ['Sola','Bola', 'Tola']
# file = open("ta.txt",'w')
# for item in names:
#     file.write(item+'\n')
# file.close()
#
# file = open("ta.txt",'a')
# file.write("Segun")
# file.close()

# r - Open for reading
# r+ - open for reading and writing
# w - Open file for writing
# w+ open file for writing and reading
# a open file for appending
# a+ open file for appending and reading

#Text Generator app
# my approach to programming is to think of smalller pieces first and then see the big stuff ready.
'''
import string
help(string)

String module has ascii_letters.
dir() function can help to see all the methods of a module

import random
Use the help( function to read all about this module)
This has different functions. We are interested in using the choice function

random.choice("Joshua")
random.choice(string.ascii_lowercase)

'''
'''
import random
import strings

def generators():
    letter1=random.choice(string.ascii_lowercase)
    letter2=random.choice(string.ascii_lowercase)
    letter3=random.choice(string.ascii_lowercase)
    name = letter1+letter2+letter3
    return(name)

print(generators())
'''

import random
import string

vowel = 'aeiou'
consonants = 'bcdfghjklmnpqrstvwxyz'
letters = random.choice(string.ascii_lowercase)
print("Welcome to the ultimate 3 letter word generator")
letter1= input("What letter do you want: Type 'v' for vowel, 'c' for consonant, 'l' for any: ")
letter2= input("What letter do you want: Type 'v' for vowel, 'c' for consonant, 'l' for any: ")
letter3= input("What letter do you want: Type 'v' for vowel, 'c' for consonant, 'l' for any: ")

def generator():
    if letter1 == 'v':
        letter10 = random.choice(vowel)
    elif letter1 == 'c':
        letter10 = random.choice(consonants)
    elif letter1 == 'l':
        letter10 = letters
    else:
        letter10 = letter1

    if letter2 == 'v':
        letter20 = random.choice(vowel)
    elif letter2 == 'c':
        letter20 = random.choice(consonants)
    elif letter2 == 'l':
        letter20 = letters
    else:
        letter20 = letter2

    if letter3 == 'v':
        letter30 = random.choice(vowel)
    elif letter3 == 'c':
        letter30 = random.choice(consonants)
    elif letter3 == 'l':
        letter30 = letters
    else:
        letter30 = letter3

    name = letter10+letter20+letter30

    return(name)

for i in range(10):
    print(generator())
