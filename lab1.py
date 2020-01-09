import requests

print(requests.__version__)

google = requests.get("http://www.google.com")
print(google)

var = requests.get("https://raw.githubusercontent.com/Scott-Dupasquier/404lab1/master/lab1.py")

print(var.content)