import requests
import socketio

from src.agents.vic_bot import vic_bot_1
from src.services.selenium.automate import get_driver
from src.services.selenium.run_actions import selenium_get_url, selenium_send_key

# Constants
TOKEN = "1234567"
APIKEY = "nancyvic"

# Socket Connection
print("Connecting to Socket...")

client_name = "vicBot-pyBot"
token_url = "your_token_url"
socket_url = "http://localhost:3000"  # "https://bot.teknixco.net"  # "http://localhost:3000"
current_token = "noToken"
my_interval = None


def update_token():
    global current_token
    try:
        #  res = requests.get(token_url, headers={"apikey": os.getenv("APP_KEY")})
        #  current_token = res.text
        #  return res.text
        current_token = TOKEN
        return current_token
    except requests.RequestException as err:
        print(err)
        return "error"


# Initialize App
update_token()
sio = socketio.Client()
print(f"Current Token: {current_token}")


@sio.event
def connect():
    print(f"{client_name} has connected")
    sio.emit("newClientPy", {"token": update_token(), "clientName": client_name, "group": "py-bots-ai-agents"})


@sio.event
def connect_error(err):
    print(f"{client_name} has a connection error, {err}")
    if my_interval:
        my_interval.cancel()


@sio.event
def disconnect():
    print(f"{client_name} has disconnected")
    if my_interval:
        my_interval.cancel()


@sio.event
def invalidToken(args):
    print(args)
    update_token()


@sio.event
def message(data):
    print("Received 'message' event with data:", data)
    response = vic_bot_1.ask(data)
    sio.emit("message-reply", response)


@sio.event
def browser(data):
    print("Received 'browser' event with data:", data)
    driver = get_driver()
    selenium_get_url(driver, data)
    sio.emit("message-reply", "Browser opened url" + data)


@sio.event
def send_key(data):
    print("Received 'send_key' event with data:", str(data), type(data))
    element = data.get('element')
    element_type = data.get('elementType')
    key_to_send = data.get('sendKey')

    driver = get_driver()
    selenium_send_key(driver, element, element_type, key_to_send)
    sio.emit("message-reply", "Key sent" + str(data))


@sio.on('*')
def catch_all(event, data):
    print(f"Received generic event '{event}' with data: {data}")


def get_sio():
    return sio


def connect_socket():
    print("socket url", socket_url)
    sio.connect(socket_url, transports=["websocket"], auth={"token": TOKEN},
                headers={"count": "0", "token": TOKEN})
    return sio

# Uncomment the following line to start a counter if needed
# my_interval = sio.start_background_task(counter, sio)
