FROM python:3.7
ENV PYTHONUNBUFFERED 1
RUN mkdir -p /usr/src
RUN mkdir -p /usr/src/static
WORKDIR /usr/src
COPY . /usr/src/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt