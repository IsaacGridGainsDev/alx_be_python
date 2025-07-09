#User input for financial details
income = input("Enter your monthly income: ")
expense = input("Enter your total monthly expenses: ")

#calculating monthly savings
savings = int(income) - int(expense)

#performing simple interest on savings
principal = savings * 12
rate = 0.05
time = 12

interest = principal * rate * time

#calculating the projected savings after a year
projected_savings = principal + interest

print(f'Your monthly savings are ${savings}')
print(f'Projected savings after one year, with interest is: ${projected_savings}')

