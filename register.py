import requests

url = "http://4.224.186.213/evaluation-service/register"

payload = {
    "email": "srinidhiakuthota@24gmail.com",
    "name": "Srinidhi Akuthota",
    "mobileNo": "7989449412",
    "githubUsername": "SrinidhiAkuthota",
    "rollNo": "2303A51131",
    "accessCode": "bDreAq"
}

response = requests.post(url, json=payload)

print(response.status_code)
print(response.json())