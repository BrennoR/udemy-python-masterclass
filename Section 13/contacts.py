import sqlite3

db = sqlite3.connect('contacts.sqlite')
db.execute('CREATE TABLE IF NOT EXISTS contacts (name TEXT, phone INTEGER, email TEXT)')    # Don't use ; in Python
db.execute('INSERT INTO contacts (name, phone, email) VALUES ("Tim", 6545678, "Tim@email.com")')
db.execute('INSERT INTO contacts VALUES ("Bryan", 1234252, "Bryan@woa.com")')

cursor = db.cursor()
cursor.execute('SELECT * FROM contacts')

# print(cursor.fetchall())    # returns the list w/ all rows

print(cursor.fetchone())
print(cursor.fetchone())
print(cursor.fetchone())

for name, phone, email in cursor:
    print(name)
    print(phone)
    print(email)
    print('-' * 20)

# for name, phone, email in cursor:  # will not execute since the cursor already ran out of rows on last loop!
#     print(name)
#     print(phone)
#     print(email)
#     print('-' * 20)

cursor.close()
db.commit() # Must commit in order for inserted rows to stay
db.close()
