#############################################
# Base container with all necessary deps
FROM python:3.10 AS build

# load necessary packages
COPY . /app
WORKDIR /app

# 1. Local access and error logs will be written here
# 2. Install pipenv
# 3. Install dependencies from Pipfile.lock (dev dependencies wont be installed)
RUN mkdir -p /app/logs \
    && python -m pip install --upgrade pip \
    && pip3 install --no-cache-dir pipenv \
    && pipenv install --system --deploy --ignore-pipfile


EXPOSE 8080
ENV APP_ENV production
ENV ENV prod
ENV FLASK_APP manage.py
ENV FLASK_RUN_PORT=8080
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_DEBUG=0

#############################################
# Test container from a common base
FROM build AS flask-tests
ARG GITLAB_PROJECT_ID

# install dev dependencies which has the required packages for running tests
RUN pipenv install --dev --system --deploy --ignore-pipfile

ENV GITLAB_PROJECT_ID ${GITLAB_PROJECT_ID}
CMD ["pytest"]

#############################################
# Deploy container
FROM build AS deploy

CMD ["flask", "run"]
