# Lisa Rehm, Financial Calculator Updated Python

def ask(category):
    return int(input(f"How much do you spend on {category} each month?\n"))

def info(income, amount, type):
    pertype = (amount/income)*100
    print(f"You spend ${amount:.2f} on {type}, which is {pertype:.2f}% of your income.\n")

print("Hello! This is a budget calculator!")
income = int(input("What is your monthly income?\n"))

rent = ask("rent or mortgage")
utilities = ask("utilities")
groceries = ask("groceries")
transportation = ask("transportation")

savings = income*0.1
spending = income-(rent+utilities+groceries+transportation+savings)
per_spending = spending/income*100

info(income, rent, "rent")
info(income, utilities, "utilities")
info(income, groceries, "groceries")
info(income, transportation, "transportation")

print(f"You have ${spending} left to spend, which is {per_spending:.2f}% amount of your income.")
print(f"We will put ${savings:.2f} in your savings.")
