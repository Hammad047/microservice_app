FROM python:3.8.0-buster
WORKDIR /microservices_app
ADD . /microservices_app
EXPOSE 9000
COPY . /requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt