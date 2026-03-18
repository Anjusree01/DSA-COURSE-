# count even no. from 1 to n
'''def count_even(n):
    count = 0
    for i in range(1,n+1):
        if i % 2 == 0:
            count += 1
    return count
def main(): #may remove
    n = int(input("enter no:"))
    print("even count: ", count_even(n))
main() #may remove'''


'''count = 0
n = int(input("enter the number:"))
for i in range(0,n,2):
    count = count+1
print(count)'''

'''def even_num(n):
    count = 0
    for i in range(2,n+1,2):
        count = count+1
    print(count)
def main():
    n = int(input("enter the number n:"))
    even_num(n)
main()'''

#count no.s in a given number
'''def count_digits(num):
    count = 0
    while num > 0:
        num = num // 10
        count += 1
    return count
def main():
    num = int(input("enter number:"))
    print("digits count:", count_digits(num))
main()'''

#count no.of even digits in a given number
def c_even_num(num):
    count = 0
    while num>0:
        digit = num%10
        if digit%2==0:
            count += 1
        num = num//10
    return count
def main():
    num = int(input("enter a number:"))
    result = c_even_num(num)
    print("n0.of even digits",result)
main()

#count no.of even digits in a given number
def c_odd_num(num):
    count = 0
    for digit in str(num):
        if int(digit) % 2 != 0:
            count += 1
    return count
def main():
    num = int(input("enter a number:"))
    result = c_odd_num(num)
    print("n0.of odd digits",result)
main()
