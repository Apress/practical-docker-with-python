FROM python:3-alpine

COPY * /apps/subredditfetcher/
WORKDIR /apps/subredditfetcher/
RUN ["pip", "install", "-r", "requirements.txt"]

ENV NBT_ACCESS_TOKEN="495637361:AAHIhiDTX1UeX17KJy0-FsMZEqEtCFYfcP8"

CMD ["python", "newsbot.py"]
