#looping patterns
n=int(input("Enter number of rows: "))
for i in range(n):               #*
    for j in range(i):           #* *
        print("*",end=" ")       #* * *
    print("*",end="\n")

n=int(input("Enter the number of rows :"))
for i in range(1,n+1):
    for j in range(i):
        print("*",end=" ")
    print()
 
for i in range(1,5,1):
    print("*" *i)

for i in range(5,0,-1):
    print("*"*i)
 
n=int(input("Enter number of rows: "))
for i in range(1,n+1):           #1
    for j in range(1,i+1):       #1 2
        print(j,end=" ")         #1 2 3
    print()

n=int(input("Enter number of rows: "))
for i in range(1,n+1):           #1
    for j in range(1,i+1):       #2 2
        print(i,end=" ")         #3 3 3
    print()

n=int(input("Enter the number of rows: "))
for i in range(n+1,1,-1):      #1 2 3
    for j in range(1,i):       #1 2
        print(j,end=" ")       #1
    print()
