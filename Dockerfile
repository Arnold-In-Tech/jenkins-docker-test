# Dockerfile to build the unittest container

# Base image is python
FROM python:latest

# Author: Arnold
LABEL maintainer="Arnold <g16a7782@gmail.com>"

# Install redis driver for python and the redis mock
RUN pip3 install redis && pip3 install mockredispy

# Copy the test and source to the Docker image
ADD src/ /src/

# Change the working directory to /src/
WORKDIR /src/

# Make unittest as the default execution
ENTRYPOINT python3 -m unittest
