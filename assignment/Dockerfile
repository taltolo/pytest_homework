FROM python:3.8

WORKDIR /assignment

COPY . /assignment 

RUN pip install requests pytest setuptools

RUN ["python","./setup.py","develop"]

CMD ["pytest","-q","./test/test_api.py"]

