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
three = "X"
four = "O"
five = "5"
six = "6"
seven = "7"
eight = "8"
nine = "9"

# Find a way to make the computer print our board
print(f" {one} | {two} | {three} ")
print("-----------")
print(f" {four} | {five} | {six} ")
print("-----------")
print(f" {seven} | {eight} | {nine} ")


name = input("What is your name?\n")


# draw a random number that create a list of our variables and have the computer draw a random one that doesn't include one already picked 
# For computers turner
# if random number = variable = X or O variable
def user():
    taken_x = input("Your turn! Pick a number between 1 and 9:\n")

import random
rand = random.randint(1,9)

# if there is 3 in a row then _ wins if one=two=three etc. else call loop
# else loop (has functions inside it to do user input and random computer number)

if one==two==three=="O" or four==five==six=="O" or seven==eight==nine=="O" or one==four==seven=="O" or two==five==eight=="O" or three==six==nine=="O" or one==five==nine=="O" or three==five==seven=="O":
    print("The winner is the computer!")
elif one==two==three=="X" or four==five==six=="X" or seven==eight==nine=="X" or one==four==seven=="X" or two==five==eight=="X" or three==six==nine=="X" or one==five==nine=="X" or three==five==seven=="X":
    print(f"Congratulations {name}, you won!")
elif one=="O" or "X" and two=="O" or "X" and three=="O" or "X" and four=="O" or "X" and five=="O" or "X" and six=="O" or "X" and seven=="O" or "X" and eight=="O" or "X" and nine=="O" or "X":
    print("Tie game!")
else:
    print("No winner yet, keep playing.")
   
