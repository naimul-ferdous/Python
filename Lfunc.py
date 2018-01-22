def copyList(LSource, LDest):
    for e in LSource:
        LDest.append(e)
        print 'LDest= ', LDest

L1= []
L2= [1,2,3]
copyList(L2, L1)
print L1
print L2
copyList(L1, L1)
print L1
