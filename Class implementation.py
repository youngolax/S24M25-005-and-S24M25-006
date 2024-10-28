# Encapsulation: Base class Staff with private attributes and public methods
class Staff:
    def __init__(self, staff_id, name, age, gender, role):
        # private attributes
        self.staff_id = staff_id
        self.name = name
        self.age = age
        self.gender = gender
        self.role = role
# Public Method
    def display_info(self):
        return f"Staff ID: {self.staff_id}, Name: {self.name}, Age: {self.age}, Gender: {self.gender}"

# Inheritance: Doctor class inherit from Staff
class Doctor(Staff):
    def __init__(self, staff_id, name, age, gender, speciality):
        super().__init__(staff_id, name, age, gender)
        self.speciality = speciality
        self.appointments = []
# Polymorphism: Method for adding a diagnosis is unique to doctors
    def diagnose(self, appointment, diagnosis):
        appointment.diagnosis = diagnosis

# Polymorphism: Method for adding appointments is unique to doctors
    def add_appointment(self, appointment):
        self.appointments.append(appointment)

# Polymorphism: Method for adding a diagnosis is unique to doctors
    def diagnose(self, appointment, diagnosis):
        appointment.diagnosis = diagnosis
        print(f"Diagnosis '{diagnosis}' added to appointment for Patient {appointment.patient.name}.")

# Inheritance: Nurse class inherits from staff class
class Nurse(Staff):
    def treat_patient(self, patient):
        return f"{self.name} is assisting in the treatment of patient {patient.name}."

class Patient:
    def __init__(self, patient_id, name, age, disease):
        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.disease = disease

    def get_patient_details(self):
        return f"Name:{self.name}, Age: {self.age}, Disease: {self.disease}"

class Appointment:
    def __init__(self, appointment_id, patient, doctor, date):
        self.appointment_id = appointment_id
        self.patient = patient
        self.doctor = doctor
        self.date = date
        self.diagnosis = None

    def display_info(self):
        diagnosis = self.diagnosis if self.diagnosis else "Pending"
        return f"Appointment {self.appointment_id} - {self.date}  with Dr. {self.doctor.name}, Diagnosis: {diagnosis}"

class Billing:
    def __init__(self, billing_id, patient, amount):
        self.billing_id = billing_id
        self.patient = patient
        self.amount = amount

    def display_info(self):
        return f"Billing ID: {self.billing_id}, Patient: {self.patient.name}, Amount Due: UGX{self.amount}"


