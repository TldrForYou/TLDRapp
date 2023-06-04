FROM python:3.9

WORKDIR /code

COPY requirements.txt /code/

RUN pip install -r requirements.txt

COPY .env /code/
COPY service.py /code/
EXPOSE 80

CMD uvicorn service:app --host 0.0.0.0 --port 80