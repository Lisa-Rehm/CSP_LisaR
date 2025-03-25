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


board()

def user_turn(spaces):
    taken_x = int(input("Pick a number between 1 and 9:\n"))
    if taken_x == 1:
        spaces[0] = "X"
        board()
        return board()
    elif taken_x == 2:
        spaces[1] = "X"
        board()
    elif taken_x == 3:
        spaces[2] = "X"
        board()
    elif taken_x == 4:
        spaces[3] = "X"
        board()
    elif taken_x == 5:
        spaces[4] = "X"
        board()
    elif taken_x == 6:
        spaces[5] = "X"
        board()
    elif taken_x == 7:
        spaces[6] = "X"
        board()
    elif taken_x == 8:
        spaces[7] = "X"
        board()
    elif taken_x == 9:
        spaces[8] = "X"
        board()
    else:
        print("pick a different number")
    return



user_turn(spaces)

board()

