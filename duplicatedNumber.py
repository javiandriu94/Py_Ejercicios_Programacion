from bubbleSort import bubbleSort

def removeDuplicatedNumber (arr):
    arr2 = []
    for i in range (len(arr)):
        if arr[i] not in arr2:
            arr2.append(arr[i])
    orderedArray = bubbleSort(arr2)
    return orderedArray

print(removeDuplicatedNumber([5,5,1,1,5,8,5,3,2,3]))