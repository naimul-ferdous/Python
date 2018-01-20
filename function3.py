def f1(x):
    def g():
        x="abc"
    x= x+1
    print("x= ", x)
    g()
    assert False
    return x
x=3
z=f1(x)
