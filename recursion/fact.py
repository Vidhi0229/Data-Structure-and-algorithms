#parameterized way

def fact(N, m):
    if(N <= 0):
        print(m)
        return
    else:
        fact(N - 1, m * N)


fact(4, 1)

# functional way
def facto(N):
    if(N <= 0):
        return 1
    else:
        return N * facto(N - 1)

print(facto(5))