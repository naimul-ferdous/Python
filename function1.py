def withinEpsilon(x, y, epsilon):
    return abs(x-y) <= epsilon
print withinEpsilon(2,3,1)
val= withinEpsilon(2,3,0.5)
print(val)
