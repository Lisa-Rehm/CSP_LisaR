# Lisa Rehm, Silly Sentences

print("Welcome! This is a MadLib, have fun!\n")

num_one = input("Please give me a number (no more than three digits).\n").strip()

dinosaur = input("Please give me a type of dinosaur (one word please).\n").strip().capitalize()

name = input("Please give me a name (one word please).\n").strip().capitalize()

num_two = input("Please give me another number (no more than two digits).\n").strip()

gerund = input("Please give me a sport that ends in -ing (one word please).\n").strip().lower()

print("Here is your story:")

print(f"{num_one} million years ago, there was a {dinosaur} named {name} who had {num_two} siblings who all loved {gerund}.\n {name} hated {gerund} and always felt left out.\n Then the asteroid struck and everything was fine.\n")
