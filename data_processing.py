import sqlite3
import pandas as pd

def get_users_within_date_range(start_date, end_date):
    conn = sqlite3.connect('example.db')
    query = f"SELECT * FROM users WHERE join_date BETWEEN '{start_date}' AND '{end_date}'"
    users_df = pd.read_sql(query, conn)
    conn.close()
    return users_df

def calculate_total_spent():
    conn = sqlite3.connect('example.db')
    query = "SELECT user_id, SUM(amount) as total_spent FROM transactions GROUP BY user_id"
    total_spent_df = pd.read_sql(query, conn)
    conn.close()
    return total_spent_df

def generate_user_report():
    conn = sqlite3.connect('example.db')
    query = '''
    SELECT u.name, u.email, IFNULL(SUM(t.amount), 0) as total_spent
    FROM users u
    LEFT JOIN transactions t ON u.user_id = t.user_id
    GROUP BY u.user_id
    '''
    report_df = pd.read_sql(query, conn)
    conn.close()
    return report_df

def calculate_average_transaction_amount():
    conn = sqlite3.connect('example.db')
    query = "SELECT AVG(amount) AS average_transaction_amount FROM transactions"
    df = pd.read_sql(query, conn)
    conn.close()
    return df


if __name__ == "__main__":
    

    users_df = get_users_within_date_range('2024-01-01', '2024-12-31')
    total_spent_df = calculate_total_spent()
    report_df = generate_user_report()

    
    users_df.to_csv('users.csv', index=False)
    total_spent_df.to_csv('total_spent.csv', index=False)
    report_df.to_csv('user_report.csv', index=False)
