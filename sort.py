# ATTENTION: This script is being currently worked on.

from read_data.py import *
import pandas as pd


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
def flatten_and_save(df, df_name):
    # Flatten geotags
    geotags = df[["sophoraId", "geotags"]].copy()
    geotags_exploded = geotags.explode("geotags")
    save_dataframe(geotags_exploded, f'geotags_{df_name}')

    # Flatten regionIds
    regionIds = df[["sophoraId", "regionIds"]].copy()
    regionIds_exploded = regionIds.explode("regionIds")
    save_dataframe(regionIds_exploded, f'regionIds_{df_name}')

    # Flatten teaserImage
    teaserImage = df[["sophoraId", "teaserImage"]].copy()
    flattened_teaserImage = teaserImage["teaserImage"].apply(flatten_teaserImage)
    teaserImage_df = pd.DataFrame(flattened_teaserImage.tolist())
    teaserImage_combined = pd.concat([teaserImage.drop(columns=['teaserImage']), teaserImage_df], axis=1)
    save_dataframe(teaserImage_combined, f'teaserImage_{df_name}')

    # Flatten tags
    tags = df[["sophoraId", "tags"]].copy()
    tags_exploded = tags.explode("tags")
    tags_exploded["tags"] = tags_exploded["tags"].apply(extract_tag)
    save_dataframe(tags_exploded, f'tags_{df_name}')

    # Flatten tracking
    tracking = df[["sophoraId", "tracking"]].copy()
    tracking_flattened = flatten_tracking(tracking)
    save_dataframe(tracking_flattened, f'tracking_{df_name}')

def save_dataframe(df, name):
    file_name = f'{name}.parquet.gzip'
    df.to_parquet(file_name, "pyarrow", "gzip", index=False)
    print(f'Saved {file_name}')
    
# Before appending them to any older files check for conflicts