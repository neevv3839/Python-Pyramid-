no=int(input("Enter no of rows =>"))
n=1

for i in range(1,no+1,1):
    for j in range(1,i+1,1):
            print("",n,end="")
    n+=2
    print("")