# Lisa Rehm and Eve Richardson, Final Project

# a variables, 2 functions, a conditional, a loop

# Lisa: Functions that ask for user input and another that gets tha random number

# Eve variable (setting the numbers on the board to usable variables) and conditional that checks if someone won

#   1 | 2 | 3
#  -----------
#   4 | 5 | 6
#  -----------
#   7 | 8 | 9

one = "1"
two = "2"
three = "3"
four = "4"
five = "5"
six = "6"
seven = "7"
eight = "8"
nine = "9"

import random

spaces = [one, two, three, four, five, six, seven, eight, nine]

# Find a way to make the computer print our board

def board():
    print(f" {one} | {two} | {three} ")
    print("-----------")
    print(f" {four} | {five} | {six} ")
    print("-----------")
    print(f" {seven} | {eight} | {nine} ")

board()

name = input("What is your name?\n")


# draw a random number that create a list of our variables and have the computer draw a random one that doesn't include one already picked 
# For computers turner
# if random number = variable = X or O variable
def user_turn():
    taken_x = input("Your turn! Pick a number between 1 and 9:\n")
    if taken_x == "1":
        one = "X"
        board()
    elif taken_x == "2":
        two ="X"
    elif taken_x == "3":
        three = "X"
    elif taken_x == "4":
        four = "X"
    elif taken_x == "5":
        five = "X"
    elif taken_x == "6":
        six = "X"
    elif taken_x == "7":
        seven = "X"
    elif taken_x == "8":
        eight = "X"
    elif taken_x == "9":
        nine = "X"
    else:
        print(":/")


        




# def com_turn():
#   rand = random.randint(1,9)
# if one == rand


if one==two==three=="O" or four==five==six=="O" or seven==eight==nine=="O" or one==four==seven=="O" or two==five==eight=="O" or three==six==nine=="O" or one==five==nine=="O" or three==five==seven=="O":
    print("The winner is the computer!")
elif one==two==three=="X" or four==five==six=="X" or seven==eight==nine=="X" or one==four==seven=="X" or two==five==eight=="X" or three==six==nine=="X" or one==five==nine=="X" or three==five==seven=="X":
    name = input("What is your name?\n")
    print(f"Congratulations {name}, you won!")
else:
    print("No winner yet, keep playing.")
    board()
    user_turn()
   
