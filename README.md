# Vehicle Maintenance Scheduler

## Objective

Develop a backend service that maximizes maintenance impact while respecting depot mechanic-hour constraints.

## Technologies Used

* Python
* Flask
* Requests

## Algorithm

The solution uses the 0/1 Knapsack Dynamic Programming algorithm to select maintenance tasks that maximize total impact without exceeding available mechanic hours.

## API Endpoints

### GET /schedule

Returns optimized maintenance schedules for all depots.

## Logging Middleware

A reusable logging middleware is implemented using the provided logging API. Logs are generated for:

* Fetching depot data
* Fetching vehicle data
* Running optimization
* Schedule generation completion

## Running the Project

Install dependencies:

pip install -r requirements.txt

Run:

python app.py
