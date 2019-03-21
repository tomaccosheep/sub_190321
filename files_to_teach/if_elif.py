#if_elif.py
'''
Shift the comments around, what numbers will let you win the prize
'''
num = input("Type a number >")
num = int(num)
if num > 2:
    print("Greater than two")
if num < 8:
# elif num < 8:
# elif num > 8:
    print("You win a prize!!!!")
