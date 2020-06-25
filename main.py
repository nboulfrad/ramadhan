import time
import schedule
import hashtag_search

if __name__ == "__main__":
    schedule.every(3).hours.do(hashtag_search.hasht)
    while True:
        schedule.run_pending ()
        time.sleep ( 1 )
