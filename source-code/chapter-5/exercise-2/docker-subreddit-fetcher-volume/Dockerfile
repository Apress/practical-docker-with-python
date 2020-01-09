FROM python:3-alpine

RUN apk add gcc musl-dev python3-dev libffi-dev openssl-dev

COPY * /apps/subredditfetcher/
WORKDIR /apps/subredditfetcher/

RUN ["mkdir", "/apps/subredditfetcher/data/"]
RUN ["pip", "install", "-r", "requirements.txt"]
RUN ["python", "one_time.py"]

VOLUME [ "/apps/subredditfetcher/data" ]
ENV NBT_ACCESS_TOKEN="495637361:AAHIhiDTX1UeX17KJy0-FsMZEqEtCFYfcP8"

CMD ["python", "newsbot.py"]
