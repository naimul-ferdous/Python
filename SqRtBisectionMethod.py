x= 0.5
epsilon= 0.01
numGuesses= 0
low= 0.0
high= max(x, 1.0)
ans= (high+low)/2.0
while abs(ans**2 - x) >= epsilon and ans <= x:
    #print(low, high, ans)
    numGuesses += 1
    if ans**2 < x:
        low= ans
    else:
        high= ans
    ans= (high+low)/2.0
#print("numGuesses= ", numGuesss)
print(ans, " is close to the square root of ", x)
