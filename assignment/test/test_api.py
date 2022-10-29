import pytest
from src.apiController import ApiController as api
from src.utilities import Test_utilities as Utils

def test_validate_person(person: object):
    # Validating the data integrity against the APIs
    # By assert each person's attribute   
    server_api = api()
    utils = Utils()
    assert person.get_age() == server_api.get_Age_By_Name(person.get_name())
    assert person.get_gender() == server_api.get_Gender_By_Name(person.get_name())
    json_nationality = server_api.get_Nationality_By_Name(person.get_name())
    nationalityList = utils.extract_probability_to_array(json_nationality["country"])
    nationality = utils.find_max(nationalityList)
    assert person.get_nationality() == nationality