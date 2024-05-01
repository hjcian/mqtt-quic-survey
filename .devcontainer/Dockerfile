FROM python:3.8
RUN apt update
RUN apt install python3-dev cmake -y
# for pynng
RUN apt install libmbedtls-dev libmbedtls14 -y
RUN pip install --upgrade pip
COPY scripts/install_pynng-mqtt.sh .
RUN bash install_pynng-mqtt.sh

COPY python/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

