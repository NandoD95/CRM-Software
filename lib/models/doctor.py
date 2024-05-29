from Patient import patient

class Doctor:
    all = []

    def __init__(self, name, patient_id, id=none):
        self.name = name
        self.patient_id = patient_id
        self.id = id
        Doctor.all.append(self)

    def __repr__(self): 
        return f'<Doctor name = {self.name}>' 

    @property
    def patient_id(self):
        return self._patient_id

    @patient_id.setter
    def patient_id(self, patient_id):
        if isinstance(patient_id, int):
            self._patient_id = patient_id
            else:
                raise TypeError("Patient ID must be an integer")

# Create a table for doctor
    @classmethod
    def create_table(cls):
        sql = """ 
            CREATE TABLE IF NOT EXISTS patients ( 
            id INTEGER PRIMARY KEY, 
            name TEXT 
            specialization TEXT 
            patient_id INTEGER 
        )
        """ 
        CURSOR.execute(sql) 
        CONN.commit()

# save db to table
    @classmethod
    def save(self): 
        sql = """ 
            INSERT INTO patients (name, specialization, patient_id)
            VALUES (?, ?, ?)
        """ 
        CURSOR.execute(sql,(self.name, self.specialization, self.patient_id)) 
        CONN.commit() 
        self.id = CURSOR.lastrowid

# save a doctor to db
    def save_doctor(self):
        sql = """
            INSERT INTO doctors (name, specialization, patient_id)
            VALUES (?, ?, ?)
        """
        CURSOR.execute(sql, (self.name, self.specialization, self.patient_id))
        CONN.commit()
        self.id = CURSOR.lastrowid
    
# create a new doctor
    @classmethod
    def create_doctor(cls, name, specialization, patient_id):
        new_doctor = cls(name=name, specialization=specialization, patient_id=patient_id)
        new_doctor.save()
        return new_doctor
