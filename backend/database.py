import os
import sqlite3

DATABASE = "/app/database/traffic.db"


def init_db():
    os.makedirs("/app/database", exist_ok=True)

    connection = sqlite3.connect(DATABASE)

    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS traffic_records (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            vehicle_count INTEGER NOT NULL,
            traffic_level TEXT NOT NULL,
            green_time INTEGER NOT NULL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    """)

    connection.commit()
    connection.close()


def save_traffic_record(vehicle_count, traffic_level, green_time):
    connection = sqlite3.connect(DATABASE)

    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO traffic_records
        (vehicle_count, traffic_level, green_time)
        VALUES (?, ?, ?)
    """, (vehicle_count, traffic_level, green_time))

    connection.commit()
    connection.close()


def get_traffic_records():
    connection = sqlite3.connect(DATABASE)

    cursor = connection.cursor()

    cursor.execute("""
        SELECT id, vehicle_count, traffic_level, green_time, timestamp
        FROM traffic_records
        ORDER BY id DESC
    """)

    records = cursor.fetchall()

    connection.close()

    return records