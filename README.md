# Python Speedtest

A simple Python script to test your internet speed using [speedtest.net](https://www.speedtest.net/).

## Running the speedtest
- Clone the repository
- Ensure you have Docker installed on your machine
- Run: `docker build -t python-speedtest . && docker run -d -v /path/to/your/local/folder:/data python-speedtest`, where `/path/to/your/local/folder` is the path to the folder where you want to store the results of the speedtest as a `.db` file.
- The script will run once per minute and store the results in a `.db` file in the folder you specified above