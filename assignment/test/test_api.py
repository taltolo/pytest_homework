import pytest
from src.utilities import Test_utilities

@pytest.mark.parametrize("name,age,gender,nationality",[
    ("Tal",52,"male",0.927),
    ("Barak",56,"male",0.842),
    ("Oliver",46,"male",0.135),
    ("Luna",50,"female",0.084),
    ("Amit",47,"male",0.364),
    ("Inbar",41,"female",0.984),
    ("Shir",43,"female",0.79),
    ("Adi",48,"male",0.376),
    ("Mor",54,"male",0.41),
    ("Ben",54,"male",0.149)
    ])
def test_preper_person(person_list,name,age,gender,nationality):
    index=Test_utilities.get_person_by_name(person_list,name)
    if index == False:
        pytest.skip(name + " isn't in the list")
    assert name == person_list[index].get_name()
    assert age == person_list[index].get_age()
    assert gender == person_list[index].get_gender()
    assert nationality == person_list[index].get_nationality()