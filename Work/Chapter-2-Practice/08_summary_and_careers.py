# import math
ttlAmt = float(input("Total: "))
tipPerc = int(input("Tip %: ")) / 100
splitAmt = int(input("Amount of people: "))
print("Each person pays " + str((ttlAmt + (tipPerc * ttlAmt)) / splitAmt))
