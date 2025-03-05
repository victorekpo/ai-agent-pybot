from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


def find_element(driver, targets):
    if not targets:
        raise Exception("No targets provided")

    for target in targets:
        by, value = target[0].split('=', 1)
        print(f"Trying to find element by {by} with value {value}")
        try:
            if by == 'css':
                element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, value)))
                try:
                    element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, value)))
                    print("CSS Element clickable")
                except:
                    pass
            elif by == 'xpath':
                element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, value)))
                try:
                    element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, value)))
                    print("Xpath Element clickable")
                except:
                    pass
            elif by == 'id':
                element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, value)))
                try:
                    element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, value)))
                    print("ID Element clickable")
                except:
                    pass
            elif by == 'name':
                element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, value)))
                try:
                    element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME, value)))
                    print("Name Element clickable")
                except:
                    pass
            else:
                print(f"Unknown selector type: {by}")
                continue

            print(f"Element found: {element}")
            return element
        except Exception as e:
            print(f"Failed to find element by {by} with value {value}: {e}")
            continue

    raise Exception("No valid selector found")
