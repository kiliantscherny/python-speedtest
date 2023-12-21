FROM python:3.9

# Install cron, speedtest-cli, and any other necessary packages
RUN apt-get update && \
    apt-get install -y cron && \
    apt-get install -y speedtest-cli

# Set working directory
WORKDIR /app

# Copy files into the container
COPY speedtest.py /app
COPY crontab /etc/cron.d/speedtest-cron

# Specify the volume to store the database file
VOLUME /data

# Give execution rights to the cron job
RUN chmod 0644 /etc/cron.d/speedtest-cron

# Create a log file for cron output
RUN touch /var/log/cron.log

# Apply the cron job
RUN crontab /etc/cron.d/speedtest-cron

# Start cron in the foreground
CMD cron && tail -f /var/log/cron.log
