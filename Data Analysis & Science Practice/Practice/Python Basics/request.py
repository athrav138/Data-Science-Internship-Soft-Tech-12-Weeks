import requests

data = requests.get("https://api.freeapi.app/api/v1/public/randomusers/user/random")
print(data)
#print(data.json())
data = data.json()
res = data["data"]["location"]["city"]
print(res)
