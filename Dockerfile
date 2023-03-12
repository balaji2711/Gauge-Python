FROM python:3.10.5

RUN apt-get update && apt-get install -y unixodbc-dev unixodbc

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Install Gauge and make sure it is in the system path
RUN wget -O - https://downloads.gauge.org/stable | sh
ENV PATH="/usr/local/bin:${PATH}"