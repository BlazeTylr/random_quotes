FROM python:3.11-alpine

WORKDIR /usr/src/app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 3000

CMD [ "python", "./app.py" ]