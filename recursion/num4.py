#print Number N to 0 by "Backtracking"
def printNum(i, N):
    if(i > N):
        return
    else:
        printNum(i+1, N)
        print(i)


printNum(0, 9)