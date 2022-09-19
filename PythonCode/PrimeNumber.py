num= int (input("Enter Number: "))

x=int(num/2)+1
if num > 1:
    for i in range(2, x):
        if (num % i)== 0:
            print(num, "is not a prime number")
            break
        else:
            print(num," is a prime number")
            break
else:
    print(num, "is not a prime number")