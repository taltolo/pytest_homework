from src.utilities import Test_utilities

def pytest_generate_tests(metafunc):
    test_utilities = Test_utilities()
    person = test_utilities.preper_Person_List()
    if "person" in metafunc.fixturenames:
        metafunc.parametrize("person",person)