import requests
url = "https://manning.com"
response = requests.request("GET", url)
print(response.text)