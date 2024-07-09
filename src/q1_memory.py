from datetime import datetime
import json
from collections import defaultdict, Counter
from typing import List, Tuple, Generator, Dict
# We this function to read the tweets from the file using a generator because im going to supose that the file is large and we dont want to load all the tweets into memory at once make it more memory efficient
def read_tweets(file_path: str):
    with open(file_path, 'r') as file:
        for line in file:
            
            yield json.loads(line)

def q1_memory(file_path: str) -> List[Tuple[datetime.date, str, int]]:
    tweet_counts_per_date = Counter()
    user_tweets_per_date = defaultdict(lambda: Counter())

    # Step 1 & 2: Read and process each tweet
    for tweet in read_tweets(file_path):
        date = datetime.strptime(tweet['date'], '%Y-%m-%dT%H:%M:%S%z').date()
        user = tweet['user']['username']
        tweet_counts_per_date[date] += 1
        user_tweets_per_date[date][user] += 1

    # Step 3 & 4: Identify top 10 dates
    top_10_dates = [date for date, _ in tweet_counts_per_date.most_common(10)]

    # Step 5: For each top date, find the user with the most tweets
    top_users = [(date, user_tweets.most_common(1)[0][0], user_tweets.most_common(1)[0][1]) for date, user_tweets in user_tweets_per_date.items() if date in top_10_dates]

    # Sort the result by date as the final step
    top_users_sorted = sorted(top_users, key=lambda x: x[0])

    return top_users_sorted

