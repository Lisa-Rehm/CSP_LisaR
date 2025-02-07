# Lisa Rehm, Financial Calculator Python

# write a print statement telling the user what the program is (bugdet calculator)
print("Hello! This is a budget calculator!")
# Ask user for monthly income (user input)
income = float(input("What is your monthly income?\n"))
# Ask for rent/mortgage (user input)
rent = float(input("how much do you spend on rent or a mortgage each month?\n"))
# Ask for utilities (user input)
utilities = float(input("How much do you spend on utilities each month??\n"))
# Ask for groceries expenses (user input)
groceries = float(input("How much do you spend on groceries each month??\n"))
# Ask for transportation cost (user input)
transportation = float(input("How much do you spend on transportation each month??\n"))
# Calculate savings as 10% of income (variable) (tell user it is 10%)
print("That's all of my questions.\n")
print("We're going to put 10% of your income in savings.\n")
savings = income*0.1
# Calculate spending money income - (rent+utilities+groceries+transportation+savings) (variable)
spending = income-(rent+utilities+groceries+transportation+savings)
# Calculate percent of rent (rent/income) (variabe)
per_rent = (rent/income)*100
# Calculate percent of utilities (utilities/income) (variabe)
per_utilities = (utilities/income)*100
# Calculate percent of groceries (groceries/income) (variabe)
per_groceries = (groceries/income)*100
# Calculate percent of transportation (transportation/income) (variabe)
per_transportation = (transportation/income)*100
# Calculate percent of spending money (spending/total) (variable)
per_spending = (spending/income)*100
# tell user rent spending amount and percent ("You spend $xx.xx on rent and that is xx% of your income")
print(f"You spend ${rent} on rent, which is {per_rent:.2f}% of your income.\n")
# tell user utilities spending amount and percent ("You spend $xx.xx on utilities and that is xx% of your income")
print(f"You spend ${utilities} on utilites, which is {per_utilities:.2f}% of your income.\n")
# tell user groceries spending amount and percent ("You spend $xx.xx on groceries and that is xx% of your income")
print(f"You spend ${groceries} on groceries, which is {per_groceries:.2f}% of your income.\n")
# tell user transportation spending amount and percent ("You spend $xx.xx on transportation and that is xx% of your income")
print(f"You spend ${transportation} on transportation, which is {per_transportation:.2f}% of your income.\n")
# tell user spending amount and percent ("You spend $xx.xx on spending and that is xx% of your income")
print(f"You have ${spending} left to spend, which is {per_spending:.2f}% of your income.\n")
# tell user savings and percent ("You spend $xx.xx on savings and that is 10% of your income")
print(f"We are going to put {savings:.2f} in your savings.\n")
