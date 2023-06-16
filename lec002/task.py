print('Welcome to Tip Calculator')
currentBill = float(input('Total bill = '))
totalMembrs = int(input('Total Persons = '))
tipPercentage = float(input('Tip percentage = '))

totalBill = currentBill * (1+(tipPercentage / 100))

eachPersonBill = totalBill / totalMembrs
print(f'Total Bill IS = {totalBill}')
print(f'Each person should Pay {eachPersonBill} RS')
