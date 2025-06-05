#print number 1 to N
def printNum(num, N):
    if(num > N):
        return
    else:
        print(num)
        printNum(num + 1, N)


N = int(input("Enter number: "))
printNum(0, N)