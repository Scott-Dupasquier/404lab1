import requests

print(requests.__version__)

google = requests.get("http://www.google.com")
print(google)

var = requests.get()

print(var.content)