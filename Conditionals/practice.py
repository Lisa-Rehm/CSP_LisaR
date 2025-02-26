# Lisa Rehm, Old Enough Python

age = int(input("How old are you? (Please give a number).\n"))

if age >= 18:
    print("You are old enought to vote!")
else:
    if age >= 16:
        print("You are old enough to drive!")
    else:
        if age >= 15:
            print("You are old enough to get a learners permit!")
        else:
            if age >= 5:
                print("You are old enough to go to school!")
            else:
                print("You aren't old enough to do anything, sorry.")
