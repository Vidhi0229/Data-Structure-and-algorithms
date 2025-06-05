#Sum of first n numbers

#parameterized way
def sumN(N, sum):
    if(N < 0):
        print(sum)
        return
    else:
        sumN(N - 1, sum+N)


sumN(3, 0)

#functional way
def summ(N):
    if(N <= 0):
        return 0
    else:
        return N + summ(N-1)

print(summ(4))