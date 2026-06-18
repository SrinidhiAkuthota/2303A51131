import requests

url = "http://4.224.186.213/evaluation-service/auth"

data = {
    "email": "srinidhiakuthota24@gmail.com",
    "name": "akuthota srinidhi",
    "rollNo": "2303a51131",
    "accessCode": "bDreAq",
    "clientID": "3b2a7a1b-1ee2-47f2-88da-501f5f09afa3",
    "clientSecret": "gUsythQDAmsHcpWX"
}

response = requests.post(url, json=data)

print("Status Code:", response.status_code)
print("Response:", response.text)