n=int(input("enter the length of the series"))
def fib(n):
    x=0
    y=1
    print(x)
    print(y)
    for i in range(2,n):
        z=x+y
        x=y
        y=z
        print(z)
fib(n)
