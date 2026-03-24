from modules.add_transaction import add_transaction
from modules.view_summary import view_summary
from modules.visualization import plot_expenses
from modules.utils import initialize_database

def main():
    initialize_database()

    while True:
        print("\n===== Smart Expense Tracker =====")
        print("1. Add Transaction")
        print("2. Summary")
        print("3. Visualize")
        print("4. Exit")

        ch = input("Enter ur choice: ")

        if ch == "1":
            add_transaction()
        elif ch == "2":
            view_summary()
        elif ch == "3":
            plot_expenses()
        elif ch == "4":
            print("Thanks for using this application")
            break
        else:
            print("Invalid choice, try again")

if __name__ == "__main__":
    main()