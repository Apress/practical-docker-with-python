import praw
from states import log

__author__ = 'Sathyajith'


def get_latest_news(sub_reddits):
    log.debug('Fetching news from reddit')
    r = praw.Reddit(user_agent='NewsBot', 
                    client_id='ralalsYuEJXKDg',
                    client_secret="16DD-6O7VVaYVMlkUPZWLhdluhU")
    r.read_only = True
    
    # Can change the subreddit or add more.
    sub_reddits = clean_up_subreddits(sub_reddits)
    log.info(f'Fetching subreddits: {sub_reddits}')
    submissions = r.subreddit(sub_reddits).hot(limit=5)
    submission_content = ''
    try:
        for post in submissions:
            submission_content += post.title + ' - ' + post.url + '\n\n'
    except praw.errors.Forbidden:
            log.debug(f'subreddit {sub_reddits} is private')
            submission_content = "Sorry couldn't fetch; subreddit is private"
    except praw.errors.InvalidSubreddit:
            log.debug(f'Subreddit {sub_reddits} is invalid or doesn''t exist')
            submission_content = "Sorry couldn't fetch; subreddit doesn't seem to exist"
    return submission_content


def clean_up_subreddits(sub_reddits):
    log.debug(f'Got subreddits to clean: {sub_reddits}')
    return sub_reddits.strip().replace(" ", "").replace(',', '+')
