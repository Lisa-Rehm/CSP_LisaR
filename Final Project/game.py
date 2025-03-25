# Lisa Rehm and Eve Richardson, Final Project
# 
# # a variables, 2 functions, a conditional, a loop
# 
# # Lisa: Functions that ask for user input and another that gets tha random number
# 
# # Eve: variable (setting the numbers on the board to usable variables) and conditional that checks if someone won
# 
# # Blaine:
# 
# 
(one, two, three, four, five, six, seven, eight, nine) = (1, 2, 3, 4, 5, 6, 7, 8, 9)

print(five)

import random
# 
spaces = [one, two, three, four, five, six, seven, eight, nine]
# 
def board():
    print(f" {one} | {two} | {three} ")
    print("-----------")
    print(f" {four} | {five} | {six} ")
    print("-----------")
    print(f" {seven} | {eight} | {nine} ")

# #def board():  
# #    for i in range(1, 10, 3):  
# #        print(f" {board[i]} | {board[i+1]} | {board[i+2]} ")  
# #        if i < 7:  
# #            print("-----------")  
# 
# 
# board()
# 
# name = input("What is your name?\n")
# 
# 
# # draw a random number that create a list of our variables and have the computer draw a random one that doesn't include one already picked 
# # For computers turner
# # if random number = variable = X or O variable
# def user_turn():
#     taken_x = input(int("Your turn! Pick a number between 1 and 9:\n"))
#     if taken_x == 1:
#         one = "X"  
#     elif taken_x == 2:
#         two = "X"
#         board()
#     elif taken_x == 3:
#         three = "X"
#         board()
#     elif taken_x == 4:
#         four = "X"
#         board()
#     elif taken_x == 5:
#         five = "X"
#         board()
#     elif taken_x == 6:
#         six = "X"
#         board()
#     elif taken_x == 7:
#         seven = "X"
#         board()
#     elif taken_x == 8:
#         eight = "X"
#         board()
#     elif taken_x == 9:
#         nine = "X"
#         board()
#     else:
#         print("Else")
#         board()
#         
# 
#         
# 
# 
# 
# 
# #def com_turn():
# #  rand = random.randint(1,9)
# #if one == rand
# 
# 
# #def com_turn():
# #    rand = random.randint(1,9)
# #    if rand == 1:
# #        if 1 =="X":
# #            com_turn()
# #        else:
# #            "1" = "O"
# #            board()
# #    elif rand == 2:
# #        if 2 =="X":
# #            com_turn()
# #        else:
# #            "2" = "O"
# #            board()
# #    elif rand == 3:
# #        if 3 =="X":
# #            com_turn()
# #        else:
# #            "3" = "O"
# #            board()
# #    elif rand == 4:
# #        if 4 =="X":
# #            com_turn()
# #        else:
# #            "4" = "O"
# #            board()
# #    elif rand == 5:
# #        if 5 =="X":
# #            com_turn()
# #        else:
# #            "5" = "O"
# #            board()
# #    elif rand == 6:
# #        if 6 =="X":
# #            com_turn()
# #        else:
# #            "6" = "O"
# #            board()
# #    elif rand == 7:
# #        if 7 =="X":
# #            com_turn()
# #        else:
# #            "7" = "O"
# #            board()
# #    elif rand == 8:
# #        if 8 =="X":
# #            com_turn()
# #        else:
# #            "8" = "O"
# #            board()
# #    elif rand == 9:
# #        if 9 =="X":
# #            com_turn()
# #        elif 9 =="O":
# #            com_turn()
# #        else:
# #            "9" = "O"
# #            board()
# #    else:
# #        print("Tie Game!")
# 
# #com_turn()
# 
# if one==two==three=="O" or four==five==six=="O" or seven==eight==nine=="O" or one==four==seven=="O" or two==five==eight=="O" or three==six==nine=="O" or one==five==nine=="O" or three==five==seven=="O":
#     print("The winner is the computer!")
# elif one==two==three=="X" or four==five==six=="X" or seven==eight==nine=="X" or one==four==seven=="X" or two==five==eight=="X" or three==six==nine=="X" or one==five==nine=="X" or three==five==seven=="X":
#     name = input("What is your name?\n")
#     print(f"Congratulations {name}, you won!")
# else:
#     print("No winner yet, keep playing.")
#     board()
#     user_turn()
#    
# 