import subprocess
import sqlite3

# Run speedtest-cli command and capture output
speedtest_output = subprocess.run(
    ["speedtest-cli", "--csv"], capture_output=True, text=True
).stdout.strip()

print(speedtest_output)

# Extract values from CSV output
lines = speedtest_output.split("\n")
header = "Server ID,Sponsor,Server Name,Timestamp,Distance,Ping,Download,Upload,Share,IP Address"
values = lines[0]

# Parse CSV header and values
header_list = header.split(",")
values_list = values.split(",")

# Create dictionary for the results
result = {}
for i in range(len(header_list)):
    result[header_list[i]] = values_list[i]

# Extract necessary values
server_id = result.get("Server ID")
sponsor = result.get("Sponsor")
server_name = result.get("Server Name")
timestamp = result.get("Timestamp")
distance = result.get("Distance")
ping = result.get("Ping")
download_speed = result.get("Download")
upload_speed = result.get("Upload")
share = result.get("Share")
ip_address = result.get("IP Address")

# Connect to SQLite database
conn = sqlite3.connect("/data/speedtest_results.db")
cursor = conn.cursor()

# Create a table if it doesn't exist
cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS speedtest_results (
        id INTEGER PRIMARY KEY,
        server_id INTEGER,
        sponsor TEXT,
        server_name TEXT,
        timestamp TEXT,
        distance REAL,
        ping REAL,
        download_speed REAL,
        upload_speed REAL,
        share TEXT,
        ip_address TEXT
    )
"""
)

# Insert the speed test results into the database
cursor.execute(
    """
    INSERT INTO speedtest_results (
        server_id,
        sponsor,
        server_name,
        timestamp,
        distance,
        ping,
        download_speed,
        upload_speed,
        share,
        ip_address
    )
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
""",
    (
        server_id,
        sponsor,
        server_name,
        timestamp,
        distance,
        ping,
        download_speed,
        upload_speed,
        share,
        ip_address,
    ),
)

# Commit changes and close connection
conn.commit()
conn.close()
