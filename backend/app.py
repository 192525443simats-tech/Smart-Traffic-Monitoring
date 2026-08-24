from flask import Flask, jsonify, request
from flask_cors import CORS

from database import init_db, save_traffic_record, get_traffic_records


app = Flask(__name__)
CORS(app)


# Home route
@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "message": "Smart Traffic Monitoring Backend is running"
    })


# Get all traffic data
@app.route("/data", methods=["GET"])
def get_data():
    records = get_traffic_records()

    data = []

    for record in records:
        data.append({
            "id": record[0],
            "vehicle_count": record[1],
            "traffic_level": record[2],
            "green_time": record[3],
            "timestamp": record[4]
        })

    return jsonify(data)


# Add traffic data
@app.route("/traffic", methods=["POST"])
def add_traffic():
    data = request.get_json()

    if not data or "vehicle_count" not in data:
        return jsonify({
            "error": "vehicle_count is required"
        }), 400

    vehicle_count = int(data["vehicle_count"])

    # Decide traffic level and signal time
    if vehicle_count <= 20:
        traffic_level = "Low"
        green_time = 30

    elif vehicle_count <= 50:
        traffic_level = "Medium"
        green_time = 45

    else:
        traffic_level = "High"
        green_time = 60

    # Save data into SQLite database
    save_traffic_record(
        vehicle_count,
        traffic_level,
        green_time
    )

    return jsonify({
        "message": "Traffic record saved successfully",
        "vehicle_count": vehicle_count,
        "traffic_level": traffic_level,
        "green_time": green_time
    }), 201


# Start application
if __name__ == "__main__":
    init_db()

    app.run(
        host="0.0.0.0",
        port=5000,
        debug=False
    )