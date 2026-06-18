import requests

url = "http://4.224.186.213/evaluation-service/register"

data = {
    "email": "srinidhiakuthota24@gmail.com",
    "name": "Akuthota Srinidhi",
    "mobileNo": "7989449412",
    "githubUsername": "SrinidhiAkuthota",
    "rollNo": "2303A51131",
    "accessCode": "bDreAq"
}

response = requests.post(url, json=data)

print("Status Code:", response.status_code)
print("Response:", response.text)