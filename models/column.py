import datetime


class Column:
    def __init__(self, name, idTable):
        self.name = name
        self.idTable = idTable
        self.timestamp = datetime.datetime.now().timestamp()

    def insert(self, cursor):
        cursor.execute('''
          INSERT INTO columns 
          ( columnName
          , idTable
          , timestamp
          )
          VALUES 
          ( ?, ?, ?)
        ''', (self.name, self.idTable, self.timestamp)
        )
    
        
    def __repr__(self):
        return "[columns < %s > created in table (#%s) at %s]"%(
            self.name,
            self.idTable,
            str(datetime.datetime.fromtimestamp(self.timestamp))
        )
    
    
    @classmethod
    def create_table(cls, cursor):
        cursor.execute('DROP TABLE IF EXISTS columns')

        cursor.execute('''
        CREATE TABLE columns
        ( columnName TEXT
        , idTable TEXT NOT NULL
        , timestamp DOUBLE
        , FOREIGN KEY (idTable) REFERENCES users(email)
        )''')

        
class ColumnForDisplay:
    '''pour les var du constructeur verifie type alias colonne en main.elm'''
    def __init__(self, row):
        self.name = row['columnName']      
        self.date = datetime.datetime.fromtimestamp(row['timestamp'])
   
    @classmethod
    def getAll(cls, cursor):
      cursor.execute('''
          SELECT  columnName, timestamp 
          FROM columns
          ORDER BY timestamp DESC
      ''')
      return [ cls(row) for row in cursor.fetchall() ]