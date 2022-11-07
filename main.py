import requests

url_ddg = "https://api.duckduckgo.com"

resp = requests.get(url_ddg + "/?q=DuckDuckGo&format=json")

rsp_data = resp.json()

print(str(rsp_data["RelatedTopics"]))

print(str(rsp_data["Heading"]))
