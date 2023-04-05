#!/usr/bin/python

#While loops
count = 0
while count < 5:
	count = count + 1
	print("The current count is %d" %(count))

count1 = 0
while (count1 < 5):
	count1 = count1 + 1
	print("the current count is %d" %(count1))
#While you don't need the parenthesis, I recommend using them

#While loop with an else statement
countdown = 10
while (countdown > 0):
	print("Countdown: %d" %(countdown))
	countdown = countdown - 1
else:
	print("Blast off!")

#For loops
for i in range(0, 5):
	print("We are counting with a for loop, the value is %d" %(i))
#print the values of i starting at 0 and the last number printed will be 4

#Lists
#Lists in python are what arrays were in perl
list = ["This", "is", "a", "list"]
#Indexing works the same, start at 0
length = len(list)
print("The length of our list is %d" %(length))

#Printing a list using a for loop
for x in list:
	print(x)

#A couple of functions for lists
list.append("NewValue")
for x in list:
	print(x)
#append adds to the end of the list
list.pop(3)
for x in list:
	print(x)
#pop will remove what is in the specified index

#Use a if else statement, ask the user if they like cats, if they say yes print something about cats
answer = input("Do you like cats?")
if (answer == "yes"):
	print("Cool, cats don't actually have 9 lives")
else:
	print("Oh, ok")
#variablename.upper changes to all uppercase, variablename.lower changes to all lowercase
answer1 = input("Do you like dogs?")
answer1 = answer1.lower()
if (answer1 == "yes"):
	print("Cool, dogs truly are man's best friend")
else:
	print(":(")

#In perl we said elsif, in python we elif
number = int(input("Pick a number between 1 and 5 "))
if (number == 1):
	print("1 is an odd number")
elif (number == 3):
	print("3 is an odd number")
elif (number == 5):
	print("5 is an odd number")
else:
	print("You picked an even number")

