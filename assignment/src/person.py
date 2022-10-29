class Person(object):

    def __init__(self,name: str,age: int,gender: str,nationality: float):
        self.name = name
        self.age = age
        self.gender = gender
        self.nationality = nationality

    def get_name(self) -> str:
        # Get person name
        return self.name

    def get_age(self) -> int:
        # Get person age 
        return self.age

    def get_gender(self) -> str:
        # Get person gender  
        return self.gender
    
    def get_nationality(self) -> float:
        # Get person nationality  
        return self.nationality

