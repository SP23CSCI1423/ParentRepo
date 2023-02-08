#!/usr/bin/perl

#Scalars have only a single value
#Arrays can have multiple values

#Scalars use $
#Arrays use @

#Number array
@numbers = (1, 2, 3, 4, 5);
print("The number array is: @numbers\n");
#Printing a specific item in the array
print("The third item in the array is $numbers[2]\n");
#Arrays start at 0 so (1, 2, 3, 4, 5) ([0], [1], [2], [3], [4])

#Characters/words in an array
@groceries = ("Milk", "Eggs", "Bread", "Bananas", "Oreos");
print("Our grocery list is: @groceries\n");
print("The first and last items on our list are $groceries[0] and $groceries[4]\n");

#Combining words and numbers
@info = ("Kahlan", 25, "Blue");
print("First name: $info[0]\n");
print("Age: $info[1]\n");
print("Favorite color: $info[2]\n");

#Make two arrays, one listing 3 favorite foods, the other listing 3 favorite movies
