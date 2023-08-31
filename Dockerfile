# base image:
FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9

# copy requirements inside  container
COPY ./requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY ./app /app/app80_