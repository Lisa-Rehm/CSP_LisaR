# Lisa Rehm, Conditionals notes

#print("Hello, welcome to my program that will sort you into a category.")

#name = input("What is your name?\n")

#if name == "Vienna":
    #print("Oh, you're the teacher... never mind.")
#else:
    #print("You are a student, welcome to class.")



#num = int(input("How many would you like?.\n"))
##this could also be num = # and you just change the number in the code

#if num == 0:
    #print("You don't want any... why?")
#elif num == 1:
    #print("You have asked for an item")
#elif num <= 3:
    #print("You have asked for a couple of the item")
#elif num <= 5:
    #print("You have asked for a few of the item, or you are in the south then you asked for a couple")
#else:
    #print("You have asked for some of the item")

    ##conditionals start at the top and work their way down, they will only take the first condition that is correct, it will ignore everything else.
    ##top condition should be the least likely


name = "Katie"

if "a" in name or "e" in name or "i" in name or "o" in name or "u" in name:
    print("Your name has a vowel!")
else:
    print("Your name doesn't have a vowel.")

