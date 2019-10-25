class Task:
    def __init__(self, description, idColonne):
        self.description = description
        self.idColonne = idColonne

    def insert(self, cursor):
        cursor.execute('''
          INSERT INTO tasks
          ( description
          , idColonne
          )
          VALUES 
          (?, ?)
        ''', (self.description, self.idColonne)
        )
    
    def __repr__(self):
        return "[tasks < %s > created in column %s]"%(self.description,self.idColonne)
    
    
    @classmethod
    def create_table(cls, cursor):
        cursor.execute('DROP TABLE IF EXISTS tasks')

        cursor.execute('''
        CREATE TABLE tasks
        ( description TEXT NOT NULL
        , idColonne TEXT NOT NULL 
        , FOREIGN KEY (idColonne) REFERENCES columns(columnName)
        )''')

        
class TaskforDisplay:
    def __init__(self, row):
        self.description = row['description']      
   
    @classmethod
    def getAll(cls, cursor):
      cursor.execute('''
          SELECT  description 
          FROM tasks
      ''')
      return [ cls(row) for row in cursor.fetchall() ]
        