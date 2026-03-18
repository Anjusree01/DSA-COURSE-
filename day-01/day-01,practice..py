#checking the no. even or odd
def check_num(num):
    if num % 2 == 0:
        print("even")
    else:
        print("odd")
def main():
    num = int(input("enter number:"))
    check_num(num)
main()

#checking maximum of two no.
def max_num(a,b):
    if a > b:
        print("a is greater")
    else:
        print("b is greater")
def main():
    a = int(input("enter no a:"))
    b = int(input("enter no b:"))
    max_num(a,b)
main()

#student grade deciding
def stu_gra(n):
    if n >= 90:
        print("O")
    elif n >= 80:
        print("A+")
    elif n >= 70:
        print("B+")
    elif n >= 60:
        print("C+")
    elif n >= 50:
        print("D+")
    else:
        print("Fail")
def main():
    n = int(input("enter the marks of the student:"))
    stu_gra(n)
main()

