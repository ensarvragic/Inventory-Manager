import sqlite3

def init_db():
    conn = sqlite3.connect("inventory.db")
    cur = conn.cursor()
    cur.execute(''' 
        CREATE TABLE IF NOT EXISTS inventory(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                quantity INTEGER NOT NULL,
                price REAL NOT NULL
                )


''')
    conn.commit()
    conn.close()


def check_data():
    conn = sqlite3.connect("inventory.db")
    cr = conn.cursor()
    cr.execute('SELECT * FROM inventory')
    print(cr.fetchall())

    
    conn.close()

if __name__ == "__main__":
    init_db()
    check_data()