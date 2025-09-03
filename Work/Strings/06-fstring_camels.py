ipt = input()
a = ipt[0]
b = ipt[1:]
ltrIdx = 0
tm = 0
# check if number
for l in b:
    
    if l!='.':

        try:
            int(l)
        except:
            ltrIdx = tm
            break
    tm += 1
print(f'In {a} years I have spotted {b[:ltrIdx]} {b[ltrIdx:]}')
