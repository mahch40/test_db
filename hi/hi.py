print("piiiii")

import sqlite3
con = sqlite3.connect('Prices.db')
cur = con.cursor()
cur.execute('''drop table prices''')
con.commit()
con.close()
