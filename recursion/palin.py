#parameterized way
def palindrome(str, i):
    if i >= len(str)/2:
        print("True")
        return
    if str[i] != str[len(str) - i -1]:
        print("False")
        return
    else:
        palindrome(str, i+1)
    

str = "AABBBBAA"
#palindrome(str, 0)

#functional way
def palin(str, i):
    if i >= len(str)/2:
        return True
    if str[i] != str[len(str) - i -1]:
        return False
    else:     
        return palin(str, i+1)
    
print(palin(str, 0))