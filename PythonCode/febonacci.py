n=10
n1=0
n2=1
nextNum= n1+n2
print(n1)
print(n2)

for i in range(3, n+1):
    print(nextNum)
    n1 = n2
    n2 = nextNum
    nextNum = n1+ n2