import random as ra
print("Welcome To RPS Game\n")
print('Rock = 0 , Paper = 1 , scissors = 2')
# print('Please Select Your Coice:\n\n')

items = ['rock','paper','scissors']
players = ['computer','player']
choices = []

choices.insert(0,ra.choice(items)) 
userChoice = int(input("Enter your Choice = "))
choices.insert(1,items[userChoice]) 
result = ''
# rock
if(choices[0] == choices[1]):
    result = "TIE"
elif choices[0] == 'rock' and choices[1] == 'Paper':
    result = "WINS"
elif choices[0] == 'rock' and choices[1] == 'scissors':
    result = "LOSES"
elif choices[0] == 'paper' and choices[1] == 'rock':
    result = "LOSES"
elif choices[0] == 'paper' and choices[1] == 'scissors':
    result = "WINS"
elif choices[0] == 'scissors' and choices[1] == 'rock':
    result = "WINS"
elif choices[0] == 'scissors' and choices[1] == 'paper':
    result = "LOSES"

print("Result : ")
print(f"Computer Choice : {choices[0]}")
print(f"Player Choice: {choices[1]}")
print(f"Status: {result}")

