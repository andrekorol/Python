balance = 42
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

monthlyInterestRate = annualInterestRate / 12.0

monthlyUnpaidBalance = 0

minimunMonthlyPayment = 0

for month in range(12):
    minimunMonthlyPayment = monthlyPaymentRate * balance
    monthlyUnpaidBalance = balance - minimunMonthlyPayment
    balance = monthlyUnpaidBalance + monthlyInterestRate * monthlyUnpaidBalance


print('Remaining balance: ' + str(round(balance, 2)))