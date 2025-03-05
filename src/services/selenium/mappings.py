from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

element_type_map = {
    "class": By.CLASS_NAME,
    "css": By.CSS_SELECTOR,
    "id": By.ID,
    "link": By.LINK_TEXT,
    "name": By.NAME,
    "partial": By.PARTIAL_LINK_TEXT,
    "tag": By.TAG_NAME,
    "xpath": By.XPATH
}

special_keys_map = {
    "${KEY_ENTER}": Keys.ENTER,
    "${KEY_TAB}": Keys.TAB,
    "${KEY_SPACE}": Keys.SPACE,
    "${KEY_BACKSPACE}": Keys.BACKSPACE,
    "${KEY_DELETE}": Keys.DELETE,
    "${KEY_ESCAPE}": Keys.ESCAPE,
    "${KEY_UP}": Keys.ARROW_UP,
    "${KEY_DOWN}": Keys.ARROW_DOWN,
    "${KEY_LEFT}": Keys.ARROW_LEFT,
    "${KEY_RIGHT}": Keys.ARROW_RIGHT,
    "${KEY_HOME}": Keys.HOME,
    "${KEY_END}": Keys.END,
    "${KEY_PAGE_UP}": Keys.PAGE_UP,
    "${KEY_PAGE_DOWN}": Keys.PAGE_DOWN,
    "${KEY_INSERT}": Keys.INSERT,
    "${KEY_F1}": Keys.F1,
    "${KEY_F2}": Keys.F2,
    "${KEY_F3}": Keys.F3,
    "${KEY_F4}": Keys.F4,
    "${KEY_F5}": Keys.F5,
    "${KEY_F6}": Keys.F6,
    "${KEY_F7}": Keys.F7,
    "${KEY_F8}": Keys.F8,
    "${KEY_F9}": Keys.F9,
    "${KEY_F10}": Keys.F10,
    "${KEY_F11}": Keys.F11,
    "${KEY_F12}": Keys.F12,
}

query_key_mapping = {
    'google_search': 'e9c387ac-6d73-4c7b-99c1-7d7fa297e276',
}
