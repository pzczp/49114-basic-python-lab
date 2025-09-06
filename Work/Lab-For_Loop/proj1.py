num = int(input("Enter your loop: "))
numttl = []
for i in range(num):
    dt = int(input("Enter data: "))
    numttl+= [dt]
print(numttl)
numttl.sort()
print(numttl)
