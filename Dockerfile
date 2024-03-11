FROM python:3.9.0-alpine
WORKDIR /usr/src/app
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
RUN pip install --no-cache --upgrade pip
COPY ./requirements.txt /usr/src/app/requirements.txt
RUN pip install --no-cache -r requirements.txt
COPY ./entrypoint.sh /usr/src/app/entrypoint.sh
COPY . /usr/src/app
ENTRYPOINT [ "/usr/src/app/entrypoint.sh" ]
