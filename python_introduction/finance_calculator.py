#User input for financial details
monthly_income = input("Enter your monthly income: ")
monthly_expenses = input("Enter your total monthly expenses: ")

#calculating monthly savings
monthly_savings = float(monthly_income) - float(monthly_expenses)

#performing simple interest on savings
principal = monthly_savings * 12
rate = 0.05
time = 12

interest = principal * rate * time

#calculating the projected savings after a year
projected_savings = principal + interest

print(f'Your monthly savings are ${monthly_savings}')
print(f'Projected savings after one year, with interest is: ${projected_savings}')

