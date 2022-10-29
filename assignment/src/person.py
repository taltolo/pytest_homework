class Person(object):
    def __init__(self,name,age,gender,nationality):
        self.name = name
        self.age = age
        self.gender = gender
        self.nationality = nationality

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_gender(self):
        return self.gender
    
    def get_nationality(self):
        return self.nationality

