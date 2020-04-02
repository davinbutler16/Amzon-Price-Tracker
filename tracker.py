import db
import scraper
import time

URL = "https://www.amazon.co.uk/JBL-Reflect-Flow-Sport-Ear-Black/dp/B07N9G52SW/ref=sr_1_6?crid=1ZND2YAY87J49&dchild=1&keywords=jbl+wireless+headphones+bluetooth&qid=1585740096&sprefix=jpl+wi%2Caps%2C196&sr=8-6"

def track():
    details = scraper.get_product_details(URL)
    result = ""
    if details is None:
        result = "not done product details"
    else:
        inserted = db.add_product_detail(details)
        if inserted:
            result = "done"
        else:
            result = "not done adding do database"
    return result

while True:
    print(track())
    time.sleep(62)
