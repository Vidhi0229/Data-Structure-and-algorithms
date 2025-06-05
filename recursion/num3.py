#print 1 to N by "Backtracking"
def printone(i, N):
    if(i < 1):
        return
    else:
        printone(i-1, N)
        print(i)

printone(9, 9)