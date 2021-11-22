FROM python:3.8
ADD /proxy/ /proxy
WORKDIR /proxy
RUN pip install pipenv
RUN pipenv install --system