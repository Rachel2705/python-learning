class patient:
    
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_detail(self):
        print("patient Name:", self.name)
        print("patient Age:", self.age)

# creating objects

Patient1 = patient("Rachel",25)
Patient2 = patient("Monica",30)

# calling methods

Patient1.display_detail()
Patient2.display_detail()