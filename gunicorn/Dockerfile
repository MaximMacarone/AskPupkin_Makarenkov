FROM python:3.9

WORKDIR /opt/app

RUN pip install --upgrade pip
COPY ./requirements.txt /opt/app/requirements.txt
RUN chmod +x /opt/app/requirements.txt
RUN pip install -r requirements.txt

COPY . /opt/app/
EXPOSE 8081
ENTRYPOINT ["gunicorn", "--bind", "0.0.0.0:8081", "simple"]