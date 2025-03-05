from selenium.webdriver.common.action_chains import ActionChains

from src.services.selenium.find_element import find_element
from src.services.selenium.mappings import special_keys_map


def run_selenium_commands(driver, json_data, custom_values_dict=None):
    print("Running Selenium commands...")
    print("Current Driver", driver)
    driver.get(json_data['url'])

    for test in json_data['tests']:
        for command in test['commands']:
            if command['command'] == 'open':
                driver.get(json_data['url'] + command['target'])
            elif command['command'] == 'setWindowSize':
                width, height = map(int, command['target'].split('x'))
                driver.set_window_size(width, height)
            elif command['command'] == 'click':
                element = find_element(driver, command['targets'])
                element.click()
            elif command['command'] == 'mouseOver':
                element = find_element(driver, command['targets'])
                ActionChains(driver).move_to_element(element).perform()
            elif command['command'] == 'mouseOut':
                ActionChains(driver).move_by_offset(10, 10).perform()
            elif command['command'] == 'type':
                element = find_element(driver, command['targets'])
                value = command['value']
                if custom_values_dict and command['id'] in custom_values_dict:
                    print("Overriding type command value with custom value", custom_values_dict[command['id']],
                          "default value was",
                          value)
                    value = custom_values_dict[command['id']].get('value', value)
                element.send_keys(value)
            elif command['command'] == 'sendKeys':
                element = find_element(driver, command['targets'])
                value = command['value']
                if custom_values_dict and command['id'] in custom_values_dict:
                    print("Overriding sendKeys command value with custom value", custom_values_dict[command['id']],
                          "default value was",
                          value)
                    value = custom_values_dict[command['id']].get('value', value)
                # Check if value is a special key
                if value in special_keys_map:
                    print("Special key found", value)
                    value = special_keys_map[value]
                element.send_keys(value)

    # input("Press Enter to close the browser...")
    # driver.quit()
