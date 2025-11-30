no=int(input("Enter no of rows =>"))
n=1
m=1

for i in range(no,0,-1):
    for j in range(1,i+1,1):
        print("",n,end="")
        n+=1
    n=1
    n=n+m
    m+=m
    print("")