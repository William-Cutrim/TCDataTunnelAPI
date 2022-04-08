# Dockerfile

# pull the official docker image
FROM python:3.9

#
WORKDIR /app

#
COPY ./requirements.txt /app/requirements.txt

#
RUN pip install --no-cache-dir --upgrade -r requirements.txt

#
COPY . .

#
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
