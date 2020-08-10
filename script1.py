#######################################
# number = input('Please type an integer: ')
# try:
#     print(int(number))
# except ValueError:
#     print('Please input an integer')
#######################################

#######################################
# answer = input("Type a number ")
# try:
#     int(answer)
#     print(answer)
# except:
#     print("Please type an integer")
#######################################

#######################################
# strings = "It was a bright cold day in April, and the clocks were striking thirteen."
# print(strings.find(","))
# print(strings[0: 33])
#######################################

#######################################
# a = "A screaming comes across the sky"
# rep = a.replace('s', '$')
# print(rep)
#######################################

#######################################
# shows = ["The Walking Dead", "Entourage",
#          "The Sopranos", "The Vampire Diaries"]
# index = 0
#######################################

#######################################
# for show in shows:
#     print(index, show)
#     index += 1
#######################################

#######################################
# qs = ['what is your name?', 'what is your color?', 'what is your quest?']
# n = 0
# while True:
#     print("Type q to quit")
#     a = input(qs[n])
#     if a == 'q':
#         break
#     n = (n + 1) % 3
#######################################

#######################################
# numbers = [11, 32, 33, 15, 1]

# while True:
#     answer = input("Guess a number or type q to quit.")
#     if answer == 'q':
#         break
#     try:
#         answer = int(answer)
#     except ValueError:
#         print("please type a number or q to quit.")
#     if answer in numbers:
#         print("You guessed correctly!")
#     else:
#         print("You guessed incorrectly")
#######################################

#######################################
# new_list = []
# for i in [8, 19, 4]:
#     for j in [9, 1, 33]:
#         new_list.append(i*j)
# print(new_list)
#######################################

#######################################
# cubed.py
# def by_three(num):
#     return num * num * num
# myscript.py
# import cubed
# print(cubed.by_three(3))
#######################################

#######################################
# import csv

# movies = [["Top Gun", "Risky Business", "Minority Report"], ["Titanic",
#                                                              "The Revenant", "Inception"], ["Training Day", "Man on Fire", "Flight"]]

# with open("movies.csv", "w") as csvfile:
#     spamwriter = csv.writer(csvfile, delimiter=",")
#     for movie_list in movies:
#         spamwriter.writerow(movie_list)
#######################################

#######################################
# Hangman Games
# import random


# def hangman():
#     word_list = ["Python", "Java", "computer", "hacker", "painter"]
#     random_number = random.randint(0, 4)
#     word = word_list[random_number]
#     wrong_guesses = 0
#     stages = ["", "________      ", "|      |      ",
#               "|      0      ", "|     /|\     ", "|     / \     ", "|"]
#     remaining_letters = list(word)
#     letter_board = ["__"] * len(word)
#     win = False
#     print('Welcome to Hangman')
#     while wrong_guesses < len(stages) - 1:
#         print('\n')
#         guess = input("Guess a letter ")
#         if guess in remaining_letters:
#             character_index = remaining_letters.index(guess)
#             letter_board[character_index] = guess
#             remaining_letters[character_index] = '$'
#         else:
#             wrong_guesses += 1
#         print((' '.join(letter_board)))
#         print('\n'.join(stages[0: wrong_guesses + 1]))
#         if '__' not in letter_board:
#             print('You win! The word was:')
#             print(' '.join(letter_board))
#             win = True
#             break
#     if not win:
#         print('\n'.join(stages[0: wrong_guesses]))
#         print('You lose! The words was {}'.format(word))


# hangman()
#######################################

#######################################
# class Rectangle():
#     def __init__(self, width, length):
#         self.width = width
#         self.length = length

#     def calculate_perimeter(self):
#         return self.width * 2 + self.length * 2


# class Square():
#     def __init__(self, s1):
#         self.s1 = s1

#     def calculate_perimeter(self):
#         return self.s1 * 4
#######################################

#######################################
# class Square():
#     def __init__(self, s1):
#         self.s1 = s1

#     def calculate_perimeter(self):
#         return self.s1 * 4

#     def change_size(self, new_size):
#         self.s1 += new_size
#######################################

#######################################
# class Shape():
#     def what_am_i(self):
#         print("I am a shape.")


# class Rectangle(Shape):
#     def __init__(self, width, length):
#         self.width = width
#         self.length = length

#     def calculate_perimeter(self):
#         return self.width * 2 + self.length * 2


# class Square(Shape):
#     def __init__(self, s1):
#         self.s1 = s1

#     def calculate_perimeter(self):
#         return self.s1 * 4


# a_rectangle = Rectangle(20, 50)
# a_square = Square(29)
# a_rectangle.what_am_i()
# a_square.what_am_i()
#######################################

#######################################
# class Square:
#     square_list = []

#     def __init__(self):
#         self.square_list.append(self)
#######################################

#######################################
# class Square:
#     def __init__(self, s1):
#         self.s1 = s1

#     def calculate_perimeter(self):
#         return self.s1 * 4

#     def __repr__(self):
#         return "{} by {} by {} by {}".format(self.s1, self.s1, self.s1, self.s1)
#######################################

#######################################
# import re

# match = re.findall(".oo", "The ghost that says boo haunts the loo.")
# print(match)
#######################################

#######################################
#######################################
