D= {1: 'one', 'daus': 'two', 'pi': 3.14159}
print D['pi']
D1= D
print D1
print D1[1]
D[1]= 'uno'
print D1
for k in D1.keys():
    print k, '=', D1[k]
