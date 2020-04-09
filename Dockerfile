FROM python:3.7
EXPOSE 3000
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
WORKDIR /src
COPY src/req.txt req.txt
RUN pip install -r req.txt
COPY ./src/ .
WORKDIR /src/project
