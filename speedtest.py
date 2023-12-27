import subprocess
import json
import sqlite3

# Run speedtest-cli command and capture output as JSON
speedtest_output = subprocess.run(
    ["speedtest-cli", "--json"], capture_output=True, text=True
).stdout.strip()

print(speedtest_output)

# Parse JSON output
speedtest_data = json.loads(speedtest_output)

# Extract necessary values
download_speed = speedtest_data.get("download")
upload_speed = speedtest_data.get("upload")
ping = speedtest_data.get("ping")

server = speedtest_data.get("server", {})

server_url = server.get("url")
server_lat = server.get("lat")
server_lon = server.get("lon")
server_name = server.get("name")
server_country = server.get("country")
server_cc = server.get("cc")
server_sponsor = server.get("sponsor")
server_id = server.get("id")
server_host = server.get("host")
server_distance = server.get("d")
server_latency = server.get("latency")

timestamp = speedtest_data.get("timestamp")
bytes_sent = speedtest_data.get("bytes_sent")
bytes_received = speedtest_data.get("bytes_received")
share = speedtest_data.get("share")

client = speedtest_data.get("client", {})

client_ip = client.get("ip")
client_lat = client.get("lat")
client_lon = client.get("lon")
client_isp = client.get("isp")
client_isprating = client.get("isprating")
client_rating = client.get("rating")
client_ispdlavg = client.get("ispdlavg")
client_ispulavg = client.get("ispulavg")
client_loggedin = client.get("loggedin")
client_country = client.get("country")

# Connect to SQLite database
conn = sqlite3.connect("/data/speedtest_results.db")
cursor = conn.cursor()

# Create a table if it doesn't exist
cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS speedtest_results_table (
        id INTEGER PRIMARY KEY,
        download_speed REAL,
        upload_speed REAL,
        ping REAL,
        server_url TEXT,
        server_lat REAL,
        server_lon REAL,
        server_name TEXT,
        server_country TEXT,
        server_cc TEXT,
        server_sponsor TEXT,
        server_id INTEGER,
        server_host TEXT,
        server_distance REAL,
        server_latency REAL,
        timestamp TEXT,
        bytes_sent INTEGER,
        bytes_received INTEGER,
        share TEXT,
        client_ip TEXT,
        client_lat REAL,
        client_lon REAL,
        client_isp TEXT,
        client_isprating REAL,
        client_rating REAL,
        client_ispdlavg REAL,
        client_ispulavg REAL,
        client_loggedin TEXT,
        client_country TEXT
    )
"""
)

# Insert the speed test results into the database
cursor.execute(
    """
    INSERT INTO speedtest_results_table (
        download_speed,
        upload_speed,
        ping,
        server_url,
        server_lat,
        server_lon,
        server_name,
        server_country,
        server_cc,
        server_sponsor,
        server_id,
        server_host,
        server_distance,
        server_latency,
        timestamp,
        bytes_sent,
        bytes_received,
        share,
        client_ip,
        client_lat,
        client_lon,
        client_isp,
        client_isprating,
        client_rating,
        client_ispdlavg,
        client_ispulavg,
        client_loggedin,
        client_country
    )
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
""",
    (
        download_speed,
        upload_speed,
        ping,
        server_url,
        server_lat,
        server_lon,
        server_name,
        server_country,
        server_cc,
        server_sponsor,
        server_id,
        server_host,
        server_distance,
        server_latency,
        timestamp,
        bytes_sent,
        bytes_received,
        share,
        client_ip,
        client_lat,
        client_lon,
        client_isp,
        client_isprating,
        client_rating,
        client_ispdlavg,
        client_ispulavg,
        client_loggedin,
        client_country,
    ),
)

# Commit changes and close connection
conn.commit()
conn.close()
