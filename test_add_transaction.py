from modules.utils import initialize_database
from modules.add_transaction import add_transaction

def test_add():
    initialize_database()
    print("Run program and add transaction")