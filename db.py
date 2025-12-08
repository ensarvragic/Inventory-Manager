import sqlite3

DB_NAME = "inventory.db"


def init_db():
    conn = sqlite3.connect(DB_NAME)
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

    # funkcija s kojom uzimam sve iteme


def get_all_items():
    conn = sqlite3.connect("inventory.db")
    cr = conn.cursor()
    cr.execute('SELECT * FROM inventory')
    items = cr.fetchall()
    conn.close()
    return items
    # funkcija za dodavanje elemenata u magacin odnosno listu vodjenja magacina


def add_items(name, quantity, price):
    conn = sqlite3.connect("inventory.db")
    cr = conn.cursor()
    cr.execute('INSERT INTO inventory (name, quantity, price) VALUES (?, ?, ?)',
               (name, quantity, price))
    conn.commit()
    conn.close()



    # funkcija za brisanje elemenata
def delete_item(item_id):
    conn = sqlite3.connect("inventory.db")
    cr = conn.cursor()
    cr.execute('DELETE FROM inventory WHERE id=?', (item_id,))
    conn.commit()
    conn.close()



    # funkcija za odabir itema, putem ID-A
def get_item_by_id(item_id):
    conn = sqlite3.connect("inventory.db")
    cr = conn.cursor()
    cr.execute('SELECT * FROM inventory WHERE id=?', (item_id,))
    item = cr.fetchone()
    conn.close()
    return item


    # funkcija za update itema
def update_item(item_id, name, quantity, price):
    conn = sqlite3.connect("inventory.db")
    cr = conn.cursor()
    cr.execute('UPDATE inventory SET name=?, quantity=?, price=? WHERE id=?',
               (name, quantity, price, item_id))
    conn.commit()
    conn.close()


if __name__ == "__main__":
    init_db()
    check_data()
