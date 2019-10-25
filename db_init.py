import sqlite3

from models.user import User
from models.column import Column


def make_dicts(cursor, row):
    return dict((cursor.description[idx][0], value)
                for idx, value in enumerate(row))

  
db = sqlite3.connect('.data/db.sqlite')
db.row_factory = make_dicts

cur = db.cursor()


User.create_table(cur)
Column.create_table(cur)

users = [
    User("Ford","zda", "ford@betelgeuse.star", "12345"),
    User("Arthur","firero", "arthur@earth.planet", "12345"),
    User("ismail","Aissami", "a@a.a", "12345")
]

columns=[
    Column("colonne1","1"),
    Column("colonne2","2")
]

for user in users:
    user.insert(cur)

for column in columns:
  column.insert(cur)    

db.commit()

print("The following users has been inserted into the DB"
      " (all the passwords are 12345):")

for user in users:
    # uses the magic __repr__ method
    print("\t", user)
    
print("The following columns has been inserted into the DB")

for column in columns:
    # uses the magic __repr__ method
    print("\t", column)
print()
