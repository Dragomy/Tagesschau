# Tagesschau-Mining

This project uses the Web API of Germany's public news service "Tagesschau." It was originally created as a self-introduction for Data Science/Analysis. Later, I extended its use for a school project.

Some of the scripts contain links to the sources, but I cannot guarantee they will work in the future.

## Installation
1. Clone the repository to a Raspberry Pi or alternative device.
2. Set up Cron; the standard Raspberry Pi OS has Cron preinstalled. Access it using `sudo crontab -e`.
   Enter how often you want to request articles. Please refer to the rules defined by: https://tagesschau.api.bund.dev/
   If you have never worked with Cron before, refer to this: https://crontab.guru/
   Here is an example that sends a request every 5 minutes:
   `*/5 * * * * /usr/bin/python path_to_project/tagesschau/save_json.py`
3. That's it! You will now receive Tagesschau news every {specified timeframe}.