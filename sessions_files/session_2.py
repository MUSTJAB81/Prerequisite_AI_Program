# -*- coding: utf-8 -*-
"""Session_2.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1FjSC8gJuLR1SB9Xj-6XcOXwV9OHwCmkV
"""

# Data Type
# Variables

# Type casting
num : int = 10

num

# Python allows Type Casting But not inforce it
num = "Mustjab"

num

name : str = "Mustjab"

name

# Type Conversion
int("10")

num = 10
str(num)

type(num)

num_int = 20
num_str = str(num_int)

type(num_str)

type(num_int)

bool(0)

bool(1)

float(0)

"""
The bool() function returns False for empty values like "" (empty string), 0, None, False, [] (empty list), etc.
Any non-empty string is considered True.
Since "Hyder" is a non-empty string, bool("Hyder") returns True."""

bool("Hyder")

bool(-1)

bool(1-1)

# ValueError: invalid literal for int() with base 10: 'Mustjab'
#int("Mustjab")

# ZeroDivisionError: division by zero
#int(10/0)

# ValueError: invalid literal for int() with base 10: '0.0'
#int("0.0")

int("200")

# convert in integer
int(0.0)

str('0.0')

float , int , complex , str , bool

"""## **Variables**"""

#dont start with keywords
#list = [1,2,3,4]

num = 10
name = "Mustjab"

print("This is Second Class.")

print("This is Second Class. My name is Mustjab. Total strength = 10. ")

"""## **String Formating**"""

# using variables in above text (dynamic code)

print(f"This is Second Class. My name is {name}. Total strength = {num}. ")

# second method of formating without 'f' using .format()
print("This is Second Class. My name is {}. Total strength = {}.".format(name,num))

# must use sequence of variable if change result will also change
print("This is Second Class. My name is {}. Total strength = {}.".format(num,name))

# using index. indexing starts with 0
print("This is Second Class. My name is {1}. Total strength = {0}.".format(num,name))

# using placeholder
print("This is Second Class. My name is {name}. Total strength = {num}.".format(num = num,name = name))

"""## User Define **Variable**"""

num = 10
name = "Mustjab"
print("This is Second Class. My name is {1}. Total strength = {0}.".format(num,name))

name = input("Enter Your Name : ")
num = 10
print("This is Second Class. My name is {1}. Total strength of class = {0}.".format(num,name))

name = input("Enter Your Name : ")
num = input("Enter Your Class Strength : ")
print("This is Second Class. My name is {1}. Total strength of class = {0}.".format(num,name))

# Task : Take three inpits from user and print in indexin format
name = input("Enter Your Name : ")
age = input("Enter Your Age : ")
num = input("Enter Your Hight in feet : ")
print("My Name is {0}. My age is {1}. My hight is {2} feet.".format(name,age,num))

# All Input values by input is string
type(num)

# concatination
name = 'Aqsa'
print("My name is " + name)

name = 'Aqsa'
print("My name is " , name)

# Str and int cant be concat
#age = 34
#print("My age is " + age)

age = input("Enter Your Age : ")
print("My age is " + age)

# Using Type conversion
age_ = 35
print("My age is " + str(age_))

# Without Type Conversion and concatenating
age_ = 35
print("My age is ", age)

age = int(input("Enter Your Age : "))
print("My age is " + str(age))

# using coma in format funcation its seprate the values of variables
name = input("Enter Your Name : ")
age = input("Enter Your Age : ")
num = int(input("Enter Your Hight in feet : "))
print("My Name is {0}. My age is {1}. My hight is {2} feet.".format(name,age,num))

