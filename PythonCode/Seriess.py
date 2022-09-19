# harmonic series
num= int(input("Enter num : "))
sum=0
for i in range(1, num+1):
    if i!=1:
        print("+", end="")
    print("1/{}".format(i),end="")
    sum=sum+1.0/i
print()
print("Sum: ",sum)

