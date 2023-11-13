FROM python:3.9

LABEL authors="raphaelreis"

COPY . /app

WORKDIR /app

RUN pip install -r requirements.txt

ENTRYPOINT ["python", "app.py"]
