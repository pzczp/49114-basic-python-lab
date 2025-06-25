cesuilus = 20
op = ''
if cesuilus<=0:
    op='Freezing'
elif 1<=cesuilus<=15:
    op='Cold'
elif 16<=cesuilus<=30:
    op='Warm'
elif cesuilus>30:
    op='Hot'
print(op)
