import datetime
import pprint
import smtplib
from scraper import WebScraper
import json

email = 'sntest20@gmail.com'
password = 'Srautharsh19$'
# region parameters setup
dt = datetime.datetime.today()
months = ["January",
          "February",
          "March",
          "April",
          "May",
          "June",
          "July",
          "August",
          "September",
          "October",
          "November",
          "December"]
month = months[dt.month - 1]
day = dt.strftime("%A %#d")
school_value = "7001"


# endregion

def dump_in_json():
    scraper = WebScraper()
    scraper.set_parameters(school_value, month, menu="Lunch")

    dates, food_items = scraper.scrape_all()
    menu = {}
    for i in range(len(food_items) - 1):
        food_list = food_items[i].text
        new_food_str = food_list.replace("w/", 'with')
        menu[dates[i]] = new_food_str
    scraper.quit()
    with open("menu.json", 'w') as file:
        json.dump({month: menu}, file)


with open('menu.json') as file:
    try:
        menu_json = json.load(file)
        food_items = menu_json[month][day]
    except (KeyError, json.decoder.JSONDecodeError):
        dump_in_json()

print(food_items)
# configure smtp settings
with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
    connection.starttls()
    print('hi')
    connection.login(email, password)
    print('hi')
    connection.sendmail(from_addr=email,
                        to_addrs="sai.s.nallani@gmail.com",
                        msg=f"Subject:{day} Lunch Menu!\n\n{food_items}")