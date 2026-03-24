import pandas as pd
import matplotlib.pyplot as plt
from modules.utils import get_connection

def plot_expenses():
    conn = get_connection()

    try:
        df = pd.read_sql_query(
            "SELECT * FROM transactions WHERE type='expense'", conn
        )

        if df.empty:
            print("No data to visualize")
            return

        summary = df.groupby('category')['amount'].sum()

        plt.figure(figsize=(8, 5))
        summary.plot(kind='bar', color='skyblue')

        plt.title("Expenses by Category")
        plt.xlabel("Category")
        plt.ylabel("Amount")
        plt.xticks(rotation=45)

        plt.tight_layout()
        plt.show()

    except Exception as e:
        print("Error: ", e)

    finally:
        conn.close()