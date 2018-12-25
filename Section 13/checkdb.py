import sqlite3

conn = sqlite3.connect('contacts.sqlite')

name = input("Please enter a name: ")       # LIKE below is for upper and lowercase

for row in conn.execute("SELECT * FROM contacts WHERE name LIKE ?", (name,)):  # Tuple containing a single value...
    print(row)                                                              # need a comma

conn.close()
