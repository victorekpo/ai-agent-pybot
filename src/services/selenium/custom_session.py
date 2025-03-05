from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service


def custom_session():
    # Set up Chrome options to connect to the existing session
    options = Options()
    # l
    # chrome_options.add_argument("--remote-allow-origins=*")
    # chrome_options.add_argument('--remote-debugging-port=9222')
    # Run the following command in the terminal to start Chrome with remote debugging enabled, be sure to create a new user profile or it won't work
    # open -a "Google Chrome" --args --remote-debugging-port=9527 --user-data-dir=/Users/algorithm.v/Documents
    options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
    print("Connecting to new session...")

    # Initialize the WebDriver with the existing session
    chromedriver_path = '/Users/algorithm.v/Downloads/chromedriver/chromedriver'
    service = Service(executable_path=chromedriver_path)
    driver = webdriver.Chrome(service=service, options=options)
    driver.get("https://google.com")
    print("driver", driver)
    url = driver
    print("Url", url)
    session_id = driver.session_id
    print("Session Id", session_id)
    driver.get("https://aws.com")
    print("Connected to the existing session.")
