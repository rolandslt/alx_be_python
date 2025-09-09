# Define user input financial details
monthly_income = int(input("Enter your monthly income:"))
monthly_expenses = int(input("Enter your total monthly expenses:")) 
annual_interest = 0.5
#Calculate monthly savings 
monthly_savings = monthly_income - monthly_expenses

#Calculate project annual savings
projected_Savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)

#print the result
print(f"Your monthly savings are ${monthly_savings}")
print(f"Projected savings after one year, with interest, is: ${projected_Savings}")