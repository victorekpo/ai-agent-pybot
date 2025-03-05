from flask import Blueprint, jsonify, request

from src.services.selenium.automate import open_chrome, get_driver, load_json_data
from src.services.selenium.mappings import query_key_mapping
from src.services.selenium.run_actions import selenium_get_url
from src.services.selenium.run_commands import run_selenium_commands

sel_bp = Blueprint('sel', __name__)


@sel_bp.route('/open-chrome')
def open_chrome_driver():
    open_chrome()
    return jsonify("Opening Chrome")


@sel_bp.route('/get-driver')
def get_current_driver():
    result = get_driver()
    return jsonify("Driver: " + str(result))


@sel_bp.route('/get-url')
def get_url():
    url = request.args.get('url')
    driver = get_driver()
    selenium_get_url(driver, url)
    return jsonify("URL Get")


@sel_bp.route('/play')
def run_selenium_play():
    site = request.args.get('site')
    play = request.args.get('play')
    custom_values = {key[7:]: value for key, value in request.args.items() if key.startswith('custom_')}

    # Map custom values to command IDs
    custom_values_dict = None

    if custom_values:
        print("Received custom values:", custom_values)
        custom_values_dict = {}
        for key, value in custom_values.items():
            print("Key:", key, "Value:", value)
            # Convert key to command ID
            command_id = query_key_mapping.get(key)
            if command_id:
                print("Command ID:", command_id)
                custom_values_dict[command_id] = {'value': value}
                print("Custom Values Dict:", custom_values_dict)

    # start_chromium()
    file_path = 'plays/' + site + '/' + play + '.json'
    json_file = load_json_data(file_path)
    driver = get_driver()

    run_selenium_commands(driver, json_file, custom_values_dict)
    return jsonify("Selenium Action ran")
