
import requests
playlist_url = 'https://youtube.com/playlist?list=PL-fS1RGo6L5u2OlEF5n4mO845_AJJZMZ_&si=0fXFzgXQoztpnZHm'
response = requests.get(playlist_url)
response.raise_for_status()  # Raise an error for bad HTTP responses
html = response.text
print(html)
