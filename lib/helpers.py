# lib/helpers.py
from models.patient import Patient 
from models.doctor import Doctor

# def helper_1():
#     print("Performing useful function#1.")


def exit_program():
    print("Goodbye!")
    exit()

def list_patients(): 
    patients = Patient.get_all() 
    print (patients)
    for patient in patients: 
        print(patient) 

def find_patient_by_user_input(): 
    name = input("Enter patient name: ") 
    patient = Patient.find_by_name(name) 
    print(patient) if patient else print(f'Patient {name} not found') 

def find_patient_by_id(): 
    patient_id = input("Enter patient ID: ") 
    patient = Patient.find_by_id(patient_id)
    print(patient) if patient else print(f'Patient with ID {patient_id} not found')

def create_patient(): 
    name = input("Enter patient name: ")
    age = input("Enter patient age: ") 
    gender = input("Enter patient gender: ") 
    address = input("Enter patient address: ") 
    ssn = input("Enter patient ssn: ") 
    try: 
        patient = Patient.create(name, age, gender,address, ssn) 
        print(f'Success: {patient}')

    except Exception as exc:
        print(f'Error creating patient:', exc)

def update_patient(): 
    patient_id = input("Enter patient ID: ")
    patient = Patient.find_by_id(patient_id) 
    if patient:
        try: 
            name = input("Enter new patient name: ") 
            patient.name = name  
            age = input("Enter new patient age: ") 
            patient.age = age 
            gender = input("Enter new patient gender: ") 
            patient.gender = gender 
            address = input("Enter new patient address: ")
            patient.address = address 
            ssn = input("Enter new patient ssn: ") 
            patient.ssn = ssn 
            patient.update() 
            print(f'Success: {patient_id}') 
        except Exception as exc: 
            print(f'Error updating patient:', exc) 
    else:  
        print(f'Patient with ID {patient_id} not found') 

def delete_patient(): 
    patient_id = input("Enter patient ID: ") 
    patient = Patient.find_by_id(patient_id)
    if patient:
        patient.delete() 
        print(f'Patient with ID {patient_id} deleted') 
    else: 
        print(f'Patient with ID {patient_id} not found') 


def list_doctors(): 
    doctors = Doctor.get_all_doctors() 
    print (doctors)
    for doctor in doctors: 
        print(doctor)

def find_doctor_by_name(): 
    name = input("Enter doctor name: ") 
    doctor = Doctor.find_by_name(name) 
    print(doctor) if doctor else print(f'Doctor {name} not found') 

def find_doctor_by_id(): 
    doctor_id = input("Enter doctor ID: ") 
    doctor = Doctor.find_by_id(doctor_id) 
    print(doctor) if doctor else print(f'Doctor with ID {doctor_id} not found') 

def create_doctor():
    name = input("Enter the doctor's name: ") 
    specialization = input("Enter the doctor's specialization: ") 
    patient_id = input("Enters the patient_id: ") 
    try: 
        doctor = Doctor(name, specialization, int(patient_id)) 
        print(f'Success: {doctor}') 
    except Exception as exc: 
        print(f'Error creating doctor:', exc) 

def update_doctor(): 
    doctor_id = input("Enter doctor ID: ") 
    doctor = Doctor.find_by_id(doctor_id) 
    if doctor:
        try: 
            name = input("Enter new doctor name: ") 
            doctor.name = name 
            specialization = input("Enter new doctor specialization: ") 
            doctor.specialization = specialization 
            patient_id = input("Enter new patient id: ") 
            doctor.patient_id = int(patient_id) 
            
            doctor.save() 
            print(f'Success {doctor}') 
        except Exception as exc: 
            print(f'Error updating doctor:', exc)  
        else: 
                print(f'Doctor with ID {doctor_id} not found') 

def delete_doctor(): 
    doctor_id = input("Enter doctor ID: ") 
    doctor = Doctor.find_by_id(doctor_id) 
    if doctor:
        doctor.delete() 
        print(f'Doctor with ID {doctor_id} deleted')  
    else: 
        print(f'Doctor with ID {doctor_id} not found') 

def list_patient_doctors(): 
    id_ = input("Enter patient ID: ") 
    patient = Patient.find_by_id(id_) 
    if patient:
        try:
            for doctor in patient.doctors():
                print(doctor)
        except Exception as exc:
            print("Error listing doctors", exc)
    else : 
        print(f"Can not find patient by id of {id_}")
     








