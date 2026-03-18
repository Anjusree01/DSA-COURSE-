expenses = []

def export_expenses(expenses):
    with open("expenses.txt", "w")as file:
        for expense in expenses:
            file.write(expense["name"]+" "+expense["amount"]+"\n")
def main():
    while True:
        print("\n1. Add Expense")
        print("2. View Expense")
        print("3. Export to file")
        print("4. Exit")

        choice = input("Enter choice:")
        if choice == "1":
              name = input("Enter expense name: ")
              amount = input("Enter the amount: ")
              expenses.append({"name": name, "amount": amount})
        elif choice == "2":
            for expense in expenses:
                print(expense["name"], "-", expense["amount"])
        elif choice == "3":
            export_expenses(expenses)
        elif choice == "4":
            print("Exiting the program")
            break
        else:
            print("invalid Choice. Try Again")
main()