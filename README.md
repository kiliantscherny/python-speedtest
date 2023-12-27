# Python Speedtest

A simple Python script to test your internet speed using [speedtest.net](https://www.speedtest.net/).

## Running the speedtest
- Clone the repository
- Ensure you have Docker and Docker Compose installed on your machine
- Choose the directory where you want to store the results of the speedtest as a `.db` file and change the volume directory in the `docker-compose.yml` file to that directory
- Run: `docker-compose up -d`
- The script will run once per minute and store the results in a `.db` file in the folder you specified above