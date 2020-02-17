FROM ubuntu:16.04

MAINTAINER Tejas  "tejas.morbagal.harish@iais.fraunhofer.de"

RUN apt-get update -y 
RUN apt-get install -y python3-pip python3-dev 
RUN pip3 install --upgrade pip
RUN pip3 install grpcio-tools
RUN pip3 install numpy
RUN pip3 install pandas
RUN pip3 install sklearn
    
COPY ./requirements.txt /requirements.txt

WORKDIR /

RUN pip3 install -r requirements.txt

COPY . /

ENTRYPOINT [ "python3","house_prediction_server.py" ]




