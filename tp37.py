no=int(input("enter the row"))

for i in range (1,no+1,1):
    for j in range (no-i):
        print(" ",end=" ")
    for k in range(1*i,0,-1):
        print(" ",k,end=" ")
    print()