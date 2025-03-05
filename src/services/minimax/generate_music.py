import requests

url = "https://api.minimaxi.chat/v1/music_upload"

api_key = 'apiKey'
file_name = 'audio file name'
file_path = 'audio file path'

payload = {
    'purpose': 'song'
}
files = [
    ('file', (file_name, open(file_path, 'rb'), 'audio/mpeg'))
]
headers = {
    'authorization': 'Bearer ' + api_key,
}

response = requests.request("POST", url, headers=headers, data=payload, files=files)
print(response.headers.get('Trace-Id'))
print(response.text)
