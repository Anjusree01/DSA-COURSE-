#.
def merge_two_sorted(arr1, arr2):
    result = []
    i = j = 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            result.append(arr1[i])
            i += 1
        else:
            result.append(arr2[j])
            j += 1
    #remaining elements
    result.extend(arr1[i:])
    result.extend(arr2[j:])
    return result
arr1 = [1,3,5]
arr2 = [2,4,6]
print(merge_two_sorted(arr1, arr2))

#.
def first_occurence(arr, target):
    low = 0
    high = len(arr)-1
    result = -1
    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            result = mid
            low = mid + 1 #moving right
        elif target < arr[mid]:
            high = mid -1
        else:
            low = mid + 1
    return result
arr = [10,20,20,30]
target = 20
print("Element found at index: ",first_occurence(arr, target))

#.
def search_rotated_arr(arr, target):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        # to skip the duplicates
        if arr[low] == arr[mid] == arr[high]:
            low += 1
            high -= 1
        if arr[low] <= arr[mid]:
            if arr[low] <= target < arr[mid]:
                high = mid - 1
            else:
                low = mid + 1
        #right sorted
        else:
            if arr[mid] <= target <= arr[high]:
                low = mid + 1
            else:
                high = mid - 1
    return -1
arr = [4,5,6,7,0,1,2]
target = 6
print("Index:", search_rotated_arr(arr, target))
