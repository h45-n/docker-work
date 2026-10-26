# this is stage 1: build
FROM python:3.8-slim as build

WORKDIR /app

RUN apt-get update && apt-get install -y \
    gcc \
    python3-dev \
    libmariadb-dev \
    pkg-config

COPY . .

RUN pip install flask mysqlclient

# step 2: production stage
FROM python:3.8-slim

WORKDIR /app
COPY --from=build /app /app

EXPOSE 5000

CMD ["python", "app.py"]