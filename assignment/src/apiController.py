import requests


class ApiController():

    def __init__(self):
        pass
    
    def get_Age_By_Name(self,name, url="https://api.agify.io?name="):
        req = url + name
        res = requests.get(req)
        data=res.json()
        return data["age"]

    def get_Gender_By_Name(self,name, url="https://api.genderize.io?name="):
        req = url + name
        res = requests.get(req)
        data=res.json()
        return data["gender"]

    def get_Nationality_By_Name(self,name, url="https://api.nationalize.io?name="):
        req = url + name
        res = requests.get(req)
        data=res.json()
        return data