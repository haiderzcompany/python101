print("Welcome to BMI Calculator\n\n")
weight = float(input('Enter Your Weight (in Kg ) = '))
height = float(input('Enter Your Height (in Feet ) = '))

bmi  = weight / (height/3.281)**2

if bmi < 18.5:
    print("You are Under weight, Eat Something")
elif bmi > 18.5 and bmi < 24.9:
    print("Your Weight is normal . MANTAIN YOUR DIET (chooki rakh)")
elif bmi > 25 and bmi < 29.9:
    print("You are Over-weight . Dont eat anything")
elif bmi > 30 and bmi < 34.9:
    print("You are OBESE . Eat less Junk Food")
else:
    print("You are Extreamly Over-weighted. Janver")