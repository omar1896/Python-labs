#!/usr/bin/env python3

""" ######################################## task 1 ########################################################################"""

# Get the user's first name and last name
# first_name = input("Enter your first name: ")
# last_name = input("Enter your last name: ")

# # Reverse the order of the first name and last name
# reversed_first_name = first_name[::-1]
# reversed_last_name = last_name[::-1]

# # Print the reversed name
# print("Your name in reverse order is:", reversed_last_name + " " + reversed_first_name)
""" ######################################## task 2 ########################################################################"""

# def function(x):
#   n=str(x) 
#   a=int(n) 
#   b=int(n+n)
#   c=int(n+n+n)
#   print(a+b+c)


# user_input=input("enter a number: ")
# function(user_input)

""" ######################################## task 3 ########################################################################"""


# print( """Sample string : 
# a string that you "don't" have to escape
# This
# is a ....... multi-line
# heredoc string --------> example""" )


""" ######################################## task 4 ########################################################################"""

# def volume_of_sphere(n):
#   result= 4/3 * 3.14 * pow(n, 3)
#   print(result)


# user_input=int(input("enter a number: "))
# volume_of_sphere(user_input)

""" ######################################## task 5 ########################################################################"""

# def area_triangle(base,height):
#     result=(base*height)/2
#     print(result)

# base=int(input("enter a base: "))
# height=int(input("enter a height: "))

# area_triangle(base,height)

""" ######################################## task 6 ########################################################################"""
# # Define the number of rows and columns
# rows = 7
# columns = 6

# # Create an empty list to store the pattern
# pattern = []

# # Iterate over the rows
# for row in range(rows):

#     # Iterate over the columns
#     for column in range(columns):

        # If the current row is less than or equal to the current column,
#         # then append a star to the pattern.
#         if row <= column:
#             pattern.append("*")
#         else:
#             pattern.append(" ")

#     # Append a newline character to the pattern.
#     pattern.append("\n")

# # Print the pattern.
# print("".join(pattern))

""" ######################################## task 7 ########################################################################"""

# user_input=str(input("enter a word: "))
# reversed_user_input = user_input[::-1]

# print(reversed_user_input)

""" ######################################## task 8 ########################################################################"""
 


# for i in range(6):
#     if i == 3 or i == 6:
#         continue
#     else:
#         print(i)

""" ######################################## task 9 ########################################################################"""
# def fibonacci(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fibonacci(n - 1) + fibonacci(n - 2)


# for i in range(51):
#     print(fibonacci(i))

""" ######################################## task 10 ########################################################################"""

# digits=0
# letters=0
# user_input=str(input("enter a word: "))
# for i in user_input:
#     if i.isdigit():
#       digits+=1 
#       print(i, end="\n")
#     else:
#       letters+=1 
#       print(i, end="\n")



# print(f' number of letters {letters} and digits {digits}')       
    
       

