#Expense Tracker
expenses = []
def add_expenses():
    name = input("Enter expense name: ")
    amount = input("Enter amount expense: ")
    expense = {
        "name": name,
        "amount": amount
    }
    expenses.append(expense)
    print("Expense added.")
def view_expenses():
    for expense in expenses:
        print(expense["name"],"-",expense["amount"])
def show_menu():
    print("\nExpense Tracker")
    print("1.Add expenses")
    print("2.View expenses")
    print("3.Exit")
def main():
    while True:
        show_menu()
        choice = input("Enter choice: ")
        if choice == "1":
            add_expenses()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            print("Exiting the program")
            break
        else:
            print("Invalid choice. Try again")
main()
