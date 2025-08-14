import pandas as pd

def invalid_tweets(tweets: pd.DataFrame) -> pd.DataFrame:
    invalid = tweets[tweets['content'].str.len() > 15]
    result = invalid[['tweet_id']]
    return result
    