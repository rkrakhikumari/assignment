import sqlite3
from datetime import datetime


conn = sqlite3.connect('example.db')
cursor = conn.cursor()


cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                    user_id INTEGER PRIMARY KEY,
                    name TEXT,
                    email TEXT,
                    join_date DATE)''')


cursor.execute('''CREATE TABLE IF NOT EXISTS transactions (
                    transaction_id INTEGER PRIMARY KEY,
                    user_id INTEGER,
                    amount REAL,
                    transaction_date DATE,
                    FOREIGN KEY(user_id) REFERENCES users(user_id))''')


users = [
    (1, 'Harry', 'harry@example.com', '2024-01-01'),
    (2, 'Potter', 'potter@example.com', '2024-02-15'),
    (3, 'hermione', 'hermione@example.com', '2024-03-10'),
    (4, 'Ron', 'ron@example.com', '2024-03-15')

]
cursor.executemany('INSERT INTO users VALUES (?, ?, ?, ?)', users)


transactions = [
    (1, 1, 150.00, '2024-04-01'),
    (2, 2, 200.00, '2024-05-01'),
    (3, 3, 500.00, '2024-06-01'),
    (4, 4, 300.00, '2024-07-01'),
    (5, 1, 70.00, '2024-08-01')

]
cursor.executemany('INSERT INTO transactions VALUES (?, ?, ?, ?)', transactions)


conn.commit()
conn.close()

print("Database initialized with sample data.")
