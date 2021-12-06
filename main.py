import datetime
import pprint
import smtplib
from scraper import WebScraper
import json

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
day = dt.strftime("%A %-d")
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

with open('menu.json', 'r') as file:
  menu_json = json.load(file)
  food_items = menu_json[month][day]

#configure smtp settings
