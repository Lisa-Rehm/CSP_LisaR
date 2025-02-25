# Lisa Rehm, Old Enough Python

age = int(input("How old are you? (Please give a number).\n"))

if age >= 5:
    print("You are old enough to go to school!")
    if age >= 15:
        print("You are old enough to get a learners permit!")
        if age >= 16:
            print("You are old enough to drive!")
            if age >= 18:
                print("You are old enough to vote!")
else:
    print("You are not old enough to do anything. Sorry.")

# Make it so that only one statement prints
