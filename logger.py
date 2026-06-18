import requests

TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJNYXBDbGFpbXMiOnsiYXVkIjoiaHR0cDovLzIwLjI0NC41Ni4xNDQvZXZhbHVhdGlvbi1zZXJ2aWNlIiwiZW1haWwiOiJzcmluaWRoaWFrdXRob3RhMjRAZ21haWwuY29tIiwiZXhwIjoxNzgxNzY1ODkwLCJpYXQiOjE3ODE3NjQ5OTAsImlzcyI6IkFmZm9yZCBNZWRpY2FsIFRlY2hub2xvZ2llcyBQcml2YXRlIExpbWl0ZWQiLCJqdGkiOiJjNTc0NTlkYi1iN2Q0LTQ4MmUtYTk0ZS0xY2ExZTA1M2NkNjgiLCJsb2NhbGUiOiJlbi1JTiIsIm5hbWUiOiJha3V0aG90YSBzcmluaWRoaSIsInN1YiI6IjNiMmE3YTFiLTFlZTItNDdmMi04OGRhLTUwMWY1ZjA5YWZhMyJ9LCJlbWFpbCI6InNyaW5pZGhpYWt1dGhvdGEyNEBnbWFpbC5jb20iLCJuYW1lIjoiYWt1dGhvdGEgc3JpbmlkaGkiLCJyb2xsTm8iOiIyMzAzYTUxMTMxIiwiYWNjZXNzQ29kZSI6ImJEcmVBcSIsImNsaWVudElEIjoiM2IyYTdhMWItMWVlMi00N2YyLTg4ZGEtNTAxZjVmMDlhZmEzIiwiY2xpZW50U2VjcmV0IjoiZ1VzeXRoUURBbXNIY3BXWCJ9.yjStQrjZx0SR4bEURG7sggfgw22OtVhyIvxbwaPRKgo"

LOG_URL = "http://4.224.186.213/evaluation-service/logs"

def Log(stack, level, package, message):

    headers = {
        "Authorization": f"Bearer {TOKEN}",
        "Content-Type": "application/json"
    }

    data = {
        "stack": stack,
        "level": level,
        "package": package,
        "message": message
    }

    response = requests.post(
        LOG_URL,
        json=data,
        headers=headers
    )

    return response.json()
if __name__ == "__main__":
    result = Log(
        "backend",
        "info",
        "scheduler",
        "Testing logging middleware"
    )

    print(result)