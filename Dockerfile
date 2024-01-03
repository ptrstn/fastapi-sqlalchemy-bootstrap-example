FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir --upgrade -r requirements.txt

ADD . /app

RUN pip install -e .

EXPOSE 8080

CMD uvicorn src.mypackage.main:app --host 0.0.0.0 --port 8080 --reload
