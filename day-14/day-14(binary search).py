def binary_search(arr, tar):
    if len(arr) == 0:
        return -1
    start = 0
    end = len(arr)-1
    while (start<=end):
        mid = start+(end-start)//2
        if(tar<arr[mid]):
            end = mid-1
        elif (tar>arr[mid]):
            start = mid+1
        else:
            return mid
    return "not found"
arr = [1,3,5,7,9,13,46]
tar = 9
print(binary_search(arr,tar))
