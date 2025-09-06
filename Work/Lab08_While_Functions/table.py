def showTable(num,limit):
    i=1
    while(i<limit+1):
        print(f"{num} x {i} = {num*i}")
        i+=1
showTable(int(input()[-1]),int(input()[-1]))
