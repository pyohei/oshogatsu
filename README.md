# oshogatsu

Tweet remaining days for next New Year days.

## Python version

I checked the below version,

* 2.7.10
* 3.6.1

## Usage

You set twitter consumer key and access key in environment values.  
The below is sample.

```bash
export TWITTER_COMSUMER_KEY=xxxxxx
export TWITTER_CONSUMER_SECRET=xxxxxxx
export TWITTER_ACCESS_KEY=xxxxxxxx
export TWITTER_ACCESS_SECRET=xxxxxxxx
```

After setting, you can tweet as follows,

```python
python2.7 tweet.py
```

## Attention

If you tweet twice in same day, Twitter API return error.  
So you have to delete previous tweet.

## Licence

MIT
