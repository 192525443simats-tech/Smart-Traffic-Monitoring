def analyze_traffic(vehicle_count):
    if vehicle_count <= 20:
        traffic_level = "LOW"
        green_time = 30
    elif vehicle_count <= 50:
        traffic_level = "MEDIUM"
        green_time = 45
    elif vehicle_count <= 80:
        traffic_level = "HIGH"
        green_time = 60
    else:
        traffic_level = "VERY HIGH"
        green_time = 90

    return traffic_level, green_time