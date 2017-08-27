from patient import Patient

class Hospital(object):
    def __init__(self, name, capacity):
        self.patients = []
        self.name = name
        self.capacity = capacity
        self.beds = {}
        for x in range(capacity,0,-1):
            self.beds[x] = 0

    def admit(self, *patients):
        for x in range(len(patients)):
            if len(self.patients) < self.capacity:
                self.patients.append(patients[x])
                for key in self.beds:
                    if self.beds[key] == 0:
                        self.beds[key] = patients[x]
                        patients[x].bedNum = key
                        break #this breaks so that once it assigns the patient being appended a bed number it doesnt keep looping
            else:
                print 'Hospital is full!!'
        return self

    def discharge(self,patient):
        self.patients.remove(patient)
        self.beds[patient.bedNum] = 0
        patient.bedNum = None
        return self


patient1 = Patient('Faith', ('kindess', 'goofy', 'caring'))
patient2 = Patient('Tiwa', ('cute', 'ratchet', 'loving'))
patient3 = Patient('Yako', ('ratchet', 'tall', 'pseudo english'))
patient4 = Patient('Wura', ('ratchet', 'tall', 'pseudo english'))
patient5 = Patient('Vitali', ('kindess', 'goofy', 'caring'))
patient6 = Patient('Matt', ('cute', 'ratchet', 'loving'))
patient7 = Patient('John', ('ratchet', 'tall', 'pseudo english'))
patient8 = Patient('Ryan', ('ratchet', 'tall', 'pseudo english'))

hospital1 = Hospital('Premier', 5)

hospital1.admit(patient1,patient2,patient3) #when a patient is admitted he gets a bed and the bedkey become his bed number
hospital1.admit(patient7)
print len(hospital1.patients)

hospital1.discharge(patient2) #when a patient is discharged, the value of his key being his bedroom no gets changed to 0 so it's empty
print patient2.bedNum, len(hospital1.patients)

hospital1.admit(patient8,patient5, patient6)
print hospital1.beds
print len(hospital1.patients), patient8.bedNum, patient5.bedNum, patient6.bedNum #6 has no bed num cos the hospital is full 
