#example of insertion sort
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        #shifting elements
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr
arr = [9, 4, 2, 7]
print(insertion_sort(arr))

#counting the shifts in insertion sort:
def insertion_sort(arr):
    count = 0
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        #shifting elements
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
        arr[j + 1] = key
        count += 1
    return arr,count
arr = [9, 4, 2, 7]
print(insertion_sort(arr))

#inserting an element in sorted array:

#arr = [1,3,5,7]
#x = 4
#arr = [1,3,4,5,7]
'''
approach:
1.start from end of an array
2.shift elements greater than x
3.insert x in correct position
'''


def insert_into_sorted(arr, x):
    arr.append(0)
    i = len(arr)-2
    #shifting elements to right
    while i >= 0 and arr[i] > x:
        arr[i+1] = arr[i]
        i -= 1
    #insert
        arr[i+1] = x
        return arr
arr = [1,3,5,7]
x = 4
print(insert_into_sorted(arr, x))


    
