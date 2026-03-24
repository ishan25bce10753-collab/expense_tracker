import pandas as pd
from modules.utils import get_connection

def view_summary():
    conn = get_connection()

    try:
        df = pd.read_sql_query("SELECT * FROM transactions", conn)

        if df.empty:
            print("No transactions found")
            return

        total_income = df[df['type'] == 'income']['amount'].sum()
        total_expense = df[df['type'] == 'expense']['amount'].sum()

        print("\n===== SUMMARY =====")
        print(f"Total Income   : {total_income}")
        print(f"Total Expense  : {total_expense}")
        print(f"Balance        : {total_income - total_expense}")

        print("\n===== CATEGORY-WISE =====")
        print(df.groupby(['type', 'category'])['amount'].sum())

    except Exception as e:
        print("Error: ", e)

    finally:
        conn.close()