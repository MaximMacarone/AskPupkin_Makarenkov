# ./AskPupkin_Makarenkov/Dockerfile
FROM python:3.9
# set work directory
WORKDIR /opt/app
# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
# install dependencies
RUN pip install --upgrade pip
COPY requirements.txt /opt/app/requirements.txt
RUN chmod +x /opt/app/requirements.txt
RUN pip install -r requirements.txt
# copy project
COPY ./app/ /opt/app/app/
COPY ./AskPupkin_Makarenkov/ /opt/app/AskPupkin_Makarenkov/
COPY ./templates/ /opt/app/templates/
COPY ./manage.py /opt/app/manage.py

RUN apt update

RUN apt install -y wrk

RUN mkdir -p /opt/app/static
RUN echo "This is a static file" > /opt/app/static/static_file.txt

RUN mkdir -p /opt/app/templates
RUN echo "This is a dynamic file" > /opt/app/templates/dynamic_file.html

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]