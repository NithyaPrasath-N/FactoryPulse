"""
Seed database with demo machines, sensors, users, and telemetry.
Run after infrastructure is up: make seed
"""

import psycopg2
import os
import random
from datetime import datetime

# Database connection config
DB_CONFIG = {
    "host": os.getenv("DB_HOST", "localhost"),
    "dbname": os.getenv("DB_NAME", "factorypulse"),
    "user": os.getenv("DB_USER", "factorypulse"),
    "password": os.getenv("DB_PASS", "fp_dev_2024"),
}

# Demo machines
MACHINES = [
    ("CNC-07", "CNC_Mill", "Plant-A / Bay-3", "2021-03-15"),
    ("CNC-12", "CNC_Mill", "Plant-A / Bay-5", "2020-08-22"),
    ("TURB-01", "Turbofan", "Plant-B / Engine-Bay", "2019-11-01"),
    ("TURB-02", "Turbofan", "Plant-B / Engine-Bay", "2020-02-14"),
    ("BRG-04", "Bearing_Rig", "Plant-A / Test-Lab", "2022-01-10"),
    ("PUMP-09", "Centrifugal_Pump", "Plant-C / Utility", "2021-07-20"),
]

# Demo sensor types
SENSOR_TYPES = [
    ("temperature", "C", -40.0, 400.0),
    ("vibration", "mm/s", 0.0, 50.0),
    ("pressure", "bar", 0.0, 500.0),
    ("rpm", "RPM", 0.0, 50000.0),
    ("current", "A", 0.0, 200.0),
]

# Demo users
USERS = [
    ("tech_arun", "technician", "Arun Kumar"),
    ("eng_priya", "engineer", "Priya Sharma"),
    ("mgr_raj", "manager", "Raj Patel"),
    ("ds_meera", "data_scientist", "Meera Nair"),
    ("admin_sys", "admin", "System Admin"),
]


def seed():
    """Insert demo data into all tables."""
    conn = psycopg2.connect(**DB_CONFIG)
    cur = conn.cursor()

    try:
        # Seed machines
        for machine_id, machine_class, location, install_date in MACHINES:
            cur.execute("""
                INSERT INTO machines (machine_id, machine_class, location, install_date)
                VALUES (%s, %s, %s, %s)
                ON CONFLICT (machine_id) DO NOTHING
            """, (machine_id, machine_class, location, install_date))

        # Seed sensors (5 per machine)
        for machine_id, machine_class, _, _ in MACHINES:
            for sensor_type, unit, lo, hi in SENSOR_TYPES:
                sensor_id = f"{machine_id}_{sensor_type}"
                cur.execute("""
                    INSERT INTO sensors (sensor_id, machine_id, sensor_type, unit, min_valid, max_valid)
                    VALUES (%s, %s, %s, %s, %s, %s)
                    ON CONFLICT (sensor_id) DO NOTHING
                """, (sensor_id, machine_id, sensor_type, unit, lo, hi))

                # Insert one demo telemetry row per sensor
                value = round(random.uniform(lo, hi), 2)
                cur.execute("""
                    INSERT INTO telemetry (sensor_id, ts, value)
                    VALUES (%s, %s, %s)
                """, (sensor_id, datetime.utcnow(), value))

        # Seed users (bcrypt hash of 'password123' — demo only!)
        demo_hash = "$2b$12$LJ3m12345...xyzABCDE"
        for username, role, full_name in USERS:
            cur.execute("""
                INSERT INTO users (username, password_hash, role, full_name)
                VALUES (%s, %s, %s, %s)
                ON CONFLICT (username) DO NOTHING
            """, (username, demo_hash, role, full_name))

        conn.commit()
        print(f"✅ Seeded {len(MACHINES)} machines, "
              f"{len(MACHINES)*len(SENSOR_TYPES)} sensors, "
              f"{len(USERS)} users, plus demo telemetry.")

    finally:
        cur.close()
        conn.close()


if __name__ == "__main__":
    seed()
