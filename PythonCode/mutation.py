import random
class Genetic:
    sample= []
    sum=0
    for i in range (0,6):
        n=random.randint(1,15)
        sample.append(n)
    print(sample)
    for i in sample:
        sum=(15*i)-(pow(i,2))
        print("Fitness: ",sum)
def uniform_crossover(A,B,P):
    for i in range(0,6):
        if p[i]<0.6:
            temp=A[i]
            A[i]=B[i]
            B[i]=temp[i]

