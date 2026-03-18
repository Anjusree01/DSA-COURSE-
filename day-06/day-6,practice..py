'''def cal_area(length, breath):
    return length * breath
print(cal_area(5,6))

#function to check prime number

def prime(num):
    if num <= 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True
def main():
    num = int(input("enter number: "))
    if prime(num):
        print("prime")
    else:
        print("not prime")
main()'''




def prime(num):
    if num <= 1:
        return False
    for i in range(2, num):
        if num % i != 0:
            return True
        
    return False
def main():
    num = int(input("enter number: "))
    if prime(num):
        print("composite")
    else:
        print("not composite")
main()
 


    
