#print number N to 1
def printNum(Num):
    if(Num <= 0):
        return
    else:
        print(Num)
        printNum(Num - 1)


Num = int(input("Enter Number: "))
printNum(Num)