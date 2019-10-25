import sqlite3

from models.user import User
from models.table import Table
from models.column import Column
from models.task import Task

def make_dicts(cursor, row):
    return dict((cursor.description[idx][0], value)
                for idx, value in enumerate(row))

  
db = sqlite3.connect('.data/db.sqlite')
db.row_factory = make_dicts

cur = db.cursor()


User.create_table(cur)
Table.create_table(cur)
Column.create_table(cur)
Task.create_table(cur)


users = [
    User("Ford","zda", "ford@betelgeuse.star", "12345"),
    User("Arthur","firero", "arthur@earth.planet", "12345"),
    User("ismail","Aissami", "a@a.a", "12345"),
    User("sana","kriaa", "sana.kriaaa@gmail.com", "aaa")
]

tables=[
    Table("Table1","a@a.a"),
    Table("Table2","a@a.a")
] 

columns=[
    Column("colonne1","Table1"),
    Column("colonne2","Table1")
]

tasks = [
    Task("descrep1","colonne1"),
    Task("descrep2","colonne1")
]

for user in users:
    user.insert(cur)

for table in tables:
    table.insert(cur)    
    
for column in columns:
    column.insert(cur)    

for task in tasks:
    task.insert(cur)
  
  
db.commit()

print("The following users has been inserted into the DB"
      " (all the passwords are 12345):")
for user in users:
    # uses the magic __repr__ method
    print("\t", user)
    

print("The following tables has been inserted into the DB")
for table in tables:
    print("\t", table)

    
print("The following columns has been inserted into the DB")
for column in columns:
    print("\t", column)

print("The following tasks has been inserted into the DB")
for task in tasks:
    print("\t", task)
print()
