import sqlite3

conn = sqlite3.connect('WeeklyFinData.db')

c = conn.cursor()

c.execute('''CREATE TABLE WeeklyFinData(Date text, Food real, Washing real, PreDrinks real, GoingOut real, Cigaretts real, Other real, TotalIn real, TotalOut real, Remainder real)''')



conn.commit()

conn.close()


# for row in c.execute('SELECT * FROM WeeklyFinData'):
#     print(row)
# 
# conn.commit()
# conn.close()