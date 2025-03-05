import json
import subprocess

from playwright.sync_api import sync_playwright


def read_jsonl(jsonl_file_path):
    actions_list = []
    with open(jsonl_file_path, 'r') as jsonl_file:
        for jsonl_line in jsonl_file:
            actions_list.append(json.loads(jsonl_line))
    return actions_list


def perform_action_with_locator(playwright_page, action_data, action_perform):
    selector = action_data.get('selector')
    if selector:
        element = playwright_page.locator(selector)
    else:
        element = playwright_page.locator(action_data['locator']['body'])
    action_perform(element, action_data)


def automate_actions(actions_list):
    with sync_playwright() as playwright:
        # browser_instance = playwright.chromium.connect_over_cdp("http://localhost:9222")
        browser_instance = playwright[actions_list[0]['browserName']].launch(**actions_list[0]['launchOptions'])
        browser_context = browser_instance.new_context(**actions_list[0].get('contextOptions', {}))
        playwright_page = browser_context.new_page()

        for action_data in actions_list[1:]:
            if action_data['name'] == 'openPage':
                playwright_page.goto(action_data['url'])
            elif action_data['name'] == 'navigate':
                playwright_page.goto(action_data['url'])
            elif action_data['name'] == 'click':
                perform_action_with_locator(playwright_page, action_data, lambda element, action: element.click(
                    button=action.get('button', 'left'),
                    modifiers=action.get('modifiers', []) if isinstance(action.get('modifiers', []), list) else [],
                    click_count=action.get('clickCount', 1)
                ))
            elif action_data['name'] == 'fill':
                perform_action_with_locator(playwright_page, action_data,
                                            lambda element, action: element.fill(action['text']))
            elif action_data['name'] == 'press':
                perform_action_with_locator(playwright_page, action_data, lambda element, action: element.press(
                    action['key']
                ))

        # playwright_page.pause()
        # browser_instance.close()
        input("Press Enter to close the browser...")


def start_chromium():
    subprocess.Popen(['chromium', '--remote-debugging-port=9222'])
