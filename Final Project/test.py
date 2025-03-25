# Lisa Rehm and Eve Richardson, Test

# one = "1"
# print(one)
# 
# one = "X"
# print(one)

# blah = input("num 1-3:")

# if blah == 1:


(one, two, three, four, five, six, seven, eight, nine) = (1, 2, 3, 4, 5, 6, 7, 8, 9)

spaces = [one, two, three, four, five, six, seven, eight, nine]

def board():
    print(f" {spaces[0]} | {spaces[1]} | {spaces[2]} ")
    print("-----------")
    print(f" {spaces[3]} | {spaces[4]} | {spaces[5]} ")
    print("-----------")
    print(f" {spaces[6]} | {spaces[7]} | {spaces[8]} ")
    print(" ")


board()

def user_turn(spaces):
    taken_x = int(input("Pick a number between 1 and 9:\n"))
    if taken_x == 1 and spaces[0] == 1:
        spaces[0] = "X"
        board()
        winner()
    elif taken_x == 2 and spaces[3] == 2:
        spaces[1] = "X"
        board()
        winner()
    elif taken_x == 3 and spaces[2] == 3:
        spaces[2] = "X"
        board()
        winner()
    elif taken_x == 4 and spaces[3] == 4:
        spaces[3] = "X"
        board()
        winner()
    elif taken_x == 5 and spaces[4] == 5:
        spaces[4] = "X"
        board()
        winner()
    elif taken_x == 6 and spaces[5] == 6:
        spaces[5] = "X"
        board()
        winner()
    elif taken_x == 7 and spaces[6] == 7:
        spaces[6] = "X"
        board()
        winner()
    elif taken_x == 8 and spaces[7] == 8:
        spaces[7] = "X"
        board()
        winner()
    elif taken_x == 9 and spaces[8] == 9:
        spaces[8] = "X"
        board()
        winner()
    else:
        print("Pick a different number.")
        user_turn(spaces)
    return

def winner():
    if one==two==three=="O" or four==five==six=="O" or seven==eight==nine=="O" or one==four==seven=="O" or two==five==eight=="O" or three==six==nine=="O" or one==five==nine=="O" or three==five==seven=="O":
        print("Blue wins!")
    elif one==two==three=="X" or four==five==six=="X" or seven==eight==nine=="X" or one==four==seven=="X" or two==five==eight=="X" or three==six==nine=="X" or one==five==nine=="X" or three==five==seven=="X":
        name = input("What is your name?\n")
        print(f"Congratulations {name}, you won!")
    else:
        print("No winner yet, keep playing.")
        board()
        user_turn(spaces)



user_turn(spaces)


## blue_turn

#winner()
#
