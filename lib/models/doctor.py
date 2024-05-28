from Patient import patient

class Doctor:
    all = []

    def __init__(self, name, patient_id):
        self.name = name
        self.specialty = specialty
        self.patient_id = patient_id
        Doctor.all.append(self)

    def __repr__(self): 
        return f'<Doctor name = {self.name}>' 

# Create a table for doctor
    @classmethod
    def create_table(cls):
        sql = """ 
            CREATE TABLE IF NOT EXISTS patients ( 
            id INTEGER PRIMARY KEY, 
            name TEXT 
            specialty TEXT
            appointments TEXT 
            patient_id INTEGER 
        )
        """ 
        CURSOR.execute(sql) 
        CONN.commit()

# save db to table
    @classmethod
    def save(self): 
        sql = """ 
            INSERT INTO patients (name, specialty, appointments, patient_id)
            VALUES (?, ?, ?, ?)
        """ 
        CURSOR.execute(sql,(self.name, self.specialty, self.appointments, self.patient_id)) 
        CONN.commit() 
        self.id = CURSOR.lastrowid
    
    
