# Lisa Rehm, Old Enough Python

age = int(input("How old are you? (Please give a number).\n"))

if age >= 18:
    print("You are old enought to vote!")
elif age >= 16:
    print("You are old enough to drive!")
elif age >= 15:
    print("You are old enough to get a learners permit!")
elif age >= 5:
    print("You are old enough to go to school!")
else:
    print("You aren't old enough to do anything, sorry.")
