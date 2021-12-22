FROM python:3.10
RUN pip3 install pipenv

RUN mkdir /app
WORKDIR /app
COPY . /app
RUN pipenv install --system --deploy --ignore-pipfile

RUN mkdir -p /app/logs

ENV APP_ENV test
ENV FLASK_APP manage.py
ENV FLASK_RUN_PORT=5000
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_DEBUG=0

CMD ["flask", "run"]
