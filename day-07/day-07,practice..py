#finding the sum of elements in arrya:

def count_sum(arr):
    total = 0
    for num in arr:
        total += num
    return total
arr = [1, 2, 3, 4, 5]
print("Sum:", count_sum(arr))

#counting the digits in array

arr = [1,2,3]
print(len(arr))

arr = [6,7,3,4,8]
count = 0
for i in arr:
    count = count + 1
print(count)

def count_digit(arr):
    count = 0
    for i in arr:
        count += 1
    return count
def main():
    arr = list(map(int,input("enter the digits:").split()))
    print("count:", count_digit(arr))
main()

#counting the even digits in the array:

def count_even_digit(arr):
    even_count = 0
    for i in arr:
        if i % 2 == 0:
            even_count += 1
    return even_count
def main():
    arr = list(map(int,input("enter the digits:").split()))
    print("count:", count_even_digit(arr))
main()

#finding the max value in the array:

#arr = [1,7,8,5]
#max_value = arr[0]



def max_value(arr):
    max_value = arr[0]
    for i in arr:
        if i > max_value:
            max_value = i
    return max_value
def main():
    arr = list(map(int,input("enter the digits:").split()))
    print("max_value:", max_value(arr))
main()
    
    
