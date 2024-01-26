# Assignment 5:
# Do the exercise 1-15 in https://pynative.com/python-basic-exercise-for-beginners/
# Try do challenge yourself by not checking the "solution"

# Exercise 10:
# Create a new list from two list using the following condition
# Given two list of numbers, write a program to create a new list such that the new list should contain odd
# numbers from the first list and even numbers from the second list.

# assign list 1 and list 2
list_1 = [10, 20, 25, 30, 35]
list_2 = [40, 45, 60, 75, 90]

result_list = []

# loop and iterate for odd numbers 
for num in list_1:
    if num % 2 != 0:
        result_list.append(num)
        
# loop and iterate for even numbers 
for num in list_2:
    if num % 2 == 0:
        result_list.append(num)

print("Result list:", result_list)
