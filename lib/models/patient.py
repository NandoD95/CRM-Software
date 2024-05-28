from models.__init__ import CURSOR,CONN 

class Patient
    all = {} 

    def __init__(self,name,id) 
        self.name = name 
        self.id = id 
    
    def __repr__(self): 
        return f'<Patient name = {self.name}>' 

# Create a patient table if it doesnt  exist  
    @classmethod 
    def create_table(cls): 
        sql = """ 
            CREATE TABLE IF NOT EXISTS patients ( 
            id INTEGER PRIMARY KEY, 
            name TEXT 
            gender TEXT
            ssn INTEGER
            age INTEGER 
            address TEXT 
        )
        """ 
        CURSOR.execute(sql) 
        CONN.commit() 

# Delete a patient table  
    @classmethod 
    def delete_table(cls): 
        sql = "DROP TABLE IF EXISTS patients" 
        CURSOR.execute(sql) 
        CONN.commit() 

# Save patient to the database 
    def save(self): 
        sql = """ 
            INSERT INTO patients (name,gender,ssn,age,address)
            VALUES (?, ?, ?, ?, ?)
        """ 
        CURSOR.execute(sql,(self.name, self.gender, self.ssn, self.age self.address)) 
        CONN.commit() 
        self.id = CURSOR.lastrowid
       
# Create new patients into the database 
    @classmethod
    def create(cls,name,gender,ssn,age,adress) 
        new_patient = cls(name=name, gender=gender, ssn=ssn, age=age, address=address) 
        new_patient.save() 
        return new_patient  

# Delete patients from database 
    def delete(self): 
        sql = """ 
            DELETE FROM patients 
            WHERE id = ? 
        """ 
        CURSOR.execute(sql, (self.id,)) 
        CONN.commit() 
        self.id = none 

# Get all patients from database 
    @classmethod  
    def get_all(cls): 
        sql = "SELECT * FROM patients"  
        rows = CURSOR.execute(sql).fetchall()  

# Finds a patient in the database 
    @classmethod 
    def find_by_id(cls,id) 
        sql = """ 
            SELECT * FROM patients 
            WHERE id = ? 
        """ 
        row = CURSOR.execute(sql, (id,)).fetchone() 

# Finds patients by their name 
    @classmethod 
    def find_by_name(cls,name) 
        sql = """ 
            SELECT * FROM patients 
            WHERE name = ? 
        """ 
        rows = CURSOR.execute(sql, (name,)).fetchone()



        