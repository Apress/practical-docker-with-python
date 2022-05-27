FROM python:3.7-alpine

RUN apk add gcc musl-dev python3-dev libffi-dev openssl-dev
WORKDIR /apps/subredditfetcher/
COPY . .

RUN pip install -r requirements.txt
VOLUME ["/data"]
CMD ["python", "newsbot.py"]
