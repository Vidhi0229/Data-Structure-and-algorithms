#parameterized way
def reverseArr(arr, i):
    if(i >= len(arr)/2):
        print(arr)
        return
    else:
        arr[i], arr[len(arr) - i - 1] = arr[len(arr) - i - 1], arr[i]
        reverseArr(arr, i+1)

arr = [1, 2, 3, 4, 5]


#functional way
def reverseArr(arr, i):
    if(i >= len(arr)/2):
        return arr
    else:
        arr[i], arr[len(arr) - i - 1] = arr[len(arr) - i - 1], arr[i]
        return reverseArr(arr, i+1)

print(reverseArr(arr, 0))
