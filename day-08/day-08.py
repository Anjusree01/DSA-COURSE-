#Write a Python function to compute the prefix sum array of a given list of integers.
def prefix_sum(arr):
    arr = [1,2,3,4,5]
    prefix = [0]*len(arr) #prefix = [0,0,0,0,0]
    prefix[0] = arr[0]

    for i in range(1,len(arr)):
        prefix[i] = prefix[i-1]+arr[i]
    return prefix
arr = [1,2,3,4,5]
print("prefix sum:",prefix_sum(arr))

#Given an array of integers, compute the sum of elements between indices L and R (inclusive) using the prefix sum technique.
def prefix_sum(arr):
    prefix = [0] * len(arr)
    prefix[0] = arr[0]

    for i in range(1, len(arr)):
        prefix[i] = prefix[i-1] + arr[i]

    return prefix

arr = [1,2,3,4,5]
prefix = prefix_sum(arr)
L = 1
R = 3
if L == 0:
    print("Prefix Sum:", prefix[R])
else:
    print("Prefix Sum:", prefix[R] - prefix[L-1])

#.Write a Python function to check whether a given string is a palindrome.
def is_palindrome(string):
    left = 0
    right = len(string)-1

    while left < right:
        if string[left] != string[right]:
            return False
        left += 1
        right -= 1
    return True
string = "racecar"
print("panlindrome :", is_palindrome(string))
    
