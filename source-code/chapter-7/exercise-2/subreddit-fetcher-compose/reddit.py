import praw
from states import log

__author__ = 'Sathyajith'


def summarize(url):
    log.info('Not yet implemented!')
    return url


def get_latest_news(sub_reddits):
    log.debug('Fetching news from reddit')
    r = praw.Reddit(user_agent='SubReddit Newsfetcher Bot', 
                    client_id='ralalsYuEJXKDg',
                    client_secret="16DD-6O7VVaYVMlkUPZWLhdluhU")
    r.read_only = True
    
    # Can change the subreddit or add more.
    sub_reddits = clean_up_subreddits(sub_reddits)
    log.info('Fetching subreddits: {0}'.format(sub_reddits))
    submissions = r.subreddit(sub_reddits).hot(limit=5)
    submission_content = ''
    try:
        for post in submissions:
            submission_content += summarize(post.title + ' - ' + post.url) + '\n\n'
    except praw.errors.Forbidden:
            log.debug('subreddit {0} is private'.format(sub_reddits))
            submission_content = "Sorry couldn't fetch; subreddit is private"
    except praw.errors.InvalidSubreddit:
            log.debug('Subreddit {} is invalid or doesn''t exist.'.format(sub_reddits))
            submission_content = "Sorry couldn't fetch; subreddit doesn't seem to exist"
    return submission_content


def clean_up_subreddits(sub_reddits):
    log.debug('Got subreddits to clean: {0}'.format(sub_reddits))
    return sub_reddits.strip().replace(" ", "").replace(',', '+')
