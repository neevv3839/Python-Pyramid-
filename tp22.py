no=int(input("Enter no of rows =>"))
n=no

for i in range(no,0,-1):
    for j in range(n,n-i,-1):
        print("",j,end="")
    print("")