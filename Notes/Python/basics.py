#!/usr/bin/python

#Print "hello world" in python
print("Hello world!")
#Don't have to include \n for a new line, however you can if you want
print("Hello again!\n")

#Look up how to save scalar values and then print them
a = 10
b = 20
print(f"The numbers we chose were {a} and {b}".format('a', 'b'))

#Another method of printing
name = "Tom"
age = 15
print("The name is %s and the age is %d"%(name,age))
# %s is a placeholder for when you want to print string values
# %d is a placeholder for when you want to print numeric values

#Multiple strings and numbers
name1 = "Casey"
name2 = "John"
age1 = 24
age2 = 21
print("The first person is %s and they are %d, the second person is %s and they are %d"%(name1,age1,name2,age2))
#You can have as many %s and %d as you want, just list the variables at the end in the right order

#Ask for input, then print the input
color = input("What is your favorite color? ")
print("Your favorite color is ", color)

favnum = input("What is your favorite number? ")
#print("Your favorite number is %d"%(favnum))
print("The datatype of the input given is ", type(favnum))
print("Your favorite number is %s"%(favnum))
#By default python expects string values as inputs, have to specify if you want to print it differently

height = int(input("What is your height? "))
print("Your height is %d"%(height))
