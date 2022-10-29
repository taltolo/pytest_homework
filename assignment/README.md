The app generate 5 different random persons by 5 different names.
By the name calling an api request 3 time to get: age, gender and nationality.
Following, it validate the data integrity against the APIs by perform
assertions test on each of the atribute of the person.
The requirements packes: requests pytest setuptools.
In the project directory run: python ./setup.py develop
To invoke the code, from the project directory cd to test,
than in the comand line run: pytest -q .\test_api.py

If you prefer to run the Dockerfile
In the project directory run: docker build -t "imagename" .
than run: docker run "imagename"
