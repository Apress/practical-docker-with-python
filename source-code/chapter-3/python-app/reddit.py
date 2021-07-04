import praw
from states import log

__author__ = 'Sathyajith'


def get_latest_news(sub_reddits):
    log.debug('Fetching news from reddit')
    r = praw.Reddit(user_agent='Practical Docker With Python tutorial')
    # Can change the subreddit or add more.
    sub_reddits = clean_up_subreddits(sub_reddits)
    log.debug(f"Fetching subreddits: {sub_reddits}")
    submissions = r.get_subreddit(sub_reddits).get_top(limit=5)
    submission_content = ''
    try:
        for post in submissions:
            submission_content += f"{post.title} - {post.url} \n\n"
    except praw.errors.Forbidden:
            log.info(f"subreddit {sub_reddits} is private".format())
            submission_content = "Sorry couldn't fetch; subreddit is private"
    except praw.errors.InvalidSubreddit:
            log.info(f"Subreddit {sub_reddits} is invalid or doesn''t exist.")
            submission_content = "Sorry couldn't fetch; subreddit doesn't seem to exist"
    except praw.errors.NotFound :
            log.info(f"Subreddit {sub_reddits} is invalid or doesn''t exist.")
            submission_content = "Sorry couldn't fetch; something went wrong, please do send a report to @sathyabhat"
    return submission_content


def clean_up_subreddits(sub_reddits):
    log.debug('Got subreddits to clean: {0}'.format(sub_reddits))
    return sub_reddits.strip().replace(" ", "").replace(',', '+')
