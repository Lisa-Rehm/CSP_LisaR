# Lisa Rehm, Financial Calculator Updated Python

print("Hello! This is a budget calculator!")

def ask((input("")), category):
    category = (input(f"How much do you spend on {category} each month?\n"))

def info(income, amount, type):
    pertype = (amount/income)*100
    print(f"You spend ${amount:.2f} on {type}, which is {pertype:.2f}% of your income.\n")


#income = float(input("What is your monthly income?\n"))
#rent = float(input("How much do you spend on rent or a mortgage each month?\n"))
#utilities = float(input("How much do you spend on utilities each month?\n"))
#groceries = float(input("How much do you spend on groceries each month?\n"))
#transportation = float(input("How much do you spend on transportation each month?\n"))


savings = income*0.1
spending = income-(rent+utilities+groceries+transportation+savings)
per_spending = spending/income*100

ask("rent or mortgage")
ask("utilities")
ask("groceries")
ask("transportation")

info(income, rent, "rent")
info(income, utilities, "utilities")
info(income, groceries, "groceries")
info(income, transportation, "transportation")

print(f"You have ${spending} left to spend, which is {per_spending} amount of your income.")
print(f"We will put ${savings} in your savings.")