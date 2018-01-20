x=int(raw_input("Please enter the number "))
ans=0
while ans*ans*ans< abs(x):
    ans=ans+1
    print("Current quess= ", ans)
if ans*ans*ans != abs(x):
    print(x, "is not a perfect cube")
else:
    if x<0:
        ans= -ans
    print("Cube root of "+str(x)+" is "+str(ans))
