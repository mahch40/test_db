print("piiiii")

import sqlite3
con = sqlite3.connect('Prices.db')
cur = con.cursor()
cur.execute("drop table Prices")
con.commit()
con.close()
