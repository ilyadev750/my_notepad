FROM python:3.11.0-alpine
WORKDIR /app/my_notepad
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
COPY ./requirements.txt /app/my_notepad/requirements.txt
RUN apk add -u libffi-dev
RUN pip install --no-cache -r requirements.txt
COPY ./entrypoint.sh /app/my_notepad/entrypoint.sh
COPY . /app/my_notepad/
ENTRYPOINT [ "/app/my_notepad/entrypoint.sh" ]