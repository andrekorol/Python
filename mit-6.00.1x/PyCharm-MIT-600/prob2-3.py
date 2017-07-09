balance = 3329
annualInterestRate = 0.2
monthlyInterestRate = annualInterestRate / 12.0
newbalance = balance
monthlyPayment = 0
while newbalance > 0:
    monthlyPayment += 10
    newbalance = balance
    month = 1

    while month <= 12 and newbalance > 0:
        newbalance -= monthlyPayment
        interest = monthlyInterestRate * newbalance
        newbalance += interest
        month += 1
    newbalance = round(newbalance, 2)

print('Lowest Payment: ' + str(monthlyPayment))