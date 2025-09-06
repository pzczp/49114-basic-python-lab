ipt = int(input())
t = ipt
isPrime = True
while(t>1):
    t = t-1
    if(t==1):
        break
    if(ipt%t==0):
        isPrime = False
if isPrime:
    print(f"{ipt} prime")
else:
    print(f"{ipt} not prime")
