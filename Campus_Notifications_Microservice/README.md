# Campus Notifications Microservice

## Overview

This project is a backend assessment submission for the Campus Notifications Microservice. It includes registration, authentication, and notification retrieval functionalities using the provided APIs.

## Files

* `register.py` - User registration using the Registration API.
* `auth.py` - Authentication and access token generation.
* `stage6.py` - Fetches notifications from the Notification API and displays the top 10 notifications based on priority.
* `screenshots/` - Contains screenshots of API responses and program execution.

## Priority Logic

Notifications are prioritized as follows:

1. Placement
2. Result
3. Event

Notifications are sorted based on priority and recency (latest timestamp first), and the top 10 notifications are displayed.

## Technologies Used

* Python 3
* Requests Library
* Git & GitHub

## How to Run

Install dependencies:

```bash
pip install requests
```

Run the program:

```bash
python stage6.py
```

## Author

Srinidhi Akuthota
Roll No: 2303A51131
