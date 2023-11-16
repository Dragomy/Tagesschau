import pandas as pd

# If you work with dataframes first do this:
# pd.set_option('display.max_columns', None)
# Never ever display all rows
# We need a good option to drop duplicates but 
# thats a datapoint we could look at later
# df_dropped = df.drop_duplicates(subset = 'sophoraId', keep = 'first')


# Drops collumns i dont know what to do with
def drop_useless_columns(tmp_df):
    columns_to_remove = ['teaserImage',
                         'tracking',
                         'brandingImage',
                         'updateCheckUrl', 
                         'details', 
                         'detailsweb', 
                         'shareURL', 
                         'streams', 
                         'comments']
    tmp_df = tmp_df.drop(columns=columns_to_remove) 
    return tmp_df


#All dates to one Format
def clean_date(tmp_df):
    tmp_df['date'] = pd.to_datetime(tmp_df['date'])
    return tmp_df


# Makes a list out of a dict list
def clean_tags(tmp_df):
    tmp_df['tags'] = tmp_df['tags'].apply(lambda line: [x['tag'] for x in line])
    return tmp_df

# Input your dataframe and it gets completely cleaned
def clean_all(tmp_df):
    tmp_df = clean_date(tmp_df)
    tmp_df = drop_useless_columns(tmp_df)
    tmp_df = clean_tags(tmp_df)
    return tmp_df

