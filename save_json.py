import os
import requests
import datetime
import json


def get_json_data_from_api_request(folder_name='/home/dragomy/Tagesschau/News'):
    current_datetime = datetime.datetime.now()
    # Api Request
    api_url = "https://tagesschau.de/api2/news/"
    response = requests.get(api_url)

    #Save 
    if response.status_code == 200:
        news_data = response.json()
        json_name = f"News_{current_datetime.strftime('%Y-%m-%d_%H-%M-%S')}.json"
        with open(os.path.join(folder_name, json_name), "w") as news_file:
            news_file.write(json.dumps(news_data))

    else:
        print(f"Something went wrong")


if __name__ == '__main__':
    get_json_data_from_api_request()