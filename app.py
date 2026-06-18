from flask import Flask, jsonify
from scheduler import generate_schedule

app = Flask(__name__)

@app.route("/")
def home():
    return "Vehicle Maintenance Scheduler API Running"

@app.route("/schedule")
def schedule():
    return jsonify(generate_schedule())

if __name__ == "__main__":
    app.run(debug=True)