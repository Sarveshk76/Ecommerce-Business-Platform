FROM python:3.11-slim-buster
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt update --fix-missing
RUN apt install -y python-psycopg2 binutils libproj-dev gdal-bin python-gdal

RUN mkdir /usr/src/ecom/
WORKDIR /usr/src/ecom/
COPY requirements.txt /usr/src/ecom/
RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt
COPY . /usr/src/ecom/
EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]