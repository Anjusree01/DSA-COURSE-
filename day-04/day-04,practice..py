
def count_chars(text): 
    count = 0 #intialize value zero to count
    for char in text:
        count += 1
    return count
def main():
    text = input("enter name:")
    print("character count:",count_chars(text))
main()

#counting vowels in a word:
def count_vowels(text): 
    count = 0 #intialize value zero to count
    vowels = "aeiouAEIOU"
    for char in text:
        if char in vowels:
            count += 1
    return count
def main():
    text = input("enter name:")
    print("vowels count:",count_vowels(text))
main()

#reversing a text
def rev_text(text):
    reversed_text = " "
    for char in text:
        reversed_text = char + reversed_text
    return reversed_text
text = input("enter text:")
print("reversed text: ",rev_text(text))

#count even no. in a string

def count_even_no(num):
    count = 0
    for i in str(num):
        if int(i) % 2 == 0:
            count += 1
    return count
def main():
    num = int(input(" enter a number:"))
    print("even count:",count_even_no(num))
main()
