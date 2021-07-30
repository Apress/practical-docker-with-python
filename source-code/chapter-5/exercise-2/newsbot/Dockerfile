FROM python:3-alpine

RUN apk add gcc musl-dev python3-dev libffi-dev openssl-dev
WORKDIR /apps/subredditfetcher/
COPY . .

RUN mkdir -p /apps/subredditfetcher/data/ && \
    pip install -r requirements.txt && \
    python one_time.py

VOLUME [ "/apps/subredditfetcher/data" ]

CMD ["python", "newsbot.py"]
