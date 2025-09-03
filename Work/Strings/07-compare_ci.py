ipt = input()
aidx = ipt.find("a")
bidx = ipt.find("b")
if(aidx<bidx):
    print("A comes before B")
elif(aidx>bidx):
    print("A comes after B")
else:
    print("A equals B")
