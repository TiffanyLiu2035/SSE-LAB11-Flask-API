FROM python:3.9

WORKDIR /app

COPY app.py books.py /app/
COPY requirements.txt /app/

RUN pip install -r requirements.txt

CMD ["python", "app.py"]
