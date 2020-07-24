import schedule

import time

def do_nothing():
    print("aaaaa")
schedule.every(5).seconds.do(do_nothing)

schedule.run_pending()