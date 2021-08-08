FROM python:3-alpine

RUN apk add gcc musl-dev python3-dev libffi-dev openssl-dev cargo
WORKDIR /apps/subredditfetcher/
COPY . .

RUN pip install --upgrade pip && pip install -r requirements.txt
VOLUME ["/data"]
CMD ["python", "newsbot.py"]
