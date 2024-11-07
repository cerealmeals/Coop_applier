import sys
import time
from login import login
from scraper import scraper


def main(args):
    user = args[1]
    secret = args[2]
    driver = login(user, secret)

    if driver == None:
        print("Sanity check login failed")
        return
    
    scraper(driver)
    
    time.sleep(10)
    driver.close()

if __name__=="__main__":
    if len(sys.argv) != 3:
        print("need 3 args")
    else:
        main(sys.argv)