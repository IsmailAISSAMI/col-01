import datetime


class Table:
    def __init__(self, name, idUser):
        self.name = name
        self.idUser = idUser
        self.timestamp = datetime.datetime.now().timestamp()

    def insert(self, cursor):
        cursor.execute('''
          INSERT INTO tables 
          ( tableName
          , idUser
          , timestamp
          )
          VALUES 
          ( ?, ?, ?)
        ''', (self.name, self.idUser, self.timestamp)
        )
    
        
    def __repr__(self):
        return "[tables < %s > created by User (#%s) at %s]"%(
            self.name,
            self.idUser,
            str(datetime.datetime.fromtimestamp(self.timestamp))
        )
    
    
    @classmethod
    def create_table(cls, cursor):
        cursor.execute('DROP TABLE IF EXISTS tables')

        cursor.execute('''
        CREATE TABLE tables
        ( tableName TEXT NOT NULL PRIMARY KEY
        , idUser TEXT NOT NULL
        , timestamp DOUBLE
        , FOREIGN KEY (idUser) REFERENCES users(email)
        )''')

        
class TableForDisplay:
    '''pour les var du constructeur verifie type alias colonne en main.elm'''
    def __init__(self, row):
        self.name = row['tableName'] 
        #self.idUser = row['idUser'] 
        self.date = datetime.datetime.fromtimestamp(row['timestamp'])
   
    @classmethod
    def getAll(cls, cursor):
      cursor.execute('''
          SELECT  tableName, timestamp 
          FROM tables
          ORDER BY timestamp DESC
      ''')
      return [ cls(row) for row in cursor.fetchall() ]