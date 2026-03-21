#searching for a target value

def linear_search(arr, target):
    for i in range (len(arr)):
        if arr[i] == target:
            return i
    return -1 #not found

arr = [50,20,40,30,10]
target = 30
print("found at index: ",linear_search(arr, target))


# Q:arr = [50,40,30,20,30,10,30] , target = 30, find the count(30)

arr = [50,40,30,20,30,10,30]
count = 0
target = 30
for i in range (len(arr)):
    if arr[i] == target:
        count += 1
print(count)


def count_target(arr, target):
    count = 0
    for i in arr:
        if i == target:
            count += 1
    return count

def main():
    arr = [50,40,30,20,30,10,30]
    target = 30
    print("count", count_target(arr,target))
main()

#finding the -ve number
    
def linear_search(arr):
    for num in arr:
        if num < 0:
            return num
    return None #not found
arr = [50, 30, 20,-2,-3,-4,-5]
print("Negative number: ",linear_search(arr))
    
#-----------------------------------------------SELECTION SORT OF AN ARRAY-----

#sorting an array(incr):

def selection_sort(arr):
    n = len(arr)

    for i in range(n):
        min_index = i

        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        
        arr[i], arr[min_index] = arr[min_index], arr[i] #swap
    return arr
arr = [63, 25, 12, 22, 11]
print("Sorted Array: ", selection_sort(arr))

#sorting an array(dec):

def selection_sort(arr):
    n = len(arr)

    for i in range(n):
        max_index = i

        for j in range(i+1, n):
            if arr[j] > arr[max_index]:
                max_index = j
        
        arr[i], arr[max_index] = arr[max_index], arr[i] #swap
    return arr
arr = [63, 25, 12, 22, 11]
print("Sorted Array: ", selection_sort(arr))

#.To print an element of an entered index number:

def selection_sort(arr):
    n = len(arr)

    for i in range(n):
        min_index = i

        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        
        arr[i], arr[min_index] = arr[min_index], arr[i] #swap
    return arr[k-1]
arr = [63, 25, 12, 22, 11]
k = int(input("enter number:"))
print(k, "number from begining: ", selection_sort(arr))

