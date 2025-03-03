# Lisa Rehm, Loops notes Python

# 1. What is a loop? 
    # a section of code that is going to repeat
# 2. What are the two types of loops?
    #while loop
x = 0
while x < 10:
    print("Hello\n", x)
    x +=1 #This makes it so that it doesn't repeat forever and ever

    #for loop
nums = [3,5,7,2,8]
for num in nums:
    print(num)
# 3. What is iteration
    # The act of repeating something

# 4. What are lists? 
    # a bunch of values in the same variable
siblings = ["Sara", "Megan", "Jeffrey", "Julia", "Amanda", "Stephanie", "Lisa", "Ryan"] #Lists have brackets and everything have to be the correct data type, each item is seperated by a comma
print(siblings) # This is ugly and awful
#Print one item
print(siblings[6])
#change an item in a list
siblings[4] = "Mandy"
print(siblings)
# remove an item
#siblings.pop(3)
#print(siblings)
# 5. How do you make lists in python? 
    # Have brackets with each item and commans in betweeen, make sure they are the same data type
    # It is proper to make a variable name for a list the plural version, so when you make your for loop you can use the singular version of the variable name
# 6. How do you make for loops in python? 
# proper print, for loops and lists go hand in hand
num = 1
for sibling in siblings:
    print(f"{num}, {sibling} Rehm")
    num +=1

for num in range(1,11, 2): #Go from 1 to 11 by twos
    print(num)

# 7. How do you make while loops in python?

num = 1

while num < 21:
    print(f"The number is {num}!")
    num += 1
# set by starting point, ending point, and amount you want to increase by for both while and for
# while: num, <21, +=1
# for num in range 1, 11, 2

import random #generates random things

num = 1
rand = random.randint(1,20)
while num < 21:
    if num == rand:
        print(f"Goose!")
        break #Even if the loop isn't finsihed, we are stopping it
    else:
        print(f"Duck!")
    num +=1
# you can also count these to see how many ducks you got

# continue tells you to stop that particular round or iteration of the loop
# It goes back to the top of the loop over and over again
