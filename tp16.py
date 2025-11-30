no= int(input("enter the row: "))
n=no*2
m=2


for i in range(no,0,-1):
    for j in range(i,0,-1):
        if n%2==0 :
              print("",n-1,end="")
              n-=2
        else :
            print("",n,end="")
            n-=2
    n=no*2
    n=n-m
    m=m+2
    print()