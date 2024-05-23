FROM python:3.8-slim-buster

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

WORKDIR /app

RUN pip install --upgrade pip
RUN pip install gunicorn 
RUN pip install pipenv

RUN which gunicorn || echo "Gunicorn not found!"

COPY . /app/

EXPOSE 8000
CMD ["gunicorn", "tasktracker.wsgi:application", "-b", "0.0.0.0:8000"]