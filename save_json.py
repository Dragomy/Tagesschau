import os
import requests
import datetime
import json
import click
from raspberry_pi_mail import sendmail

@click.command()
@click.option('--path', default='/home/dragomy/Tagesschau/News', 
                        help='Defines the path to save the gathered data.')
def get_json_data_from_api_request(path):
    current_datetime = datetime.datetime.now()
    # Api Request
    api_url = "https://tagesschau.de/api2/news/"
    response = requests.get(api_url)

    #Save 
    if response.status_code == 200:
        news_data = response.json()
        json_name = f"News_{current_datetime.strftime('%Y-%m-%d_%H-%M-%S')}.json"
        with open(os.path.join(path, json_name), "w") as news_file:
            news_file.write(json.dumps(news_data))
    else:
        raise Exception("Wrong Status Code:" + response.status_code)


if __name__ == '__main__':
    try:
        get_json_data_from_api_request()  
    except Exception as e: 
        subject = "A Problem in your current Pi Project"
        content =  str(e)
        sendmail(subject, content)