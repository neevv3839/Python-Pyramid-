no=int(input("Enter no of rows =>"))
n=no
m=no

for i in range(0,no,1):
    for j in range(m-i,n,1):
        print("",j,end="")
    m=n
    print("")