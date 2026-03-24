Smart Expense Tracker: BYOP

A simple Python-based command line application to keep track of daily income and expenses

This project helps in understanding spending habits by storing transactions and showing summary and graphs

What this project does:

1.Add income and expense entries

2.Store data using SQLite database

3.Show total income, total expense, and balance

4.Display category-wise summary

5.Generate a bar graph of expenses


Requirements:

Make sure Python is installed.

Install required libraries using:

    pip install pandas matplotlib

If pip doesn’t work:

    python -m pip install pandas matplotlib


How to run:

Open terminal in the project folder and run:

    python main.py


How to use:

After running the program, you will see a menu:

    Add Transaction
    View Summary
    Visualize Expenses
    Exit
        Choose option 1 to add income or expense
        Choose option 2 to see summary
        Choose option 3 to see graph


Notes:

    Database file is created automatically in the database folder
    Make sure to enter correct input format (especially date and amount)
    Graph will open in a new window


Limitations:

    Only command line interface (no GUI)
    No login system

Author: Ishan Choudhary 25BCE10753

