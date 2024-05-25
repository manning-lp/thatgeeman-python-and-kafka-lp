import requests

url = "https://www.manning.com/"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
    "Accept": "application/json",
}

response = requests.get(url, headers=headers)

with open("saved_page.html", "w", encoding="utf-8") as f:
    f.write(response.text)

print(f"Successfully saved {url} as saved_page.html")
