from modules.utils import get_connection

def add_transaction():
    conn = get_connection()
    c = conn.cursor()

    try:
        t_type = input("Enter type (income/expense): ").strip().lower()
        if t_type not in ["income", "expense"]:
            print("Invalid")
            return

        category = input("Enter category: ").strip()
        amount = float(input("Enter amount: "))
        date = input("Enter date (YYYY-MM-DD format): ").strip()

        c.execute(
            "INSERT INTO transactions (type, category, amount, date) VALUES (?, ?, ?, ?)",
            (t_type, category, amount, date)
        )

        conn.commit()
        print("Transaction added")

    except ValueError:
        print("Invalid")

    finally:
        conn.close()