# given by the site:
# ----------------------------
balance = 3329
annualInterestRate = 0.2
# ----------------------------

monthlyInterestRate = annualInterestRate / 12.0

monthlyUnpaidBalance = 0

minimumFixedMonthlyPayment = 0


for month in range(12):
    if balance > 0:
        minimumFixedMonthlyPayment += 10
    monthlyUnpaidBalance = balance - minimumFixedMonthlyPayment
    balance = monthlyUnpaidBalance + monthlyInterestRate * monthlyUnpaidBalance

print('Lowest Payment: ' + str(minimumFixedMonthlyPayment))

# comentario

