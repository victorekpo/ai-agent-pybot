import json

from selenium import webdriver
from selenium.common import NoSuchWindowException

# Define driver globally in order to reuse it
chrome_driver = None


def load_json_data(file_path):
    print("Loading data from", file_path)
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data


def open_chrome():
    print("Initializing chrome driver, opening chrome")
    global chrome_driver
    chrome_driver = webdriver.Chrome()
    chrome_driver.get("https://google.com")
    return chrome_driver


def get_driver(debug=False):
    print("Current chrome driver", chrome_driver)
    if chrome_driver is None and debug is False:
        print("Driver is not initialized")
        return open_chrome()

    try:
        chrome_driver.current_window_handle
    except NoSuchWindowException:
        print("Target window already closed, reopening chrome")
        return open_chrome()

    return chrome_driver
