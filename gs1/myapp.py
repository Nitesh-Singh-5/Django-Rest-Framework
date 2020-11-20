import requests

URL = "http://localhost:8000/stuinfo/"
r = requests.get(url =URL)
data = r.json()
print(data) 