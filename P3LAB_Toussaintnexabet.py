# P3LAB_ToussaintNexabet
# Gives amount of each specific currency after being given an amount of money
# 10/27/2024


amount = float(input("Enter the amount of money as a float: "))

# Convert the number to cents 
cents = int(round(amount * 100))

# number of dollars
dollars = cents // 100
cents %= 100

# of quarters
quarters = cents // 25
cents %= 25

# number of dimes
dimes = cents // 10
cents %= 10

# number of nickels
nickels = cents // 5
cents %= 5

# Rest are pennies
pennies = cents

# results
if dollars == 0:
    print("no change")


if dollars > 0:
    if dollars == 1:
        print("1 dollar")
    else:
        print(f"{dollars} dollars")


if dimes > 0:
    if dimes == 1:
        print("1 dime")
    else:
        print(f"{dimes} dimes")

if quarters > 0:
    if quarters == 1:
        print("1 quarter")
    else:
        print(f"{quarters} quarters")



if pennies > 0:
    if pennies == 1:
        print("1 penny")
    else:
        print(f"{pennies} pennies")
        
if nickels > 0:
    if nickels == 1:
        print("1 nickel")
    else:
        print(f"{nickels} nickels")
