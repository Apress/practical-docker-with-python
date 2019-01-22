import praw
from states import log
from constants import REDDIT_CLIENT_ID, REDDIT_CLIENT_SECRET

__author__ = 'Sathyajith'


def summarize(url):
    log.info('Not yet implemented!')
    return url


def get_latest_news(sub_reddits):
    log.debug('Fetching news from reddit')
    no_tokens_message = (
        "Reddit client id is not set, please create a client id as mentioned in"
        " https://github.com/reddit-archive/reddit/wiki/OAuth2-Quick-Start-Example#first-steps"
        " and set the environment variable `{}` similar to how `NBT_ACCESS_TOKEN` was done "
        )

    if REDDIT_CLIENT_ID is None:
        return no_tokens_message.format("REDDIT_CLIENT_ID")
    if REDDIT_CLIENT_SECRET is None:
        return no_tokens_message.format("REDDIT_CLIENT_SECRET")
    r = praw.Reddit(user_agent='SubReddit Newsfetcher Bot', client_id=REDDIT_CLIENT_ID, client_secret=REDDIT_CLIENT_SECRET)
    # Can change the subreddit or add more.
    sub_reddits = clean_up_subreddits(sub_reddits)
    log.debug('Fetching subreddits: {0}'.format(sub_reddits))
    submissions = r.subreddit(sub_reddits).hot(limit=5)
    submission_content = ''
    try:
        for post in submissions:
            submission_content += summarize(post.title + ' - ' + post.url) + '\n'
    except praw.errors.Forbidden:
            log.debug('subreddit {0} is private'.format(sub_reddits))
            submission_content = "Sorry couldn't fetch; subreddit is private"
    except praw.errors.InvalidSubreddit:
            log.debug('Subreddit {} is invalid or doesn''t exist.'.format(sub_reddits))
            submission_content = "Sorry couldn't fetch; subreddit doesn't seem to exist"
    except praw.errors.NotFound :
            log.debug('Subreddit {} is invalid or doesn''t exist.'.format(sub_reddits))
            submission_content = "Sorry couldn't fetch; something went wrong, please do send a report to @sathyabhat"
    return submission_content


def clean_up_subreddits(sub_reddits):
    log.debug('Got subreddits to clean: {0}'.format(sub_reddits))
    return sub_reddits.strip().replace(" ", "").replace(',', '+')
