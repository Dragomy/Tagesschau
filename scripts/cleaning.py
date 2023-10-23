import os 
import json
import pandas as pd


#Opens all jsons in the specified folder and packs them into a list for later use.
def load_and_list_jsons(dataframe, folder_path = './'):
    list_of_data_frames = []
    for filename in os.listdir(folder_path):
        if filename.endswith('.json'):
            file_path = os.path.join(folder_path, filename)
            with open(file_path, 'r') as json_file:
                print(file_path)
                data = json.load(json_file)['news']
                df_temp = pd.DataFrame.from_records(data)  # One file as DataFrame
                list_of_data_frames.append(df_temp)
                
    dataframe = pd.concat(list_of_data_frames, ignore_index=True)
    return dataframe


#Cleaning does several things:
#First we change how the date is displayed in our DataFrame 
#Second we filter out the videos so we know all NaN get some kind of validation
#Third we filter all left over regionIds (they are now most likely abroad news)
def clean_dataframe(dataframe):
    
    dataframe['date'] = pd.to_datetime(tmp_df['date'])
    
    tmp_index = dataframe['sophoraId'].str.contains("video")
    dataframe.loc[tmp_index, 'regionId'] = tmp_df.loc[tmp_index, 'regionId'].fillna(-1)
    
    dataframe.regionId = dataframe.regionId.fillna(-2)
    return dataframe


# WIP Should display duplicates in a dataframe if two criterias are met!
def show_duplicated(dataframe, crit1= 'sophoraId' , crit2= 'date')
    pass
    tmp = dataframe['sophoraId','date']
    dataframe.duplicated


# Special for sorting the Tag category which returns a list of dictionary at a point where only a list is needed
def clean_tags(line = 'tags'): 
    return [x['tag'] for x in zeile]
    