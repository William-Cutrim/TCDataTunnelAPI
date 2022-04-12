# Dockerfile

# pull the official docker image
FROM tiangolo/uvicorn-gunicorn:python3.8-slim

#
WORKDIR /app

# set env variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

#
COPY ./requirements.txt /app/requirements.txt

#
RUN pip install --no-cache-dir --upgrade -r requirements.txt

#
COPY . .
EXPOSE 8000
#
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
