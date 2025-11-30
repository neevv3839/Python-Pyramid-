no= int(input("enter the row: "))

num = [1,3,5,7,9]

for i in range(no):
    for j in range(i):
        print(" ", end="")
    for k in range(i,no):
        print("*", end="")
    print()