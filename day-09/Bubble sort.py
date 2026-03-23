#bubble sort in ascending order
def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr
arr = [8,4,2,6]
print(bubble_sort(arr))

#bubble sort in descending order
def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] < arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr
arr = [8,4,2,6]
print(bubble_sort(arr))


#counting no.of swaps in descending order
def bubble_sort(arr):
    n = len(arr)
    count = 0
    for i in range(n):
        swapped = False
        count += 1
        for j in range(0, n-i-1):
            if arr[j] < arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
                count += 1
        if not swapped:
            break
    return arr,count
arr = [8,4,2,6]
print(bubble_sort(arr))

#arraging even no.s of an array
def bubble_sort(arr):
    n = len(arr)
    
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] % 2 == 0 and arr[j+1] % 2 == 0:
                if arr[j] < arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
                    swapped = True
                    
        if not swapped:
            break
    return arr
arr = [8,5,4,2,6,1,3]
print(bubble_sort(arr))
