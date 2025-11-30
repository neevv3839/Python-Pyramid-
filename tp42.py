no=int(input("enter the row =>"))
n=no


for i in range(no, 0, -1):
    for j in range(no- i):
        print(" ", end="")
    for k in range(1, i + 1):
        print(n, end=" ")
    n-=1
    print() 