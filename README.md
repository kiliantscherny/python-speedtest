# Python Speedtest

A simple Dockerized app to test and log your internet speed using [speedtest.net](https://www.speedtest.net/).

By default, the script will run once per minute and test your internet speed.

The results are saved and persisted in a SQLite database on the host machine, so you can easily query and analyse the results.

## Running the speedtest
0. Ensure you have Docker and Docker Compose installed on your machine
1. Clone this repository
2. Choose the directory where you want to store the results of the speedtest file and change the volume directory in the `docker-compose.yml` file to that directory
3. Run: `docker-compose up -d` to start the container

The script will run once per minute and store the results in a `.db` file in the folder you specified above.

You can view the results of the SQLite database table by (for example):
- Using the SQLite CLI
- Using a GUI tool like DB Browser for SQLite, DataGrip, etc.
- Using a Python script to query the database

To stop the script, run: `docker-compose down`.