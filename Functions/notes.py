# Lisa Rehm, Functions notes in python

# Function is an action stored in a key word

#def add():
#    numOne = int(input("Give me a number:\n"))
#    numTwo = int(input("Give me another number:\n"))
#    print(numOne+numTwo)

#add()
#add()
#add()
#every time you call the function the whole thing runs all over again

# the first variable naming method is called snake_case: no caps, underscores instead of spaces
# the first variable naming method is called camel_case: removes spaces, puts words next to eachother and any word after the first one starts with a capital

#Parameters and arguments:
#in the above function the () is black because there was no parameters

def add(numOne, numTwo): #parameters go in the () seperated by ,'s

    print(numOne+numTwo)

add(2, 4) #arguments are given when the function is called and must match the number of parameters
add(7,21)
add(int(input("Give me a number:\n")),20)


def add(int(input("Give me another number\n"),number): #parameters go in the () seperated by ,'s

    print(numOne+numTwo)

add(2, 4) #arguments are given when the function is called and must match the number of parameters
add(7,21)
add(int(input("Give me a number:\n")),20)


def user(word):
    input(f"Tell me a {word}:\n")

user("name")
user("verb")
user("place")


def user(word):
    return input(f"Tell me a {word}:\n")
    # any variable set in function can't be used outside of the function
name = user("name")
verb = user("verb")
place = user("place")
print(f"{name} was {verb} and somehow got to {place}.")

#Use a return statement, it is how you transfer info from the function to the rest of the code
