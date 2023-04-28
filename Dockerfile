FROM python:3.7.6-buster
MAINTAINER python_student

# RUN apt-get update && \
#     apt-get install -y openjdk-11-jdk ca-certificates-java && \
#     apt-get clean && \
#     update-ca-certificates -f
# ENV JAVA_HOME /usr/lib/jvm/java-11-openjdk-amd64/
# RUN export JAVA_HOME


RUN mkdir /pytest_project/
COPY ./test-requirements.txt /pytest_project/
COPY ./setup.py ./setup.py

RUN pip install --upgrade pip
RUN pip install -e .
RUN pip3 install -r /pytest_project/test-requirements.txt

WORKDIR /pytest_project/

CMD "pytest"
ENV PYTHONDONTWRITEBYTECODE=true

