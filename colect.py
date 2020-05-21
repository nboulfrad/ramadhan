import json
import tweepy as tw
import time


if __name__ == '__main__':

    consumer_key = 'aDw0qrmlSNEcTXdSJwfxVnrhR'
    consumer_secret = 'hngMVhVhryHXUlZgpCswP87lOst5jW7mncQx6omno5Y74LOMEE'
    access_token = '4684871288-g0Eyearzq8ekNU68mPrE5qibXmQULXnJsD45sqr'
    access_token_secret = '2wzOiLt8q8q48s9ck4lcSYa2RA3BVZXGPnoxpuIDw1IB4'
    auth = tw.OAuthHandler ( consumer_key, consumer_secret )
    auth.set_access_token ( access_token, access_token_secret )
    api = tw.API ( auth, wait_on_rate_limit=True )
    public_tweets = api.home_timeline ()
    search_words = "ramadan"
    search_words1 = "رمضان"
    search_words2 = "ramadhan"
    search_words3 = "ramazan"
    date_since = "2020-05-08"
    backoff_counter = 1
    while True:
        try:
            tweets = tw.Cursor ( api.search,
                                 q=search_words,
                                 since=date_since ).items ( 20000 )
            tweets1 = tw.Cursor ( api.search,
                                  q=search_words1,
                                  since=date_since ).items ( 20000 )
            tweets2 = tw.Cursor ( api.search,
                                  q=search_words2,
                                  since=date_since ).items ( 20000 )
            tweets3 = tw.Cursor ( api.search,
                                  q=search_words2,
                                  since=date_since ).items ( 20000 )

            list_tweets = [tweet for tweet in tweets] + [tweet for tweet in tweets1] + [tweet for tweet in tweets2] + [tweet for tweet in tweets3]
            json_str = []

            for user in list_tweets:
                json_str.append ( json.dumps ( user._json ) )
            print ( len ( json_str ) )

            f = open ( 'tweets21.jsonl', 'a' )
            for tweet in json_str:
                f.write ( tweet )
                f.write ( "\n" )
            f.close ()
            break
        except tw.TweepError as e:
            print ( e.reason )
            time.sleep ( 60 * backoff_counter )
            backoff_counter += 1
            continue
