FROM python:3.8-slim

WORKDIR /app

COPY . .

#trying to install the depc'ies
RUN apt update 
RUN apt install python3-pip -y 
RUN pip install flask-redis

CMD ["python3", "app.py"]

EXPOSE 5000