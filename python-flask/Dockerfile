FROM python:3.6-alpine
MAINTAINER Cuong Ba

# Create app directory
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

# install Python modules needed by the Python app
COPY requirements.txt /usr/src/app/
RUN pip install --no-cache-dir -r /usr/src/app/requirements.txt

# Bundle app source
COPY . /usr/src/app

EXPOSE 5000

CMD ["python", "app.py"]