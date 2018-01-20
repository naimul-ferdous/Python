x= 123456
epsilon= 0.01
numGuesses= 0
ans= 0.0
while abs(ans**2-x) >= epsilon and ans <= x:
    ans+=0.00001
    numGuesses += 1;
    #print("numGuesses = ", numGuesses)
if abs(ans**2 - x) >= epsilon:
    print("Failed on square root of", x)
else:
    print(ans, "is close to square root of ", x)
