FROM python:3.10-slim

RUN apt-get update && apt-get install -y wireguard iproute2

WORKDIR /app

COPY . /app
RUN pip install --no-cache-dir -r requirements.txt

COPY start.sh /start.sh
RUN chmod +x /start.sh

CMD ["/start.sh"]
