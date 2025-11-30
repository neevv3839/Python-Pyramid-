no= int(input("Enter limit => "))
n=1
m=2
for i in range(no,0,-1):
    for j in range((no-i)*2):
        print(" ", end="")
    for k in range(i):
           print(n,end=" ")	
           n+=2
    n=1
    n+=m
    m+=2
    print( )