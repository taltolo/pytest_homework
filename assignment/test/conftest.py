from src.utilities import Test_utilities

def pytest_generate_tests(metafunc):
    # Generate 5 different random person to sent to the test_api
    test_utilities = Test_utilities()
    person = test_utilities.generate_Person_List()
    if "person" in metafunc.fixturenames:
        metafunc.parametrize("person",person)