import requests
from logger import Log

TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJNYXBDbGFpbXMiOnsiYXVkIjoiaHR0cDovLzIwLjI0NC41Ni4xNDQvZXZhbHVhdGlvbi1zZXJ2aWNlIiwiZW1haWwiOiJzcmluaWRoaWFrdXRob3RhMjRAZ21haWwuY29tIiwiZXhwIjoxNzgxNzY4MDA3LCJpYXQiOjE3ODE3NjcxMDcsImlzcyI6IkFmZm9yZCBNZWRpY2FsIFRlY2hub2xvZ2llcyBQcml2YXRlIExpbWl0ZWQiLCJqdGkiOiJmOGU2M2Q4OS0wOTA1LTRkMjYtYTQyNy1hZDAxYWFkYTA5ZjMiLCJsb2NhbGUiOiJlbi1JTiIsIm5hbWUiOiJha3V0aG90YSBzcmluaWRoaSIsInN1YiI6IjNiMmE3YTFiLTFlZTItNDdmMi04OGRhLTUwMWY1ZjA5YWZhMyJ9LCJlbWFpbCI6InNyaW5pZGhpYWt1dGhvdGEyNEBnbWFpbC5jb20iLCJuYW1lIjoiYWt1dGhvdGEgc3JpbmlkaGkiLCJyb2xsTm8iOiIyMzAzYTUxMTMxIiwiYWNjZXNzQ29kZSI6ImJEcmVBcSIsImNsaWVudElEIjoiM2IyYTdhMWItMWVlMi00N2YyLTg4ZGEtNTAxZjVmMDlhZmEzIiwiY2xpZW50U2VjcmV0IjoiZ1VzeXRoUURBbXNIY3BXWCJ9.ge6Lhk1-fI82f3ygTdpHB3ZnGEwNU6NYyGsIXupjLAM"

headers = {
    "Authorization": f"Bearer {TOKEN}"
}

DEPOT_URL = "http://4.224.186.213/evaluation-service/depots"
VEHICLE_URL = "http://4.224.186.213/evaluation-service/vehicles"


def get_depots():
    response = requests.get(DEPOT_URL, headers=headers)

    if response.status_code != 200:
        Log("backend", "error", "scheduler",
            f"Failed to fetch depots: {response.text}")
        return []

    return response.json()["depots"]


def get_vehicles():
    response = requests.get(VEHICLE_URL, headers=headers)

    if response.status_code != 200:
        Log("backend", "error", "scheduler",
            f"Failed to fetch vehicles: {response.text}")
        return []

    return response.json()["vehicles"]


def knapsack(tasks, capacity):

    n = len(tasks)

    dp = [[0 for _ in range(capacity + 1)]
          for _ in range(n + 1)]

    for i in range(1, n + 1):

        duration = tasks[i - 1]["Duration"]
        impact = tasks[i - 1]["Impact"]

        for w in range(capacity + 1):

            if duration <= w:

                dp[i][w] = max(
                    dp[i - 1][w],
                    dp[i - 1][w - duration] + impact
                )

            else:
                dp[i][w] = dp[i - 1][w]

    selected_tasks = []

    w = capacity

    for i in range(n, 0, -1):

        if dp[i][w] != dp[i - 1][w]:

            selected_tasks.append(
                tasks[i - 1]["TaskID"]
            )

            w -= tasks[i - 1]["Duration"]

    selected_tasks.reverse()

    return {
        "TotalImpact": dp[n][capacity],
        "SelectedTasks": selected_tasks
    }


def generate_schedule():

    depots = get_depots()
    print("DEPOTS =", depots)

    vehicles = get_vehicles()
    print("VEHICLES =", vehicles)

    results = []

    for depot in depots:

        result = knapsack(
            vehicles,
            depot["MechanicHours"]
        )

        results.append({
            "DepotID": depot["ID"],
            "MechanicHours": depot["MechanicHours"],
            "TotalImpact": result["TotalImpact"],
            "SelectedTasks": result["SelectedTasks"]
        })

    return results

    for depot in depots:

        result = knapsack(
            vehicles,
            depot["MechanicHours"]
        )

        results.append({
            "DepotID": depot["ID"],
            "MechanicHours": depot["MechanicHours"],
            "TotalImpact": result["TotalImpact"],
            "SelectedTasks": result["SelectedTasks"]
        })

    Log(
        "backend",
        "info",
        "scheduler",
        "Schedule generation completed"
    )

    return results


if __name__ == "__main__":

    schedules = generate_schedule()

    for schedule in schedules:

        print("\nDepot ID:", schedule["DepotID"])
        print("Mechanic Hours:", schedule["MechanicHours"])
        print("Total Impact:", schedule["TotalImpact"])
        print("Selected Tasks:", schedule["SelectedTasks"])
if __name__ == "__main__":

    schedules = generate_schedule()

    print("Schedules:", schedules)