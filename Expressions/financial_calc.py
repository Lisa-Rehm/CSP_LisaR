# Lisa Rehm, Financial Calculator Python

print("Hello! This is a budget calculator!")
income = float(input("What is your monthly income?\n"))
rent = float(input("how much do you spend on rent or a mortgage each month?\n"))
utilities = float(input("How much do you spend on utilities each month??\n"))
groceries = float(input("How much do you spend on groceries each month??\n"))
transportation = float(input("How much do you spend on transportation each month??\n"))
savings = income*0.1
spending = income-(rent+utilities+groceries+transportation+savings)
per_rent = (rent/income)*100
per_utilities = (utilities/income)*100
per_groceries = (groceries/income)*100
per_transportation = (transportation/income)*100
per_spending = (spending/income)*100
print(f"You spend ${rent} on rent, which is {per_rent:.2f}% of your income.\n")
print(f"You spend ${utilities} on utilites, which is {per_utilities:.2f}% of your income.\n")
print(f"You spend ${groceries} on groceries, which is {per_groceries:.2f}% of your income.\n")
print(f"You spend ${transportation} on transportation, which is {per_transportation:.2f}% of your income.\n")
print(f"You have ${spending} left to spend, which is {per_spending:.2f}% of your income.\n")
print(f"We are going to put ${savings:.2f} in your savings.\n")
