import sqlite3 
# 
# conn = sqlite3.connect('WeeklyFinData.db')
# c = conn.cursor()
# c.execute('SELECT Food FROM WeeklyFinData')
# food = c.fetchone()[0]
# print(food)
# 
# newVal = input("Enter a new value: ")
# 
# 
# 
# c.execute("UPDATE WeeklyFinData SET Food = ? WHERE rowid = 1",newVal)
# 
# 
# c.execute('SELECT Food FROM WeeklyFinData')
# food1 = c.fetchone()[0]
# print(food)
# print(food1)
# 
# 
# 
# 
# conn.commit()    
# conn.close()

    
conn = sqlite3.connect('WeeklyFinData.db')
c = conn.cursor()

c.execute('SELECT Date FROM WeeklyFinData WHERE rowid = 4')
date = c.fetchone()[0]
print("Date ", date)

# c.execute('SELECT Food FROM WeeklyFinData WHERE rowid = (4)')
# food = c.fetchone()[0]
# print("Food ", food)
# 
# c.execute('SELECT Washing FROM WeeklyFinData WHERE rowid = (4)')
# washing = c.fetchone()[0]
# print("Washing ", washing) 
# 
# c.execute('SELECT preDrinks FROM WeeklyFinData WHERE rowid = (4)')
# pre = c.fetchone()[0]
# print("Pre Drinks", pre)
# 
# c.execute('SELECT goingOut FROM WeeklyFinData WHERE rowid = (4)')
# goingOut = c.fetchone()[0]
# print("Going Out ", goingOut)
# 
# c.execute('SELECT Cigaretts FROM WeeklyFinData WHERE rowid = (4)')
# cig = c.fetchone()[0]
# print("Cigaretts", cig)
# 
# c.execute('SELECT Other FROM WeeklyFinData WHERE rowid = (4)')
# other = c.fetchone()[0]
# print("Other ", other)
# 
#            

conn.commit()    
conn.close()

