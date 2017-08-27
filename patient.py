count = 1
class Patient(object):
    def __init__(self, name, allergies):
        global count
        self.name = name
        self.idNum = count
        self.allergies = allergies
        self.bedNum = None 
        count += 1
