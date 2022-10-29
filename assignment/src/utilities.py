import random
from src.person import Person
from src.apiController import ApiController

class Test_utilities():

    name_set=set(['Tal','Barak',"Oliver",'Luna','Amit',"Inbar","Shir","Adi","Mor","Ben"])

    def generate_Person_List(self) -> list:
        # Creating a Person by calling the api 
        # and adding it to the Person list 
        person_list=list()
        api = ApiController()
        for i in range(5):
            name = self.generate_Random_Name()
            age = api.get_Age_By_Name(name)
            gender = api.get_Gender_By_Name(name)
            json_nationality = api.get_Nationality_By_Name(name)
            nationalityList = self.extract_probability_to_array(json_nationality["country"])
            nationality = self.find_max(nationalityList)
            person = Person(name, age, gender, nationality)
            person_list.append(person)
        return person_list

    def generate_Random_Name(self) -> str:
        # Choicing a name from the set by calling random
        # Removing the name that has been chosen 
        # To avoid duplication 
        name = random.choices(list(self.name_set))
        self.name_set.remove(str(name[0]))
        return name[0]

    def extract_probability_to_array(self,jsonList: list) -> list:
        # Extracting the probability from each list
        # To probability list
        list = []
        for sub in jsonList:
            list.append(sub["probability"])
        return list
  
    def find_max(self,list: list) -> list:
        # Searching for the max probability 
        max = 0
        for probability in list:
            if probability > max :
                max = probability
        return max

    