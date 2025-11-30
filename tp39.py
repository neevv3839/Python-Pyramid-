no=int(input("enter the row =>"))
n=1

for i in range(no, 0, -1):
    for s in range(no- i):
        print(" ", end="")
    for num in range(1, i + 1):
        print(n, end=" ")
        n+=1
    n=1
    print() 