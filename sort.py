# ATTENTION: This script is being currently worked on.

from read_data.py import *

# All files get converted into a dataframe
daily_news = data_to_dataframe() 

known_columns = ["sophoraId", "extarnalId", "title", "date",
                  "teaserImage","tags", "updateCheckUrl", "tracking",
                  "topline", "firstSentence", "details", "detailsweb",
                  "shareURL", "geotags", "regionId", "regionIds",
                  "type", "breakingNews", "ressort", "brandingImage",
                  "streams", "alttext", "copyright", "comments"]

# Save all known collumns in a dataframe
daily_news_passed = daily_news[known_columns]

# Check if there are unknown collumns 
new_columns = [column for column in daily_news.columns if col not in required_columns]

# Should an unknown collumn be found save it in a dataframe with its sophoraId and date as Identifier
if new_columns:
    daily_news_failed = daily_news[["sophoraId", "date"] + new_columns]

# Split daily into first and last
first = daily_news_passed.drop_duplicates(subset = 'sophoraId', keep = 'first')
last = daily_news_passed.drop_duplicates(subset = 'sophoraId', keep = 'last')


#Requirements: 
def flatten_teaserImage(teaser_image):
    if isinstance(teaser_image, dict):
        flat_data = {
            'teaserImage_alttext': teaser_image.get('alttext', ''),
            'type': teaser_image.get('type', ''),
        }
        image_variants = teaser_image.get('imageVariants', {})
        if isinstance(image_variants, dict):
            for key, value in image_variants.items():
                flat_data[f'imageVariants_{key}'] = value
        return flat_data
    else:
        return {}


def extract_tag(tmp_df):
    if isinstance(tmp_df, dict):  
        return tmp_df.get('tag')  
    else:
    return None  


def flatten_tracking(df):  
    if 'tracking' in df.columns and df['tracking'].notna().any():
        
        tracking_df = df['tracking'].apply(lambda x: pd.Series(x[0]) if isinstance(x, list) and len(x) > 0 else pd.Series())
        tracking_df.columns = [f'tracking_{col}' for col in tracking_df.columns]
        df = pd.concat([df.drop(columns=['tracking']), tracking_df], axis=1)
    
    return df


# Since everything that follows is for both first and last we write a function
def flatten_known_collumns(df, df_name):
    geotags = df["sophoraId", "geotags"]
    f'geotags_{df_name}' = geotags.explode("geotags")
    
    regionIds = df["sophoraId", "regionIds"]
    f'regionIds_{df_name}' = regionIds.explode("regionIds")

    teaserImage = df["sophoraId", "teaserImage"]
    flatten_teaserImage = teaserImage["teaserImage"].apply(flatten_teaserImage)
    teaserImage_df = pd.DataFrame(flatten_teaser_images.tolist())
    teaserImage = pd.concat([links.drop(columns=['teaserImage']), flattened_df], axis=1)
    f'teaserImage_{df_name}' = teaserImage

    tags = df["sophoraId", "tags"]
    tags = tags.explode('tags')
    tags['tags'] = tags['tags'].apply(extract_tag)
    f'tags_{df_name}' = tags

    tracking = df["sophoraId", "tracking"]
    tracking = flatten_tracking(df)  
    f'tracking_{df_name}' = tracking


flatten_known_collumns(first,"first")

    
    


     









# If evrery collumn is in the list 
# --> Split into daylie_news_first and daylie_news_last
# --> flatten and save them as parquet 
# You should now get:
# daylie_news_first.parquet
# daylie_news_last.parquet
# {non_flat_collumn_name}_first.parquet
# {non_flat_collumn_name}_last.parquet

# Before appending them to any older files check for conflicts



