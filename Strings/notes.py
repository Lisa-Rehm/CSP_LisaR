#Lisa Rehm, Strings Notes Python

# words in programming (data type) "" ''

# print("Hello world")

# print('Hello world') #you can use either "" or '' but don't mix them

#print('This is someone's code)
# print("this is someone's code")

# name = input("What is your first name?\n").strip().capitalize()
# stupid proofing is asking more straighforward questions and the sanitization
# print(f"Hello {name} welcome to my program.")

# num = input("Please give me a number with no decimal\n").strip()

# print(num + 1) 
# this doen't work because inputs are automatically strings so you have to tell it it's an integer

# num = input("Please give me a number with no decimal\n").strip()

# print(num + str(1)) 
# this doesn't work because it puts the 1 right after the input, it is because of the parentheses around the 1
# input = 5, output = 51, this is concatenation. when you add strings it put them next to each other. The fix is to convernt them to integers.

# sentence = "The quick brown fox jumps over the lazy dog."

# print(sentence.find("fox")) or if you want the whole word:

# word = sentence.find("fox)")
# print(sentence(word:word+3)) length of word
# print(sentence(4,9))
# print(len(sentence))
name = "Lisa"
percent = 89
print("Welcome to my program" +name)
print(f"Welcome to my program {name}!")
print(f"Welcome to my program {percent:.1f}!")
