from raspberry_pi_mail import sendmail
import datetime
import requests
import click
import json
import gzip
import os

@click.command()
@click.option('--path', default='News', help='Defines the path to save the gathered data.')
def get_json_data_from_api_request(path):
    current_datetime = datetime.datetime.now()

    # Api Request
    api_url = "https://tagesschau.de/api2/news/"
    response = requests.get(api_url)

    # Save as Gzipped JSON
    if response.status_code == 200:
        news_data = response.json()
        json_name = f"News_{current_datetime.strftime('%Y-%m-%d_%H-%M-%S')}.json.gz"
        with gzip.open(os.path.join(path, json_name), "wb") as news_file:
            news_file.write(json.dumps(news_data).encode('utf-8'))
    else:
        raise Exception("Wrong Status Code: " + str(response.status_code))


if __name__ == '__main__':
    try:
        get_json_data_from_api_request()
    except Exception as e:
        pass
        subject = "A Problem in your current Pi Project"
        content = str(e)
        sendmail(subject, content)
