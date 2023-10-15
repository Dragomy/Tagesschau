import os
import json
import matplotlib.pyplot as plt

folder_path = 'News' 

for filename in os.listdir(folder_path):
    if filename.endswith('.json'):
        file_path = os.path.join(folder_path, filename)
        with open(file_path, 'r') as json_file:
            try:
                data = json.load(json_file)

                #Get Value of Tag x
                for item in data["news"]:
                  regionId = item.get("regionId")
                  geotags = item.get("geotags")
                  
                #Do something with gathered items:
                  print(regionId,geotags)
                
            except json.JSONDecodeError as e:
                print(f"Error loading JSON from {filename}: {e}")


