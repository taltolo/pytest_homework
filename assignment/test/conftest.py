from src.utilities import Test_utilities

def pytest_generate_tests(metafunc):
    test_utilities = Test_utilities()
    list_person=list()
    list_person.append( test_utilities.preper_Person_List())
    if "person_list" in metafunc.fixturenames:
        metafunc.parametrize("person_list",list_person)