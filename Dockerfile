FROM python:3.9-slim-buster

COPY skrypt.py /app/

WORKDIR /app

ENTRYPOINT ["python", "skrypt.py"]