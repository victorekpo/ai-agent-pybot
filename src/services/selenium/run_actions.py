from selenium.webdriver.common.by import By

from src.services.selenium.mappings import element_type_map
from src.services.selenium.mappings import special_keys_map


def selenium_get_url(driver, url):
    print("Received URL: ", url)
    # Check if URL has schema, if not use default schema https://
    if url.startswith("80:"):
        url = url.replace("80:", "http://")

    if not url.startswith("http"):
        url = "https://" + url

    print("Navigating to URL: ", url)
    driver.get(url)


def selenium_send_key(driver, element="input", element_type="tag", key=""):
    if key in special_keys_map:
        key = special_keys_map[key]

    if element_type in element_type_map:
        element_type = element_type_map[element_type]
    else:
        print("Element type not found, using default By.TAG_NAME")
        element_type = By.TAG_NAME

    driver.find_element(element_type, element).send_keys(key)
