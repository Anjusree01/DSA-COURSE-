#Fee_Calculator
# this project will introduce conditional logic in real time project
#validation
#edge case handling

def calculate_fee(course, marks):
    if course == "AI":
        fee = 50000
    elif course == "Web":
        fee = 30000
    elif course == "Data Science":
        fee = 40000
    else:
        return None #Invalid Course

    #Discount Condition
    if marks > 90:
        fee -= 5000
    return fee

def main():
    course = input("Enter course: ")
    marks = int(input("Enter marks: "))

    fee = calculate_fee(course, marks)

    if fee is None:
        print("Invalid course selected")
    else:
        print("Final fee: ",fee)
main()