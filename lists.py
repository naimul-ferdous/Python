Techs= ["MIT", "Cal Tech"]
Ivys= ["Harvard", "Yale", "Brown"]
Univs= []
Univs.append(Techs)
print("Univs= ", Univs)

Univs.append(Ivys)
print('Univs= ', Univs)
for e in Univs:
    print('e= ', e)

flat= Techs+Ivys
print 'flat= ', flat

artSchools= ['RIBD', 'Harvard']
for u2 in artSchools:
    if u2 in flat:
        flat.remove(u2)

print 'flat= ', flat

flat.sort()
print 'flat= ', flat

flat[1]= 'Umass'
print 'flat= ', flat
