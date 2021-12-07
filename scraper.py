from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
import time



class WebScraper():
    def __init__(self):
        time.sleep(1)
        url = "file:///C:/Users/saisn/Downloads/Menu%20Calendar.html"
        driver = webdriver.Chrome("C:/02-Happy/chromedriver.exe")
        driver.get(url)
        time.sleep(1)

    def set_parameters(self, school_value, month, menu):
        school_selection = Select(driver.find_element(By.XPATH, (
            "/html/body/form/div[6]/div[4]/div[2]/div[2]/div[2]/div/div/div[1]/div[1]/select")))
        school_selection.select_by_value(school_value)
        month_selection = Select(driver.find_element(By.XPATH, '//*[@id="MainContent_DdlMenuMonth"]'))
        month_selection.select_by_visible_text(month)
        menu_selection = Select(driver.find_element(By.XPATH, '//*[@id="MainContent_DdlMealPeriod"]'))
        menu_selection.select_by_visible_text(menu)

    def scrape_all(self):
        dates = [date.text for date in driver.find_elements(By.CSS_SELECTOR, ".menu-date")]
        items = [item for item in driver.find_elements(By.CSS_SELECTOR, ".calendar ul.menu.item.dropdown")]
        return dates, items

    def quit(self):
        driver.quit()
