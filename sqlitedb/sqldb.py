import sqlite3
con = sqlite3.connect('my_database.db')
cur = con.cursor()
tablequery = "CREATE TABLE IF NOT EXISTS users ( id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, email TEXT);"

cur.execute(tablequery)

insertquery = "INSERT INTO users (name, email) VALUES (?,?)"
cur.execute(insertquery,('John Doe', 'johndoe@exaple.com'))

selectquery = "SELECT * FROM users"
cur.execute(selectquery)
rows = cur.fetchall()
for row in rows:
    print(row)

updatequery = "UPDATE users SET email = ? WHERE id = ?;"
cur.execute(updatequery, ('newemail@example.com', 1))

selectquery = "SELECT * FROM users"
cur.execute(selectquery)
rows = cur.fetchall()
for row in rows:
    print(row)

deletequery = "DELETE FROM users WHERE id = ?"
cur.execute(deletequery, (1,))

con.commit()
con.close()