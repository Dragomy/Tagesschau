import os
import gzip
import json
import pandas as pd

# Opens a Json file and writes the data into a dataframe
def load_json(file_path):
    with open(file_path, 'r') as json_file:
        data = json.load(json_file)['news']
        df_temp = pd.DataFrame.from_records(data)
        return df_temp
    

# Opens a GZipped Json file and writes the data into a dataframe
def load_gzip(file_path):
    with gzip.open(file_path, 'rt') as gzipped_json_file:
        data = json.load(gzipped_json_file)['news']
        df_temp = pd.DataFrame.from_records(data)
        return df_temp
    

# Writes data from different files into one dataframe
def data_to_dataframe(folder_path='News'):
    list_of_data_frames = []
    
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        
        if filename.endswith('.json'):
            list_of_data_frames.append(load_json(file_path))
                
        elif filename.endswith('.json.gz'):
            list_of_data_frames.append(load_gzip(file_path))
                
    print('Process finished')
    return pd.concat(list_of_data_frames, ignore_index=True)

# This is how to use it:
# df = data_to_dataframe()
# Who would have thought