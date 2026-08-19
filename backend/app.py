from flask import Flask, request, jsonify
from flask_cors import CORS
from traffic_analysis import analyze_traffic
from database import init_db, save_traffic_record

app = Flask(__name__)
CORS(app)

init_db()


@app.route("/")
def home():
    return "Smart Traffic Monitoring System is running!"


@app.route("/analyze", methods=["POST"])
def analyze():
       data = request.get_json()

if not data or "vehicle_count" not in data:
    return jsonify({"error": "vehicle_count is required"}), 400

try:
    vehicle_count = int(data["vehicle_count"])
except (ValueError, TypeError):
    return jsonify({"error": "vehicle_count must be a number"}), 400

if vehicle_count < 0:
    return jsonify({"error": "vehicle_count cannot be negative"}), 400

    traffic_level, green_time = analyze_traffic(vehicle_count)

    save_traffic_record(
        vehicle_count,
        traffic_level,
        green_time
    )

    return jsonify({
        "vehicle_count": vehicle_count,
        "traffic_level": traffic_level,
        "green_time": green_time
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)