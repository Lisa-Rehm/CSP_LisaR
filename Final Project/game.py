# Lisa Rehm and Eve Richardson, Final Project

# a variables, 2 functions, a conditional, a loop

# Lisa: Functions that ask for user input and another that gets tha random number

# Eve: variable (setting the numbers on the board to usable variables) and conditional that checks if someone won

# Blaine:


(one, two, three, four, five, six, seven, eight, nine) = (1, 2, 3, 4, 5, 6, 7, 8, 9)

import random

spaces = [one, two, three, four, five, six, seven, eight, nine]

def board():
    print(f" {one} | {two} | {three} ")
    print("-----------")
    print(f" {four} | {five} | {six} ")
    print("-----------")
    print(f" {seven} | {eight} | {nine} \n")

#def board():  
#    for i in range(1, 10, 3):  
#        print(f" {board[i]} | {board[i+1]} | {board[i+2]} ")  
#        if i < 7:  
#            print("-----------")  


board()



# draw a random number that create a list of our variables and have the computer draw a random one that doesn't include one already picked 
# For computers turner
# if random number = variable = X or O variable

        

def user_turn(spaces):
    taken_x = int(input("Pick a number between 1 and 9:\n"))
    if taken_x == 1 and spaces[0] == 1:
        spaces[0] = "X"
        board()
    elif taken_x == 2 and spaces[3] == 2:
        spaces[1] = "X"
        board()
    elif taken_x == 3 and spaces[2] == 3:
        spaces[2] = "X"
        board()
    elif taken_x == 4 and spaces[3] == 4:
        spaces[3] = "X"
        board()
    elif taken_x == 5 and spaces[4] == 5:
        spaces[4] = "X"
        board()
    elif taken_x == 6 and spaces[5] == 6:
        spaces[5] = "X"
        board()
    elif taken_x == 7 and spaces[6] == 7:
        spaces[6] = "X"
        board()
    elif taken_x == 8 and spaces[7] == 8:
        spaces[7] = "X"
        board()
    elif taken_x == 9 and spaces[8] == 9:
        spaces[8] = "X"
        board()
    else:
        print("Pick a different number.")
        user_turn(spaces)
    return

rand = random.randint(1,9)

def blue_turn(rand):
    if rand == 1 and spaces[0] == 1:
        spaces[0] = "O"
        board()
    elif rand == 2 and spaces[1] == 2:
        spaces[1] = "O"
        board()
    elif rand == 3 and spaces[2] == 3:
        spaces[2] = "O"
        board()
    elif rand == 4 and spaces[3] == 4:
        spaces[3] = "O"
        board()
    elif rand == 5 and spaces[4] == 5:
        spaces[4] = "O"
        board()
    elif rand == 6 and spaces[5] == 6:
        spaces[5] = "O"
        board()
    elif rand == 7 and spaces[6] == 7:
        spaces[6] = "O"
        board()
    elif rand == 8 and spaces[7] == 8:
        spaces[7] = "O"
        board()
    elif rand == 9 and spaces[8] == 9:
        spaces[8] = "O"
        board()
    else:
        print("This will be something useful.")
    return

blue_turn(rand)


#def blue_turn():
#    rand = random.randint(0,8)
#    if rand == 1:
#        if 1 =="X":
#            com_turn()
#        else:
#            "1" = "O"
#            board()
#    elif rand == 2:
#        if 2 =="X":
#            com_turn()
#        else:
#            "2" = "O"
#            board()
#    elif rand == 3:
#        if 3 =="X":
#            com_turn()
#        else:
#            "3" = "O"
#            board()
#    elif rand == 4:
#        if 4 =="X":
#            com_turn()
#        else:
#            "4" = "O"
#            board()
#    elif rand == 5:
#        if 5 =="X":
#            com_turn()
#        else:
#            "5" = "O"
#            board()
#    elif rand == 6:
#        if 6 =="X":
#            com_turn()
#        else:
#            "6" = "O"
#            board()
#    elif rand == 7:
#        if 7 =="X":
#            com_turn()
#        else:
#            "7" = "O"
#            board()
#    elif rand == 8:
#        if 8 =="X":
#            com_turn()
#        else:
#            "8" = "O"
#            board()
#    elif rand == 9:
#        if 9 =="X":
#            com_turn()
#        elif 9 =="O":
#            com_turn()
#        else:
#            "9" = "O"
#            board()
#    else:
#        print("Tie Game!")

#com_turn()


    
   
