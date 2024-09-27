FROM python:3-alpine

WORKDIR /usr

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD [ "python", "./src/main.py" ]