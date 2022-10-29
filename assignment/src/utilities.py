import random
from src.person import Person
from src.apiController import ApiController

class Test_utilities():

    name_set=set(['Tal','Barak',"Oliver",'Luna','Amit',"Inbar","Shir","Adi","Mor","Ben"])

    def preper_Person_List(self):
        person_list=list()
        api = ApiController()
        for i in range(5):
            name = self.generate_Random_Name()
            print(name)
            age = api.get_Age_By_Name(name)
            gender = api.get_Gender_By_Name(name)
            json_nationality = api.get_Nationality_By_Name(name)
            nationalityList = self.extract_probability_to_array(json_nationality["country"])
            nationality = self.find_max(nationalityList)
            person = Person(name, age, gender, nationality)
            person_list.append(person)
        return person_list
        
    @staticmethod
    def get_person_by_name(listPersons,name):
        for i in range(len(listPersons)):
            person=listPersons[i]
            if person.get_name() == name:
                return i
        return False

    def generate_Random_Name(self):
        name = random.choices(list(self.name_set))
        self.name_set.remove(str(name[0]))
        return name[0]

    def extract_probability_to_array(self,jsonList):
        list = []
        for sub in jsonList:
            list.append(sub["probability"])
        return list
  
    def find_max(self,list):
        max = 0
        for probability in list:
            if probability > max :
                max = probability
        return max
