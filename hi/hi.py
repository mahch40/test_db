print("piiiii")

import sqlite3
con = sqlite3.connect('Prices.db')
cur = con.cursor()
cur.execute('''create table prices
            (
            id integer primary key,
            price integer)''')
con.commit()
con.close()
