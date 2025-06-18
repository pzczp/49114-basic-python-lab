import math
ipt = int(input("Total: "))
print("Trays: " + str(math.floor(ipt / 30) + " Remaining: " + str(ipt % 30)))
