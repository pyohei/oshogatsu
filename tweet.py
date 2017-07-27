# -*- coding: utf-8 -*-
"""
Tweet remaining days for next New Year.
"""
from calculation import Calculation
import tweepy
import os

TWEET_CONTENT = ("[自動投稿]\n今日で今年のrate%を消化。\n"
                 "残りday日です。\n今日も頑張りましょう！")
# Load setting from environment variables.
# You should set twitter variables to your environment.
consumer_key = os.environ.get("TWITTER_COMSUMER_KEY", None)
consumer_secret = os.environ.get("TWITTER_CONSUMER_SECRET", None)
access_key = os.environ.get("TWITTER_ACCESS_KEY", None)
access_secret = os.environ.get("TWITTER_ACCESS_SECRET", None)


def main():
    c = Calculation()
    rest_day = c.calc_rest_day()
    passed_rate = c.calc_passed_rate()
    content = TWEET_CONTENT.replace("rate", str(passed_rate))
    content = content.replace("day", str(rest_day))
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth_handler=auth)
    api.update_status(content)

if __name__ == '__main__':
    main()
