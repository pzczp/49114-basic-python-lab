ttl = int(input("Assignments scores: ")) + int(input("Midterms scores: ")) + int(input("Finals scores: "))
gr = ''
if(80<=ttl<=100):
    gr='A'
elif(ttl>=75):
    gr='B+'
elif(ttl>=70):
    gr='B'
elif(ttl>=65):
    gr='C+'
elif(ttl>=60):
    gr='C'
elif(ttl>=55):
    gr='D+'
elif(ttl>=50):
    gr='D'
elif(ttl>=0):
    gr='F'
else:
    gr='what.'
print(gr)
