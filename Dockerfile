FROM python:3.9.10-alpine3.15 AS builder

RUN apk add build-base

COPY requirements.txt .

RUN CFLAGS=-fcommon pip install -r requirements.txt

FROM python:3.9.10-alpine3.15

COPY --from=builder /usr/local/lib/python3.9/site-packages/ /usr/local/lib/python3.9/site-packages/

WORKDIR /app

COPY dht22_exporter.py .

ENTRYPOINT [ "python", "-u", "dht22_exporter.py" ]
