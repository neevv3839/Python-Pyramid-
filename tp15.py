no= int(input("enter the row: "))
n=1
m=2


for i in range(no,0,-1):
    for j in range(i,0,-1):
        print("",n,end="")
        n+=2
    n=1
    n=n+m
    m=m+2
    print()