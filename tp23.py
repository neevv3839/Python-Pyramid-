no=int(input("Enter no of rows =>"))
n=no+1
m=no+1

for i in range(1,no+1,1):
    for j in range(m-i,n,1):
        print("",j,end="")
    m=n
    print("")