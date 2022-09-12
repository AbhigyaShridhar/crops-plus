FROM python:3.9

WORKDIR /app

ADD . /app

RUN pip install --no-cache-dir --upgrade -r requirements.txt

CMD ["uvicorn", "main:app","--reload", "--host", "0.0.0.0"]
