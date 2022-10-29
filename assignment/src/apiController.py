import requests

class ApiController():
    
    def get_Age_By_Name(self,name: str, url: str="https://api.agify.io?name=") -> str:
        # Get the age by sending a request to the api 
        req = url + name
        res = requests.get(req)
        data=res.json()
        return data["age"]

    def get_Gender_By_Name(self,name: str, url: str="https://api.genderize.io?name=")-> str:
        # Get the gender by sending a request to the api
        req = url + name
        res = requests.get(req)
        data=res.json()
        return data["gender"]

    def get_Nationality_By_Name(self,name: str, url: str="https://api.nationalize.io?name=")-> list:
        # Get the nationality list by sending a request to the api
        req = url + name
        res = requests.get(req)
        data=res.json()
        return data