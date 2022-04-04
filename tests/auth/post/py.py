import requests


a = requests.request('POST', 'http://localhost:4002/')
print(a.status_code, a.text)