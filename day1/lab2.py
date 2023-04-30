#!/usr/bin/env python3
""" ######################################## task 1 ########################################################################"""
# def sort_list(list):
#   print(set(list))


# sort_list([5,4,2,1,6,6,5,5]) 
""" ######################################## task 2 ########################################################################"""
# def modify_2strings(x,y):
#   x=str(x)
#   y=str(y)
#   len_str1=len(x)
#   len_str2=len(y)
#   first_half, second_half = x[:len_str1 // 2], x[len_str1 // 2:]
#   first_half_str2, second_half_str2 = y[:len_str2 // 2], y[len_str2 // 2:]

#   final_string=(first_half+first_half_str2)+(second_half+second_half_str2)

#   print(final_string)
  


# user_input1=str(input("enter a word "))
# user_input2=str(input("enter a word "))
# modify_2strings(user_input1,user_input2)

""" ######################################## task 3 ########################################################################"""
# def check_function(*args):
#     print(args)
#     array=[]
#     array=args
#     len1=len(array)
#     print(len(array))
#     newarray=set(array)
#     len2=len(newarray)
#     print(len(newarray))
#     if len1==len2:
#         print("numbers are unique")
#     else:
#         print("numbers are diff")
        


# check_function(1,2,3,4,4,3,2,1)

""" ######################################## task 4 ########################################################################"""
# def bubble_sort(list):

  

#   n = len(list)
#   for i in range(n):
#     for j in range(n - i - 1):
#       if list[j] > list[j + 1]:
#         list[j], list[j + 1] = list[j + 1], list[j]

#   return list

# list1=[5,4,7,8,6,5]
# orderd=bubble_sort(list1)
# print(orderd)

""" ######################################## task 5 ########################################################################"""
# import random

# def guess_game():
#   guesses=[]
      

#   """
#   A guessing game that generates a random number and gives the user 10 tries to guess it.

#   Returns:
#     True if the user guessed the number correctly, False otherwise.
#   """

#   # Generate a random number between 1 and 100.
#   number = random.randint(1, 100)
 

#   # Initialize the number of tries.
#   tries = 10

#   # Loop until the user has guessed the number or run out of tries.
#   while tries > 0:

   
#     # Get the user's guess.
  
#     guess = int(input("Guess a number between 1 and 100: "))
  

#     # Check if the user guessed the number correctly.
#     if guess == number:
#       print("Congratulations! You guessed the number correctly!")
#       return True

#     # Check if the user's guess is out of range.
#     elif guess < 1 or guess > 100:
#       print("Your guess is out of range. Please try again.")
#       tries -= 1
#       continue

#     # Check if the user has guessed the number before.
#     elif guess in guesses:
#       print("You have already guessed that number. Please try again.")
#       tries -= 1
#       continue

#     # If the user's guess is not correct, display a hint message.
#     if guess > number:
#       print("Your guess is too high.")
#     else:
#       print("Your guess is too low.")
#     tries -= 1
#     pass
#     guesses.append(guess)
#     print(guesses)


#   # If the user has run out of tries, display a message and ask them if they want to play again.
#   if tries == 0:
#     print("You have run out of tries.")
#     play_again = input("Do you want to play again? (Y/N) ")
#     if play_again.lower() == "y":
#       return guess_game()
#     else:
#       return False


# guess_game()