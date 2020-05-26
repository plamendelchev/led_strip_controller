FROM python:3.8.3-buster

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY docker/ .

EXPOSE 5000

CMD [ "uwsgi", "app.ini" ]
