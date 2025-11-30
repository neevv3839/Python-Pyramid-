no = int(input("enter the row => "))
n=1
m=2

for i in range(1,no + 1):
    for j in range(1,i+1):
        print("",n, end="")
        n-=2
    n=1
    n=n+m
    m+=2
    print()