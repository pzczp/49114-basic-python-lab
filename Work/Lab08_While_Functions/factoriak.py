ipt = int(input())
t = ipt
sum = 1
while(ipt>0):
    sum = ipt * sum
    ipt = ipt - 1
print(f"{t}! = {sum}")
