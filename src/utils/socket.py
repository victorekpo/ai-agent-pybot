import requests
import socketio

# Constants
TOKEN = "1234567"

# Socket Connection
print("Connecting to Socket...")

client_name = "vicBot-pyBot"
token_url = "your_token_url"
socket_url = "http://localhost:3000"
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


def connect_socket():
    sio.connect(socket_url, transports=["websocket"], auth={"token": TOKEN},
                headers={"count": "0", "token": TOKEN})

# Uncomment the following line to start a counter if needed
# my_interval = sio.start_background_task(counter, sio)
