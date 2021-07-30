# themnewsbot

Telegram bot which fetches Bot posts top submissions from a subreddit. NewsBot is used to demo a short, simple Python project in my book, [Practical Docker With Python](https://www.apress.com/gp/book/9781484237830). 

Refer to the [book repo](https://github.com/apress/practical-docker-with-python) for other exercises using this code.

### Getting started 

- Clone the repo or download the code
- Install the requirements with pip

    pip3 install -r requirements.txt

- Set the environment variable `NBT_ACCESS_TOKEN` where the value is the Bot token generated using Telegram BotFather.
    - See instructions on how to generate the token in Chapter 3 or [refer to this guide](https://core.telegram.org/bots/api#authorizing-your-bot)
    - See this guide on [how to set environment variables](https://core.telegram.org/bots/api#authorizing-your-bot)
- Start the bot 
    python newsbot.py

where `<token>` is the [Telegram Bot API](https://core.telegram.org/bots/api) token

