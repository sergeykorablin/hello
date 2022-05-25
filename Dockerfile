FROM python:3.8
LABEL maintainer="s.korablin@ya.ru"
WORKDIR /app

COPY requirements.txt /app

RUN pip install --upgrade pip -r requirements.txt
COPY main.py /app

EXPOSE 5000

#CMD ["python", "./hello.py"]
