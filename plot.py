from read_data import data_to_dataframe
from cleaning import clean_all
import pandas as pd


def tag_count(tmp_df = "df"):
    all_tags = [tag for tags_list in tmp_df['tags'] for tag in tags_list]
    tag_counts = pd.Series(all_tags).value_counts()
    return tag_counts


def top_tags(topX):
    tag_count()
    
    top_tags = tag_counts.head(topX)
    return top_tags


def top_tags_without_regions(topX):
    tags_to_remove = ['Bundesländer','Baden-Württemberg','Bayern','Berlin',
                      'Brandenburg','Bremen','Hamburg','Hessen',
                      'Mecklenburg-Vorpommern','Niedersachsen','Nordrhein-Westfalen','Rheinland-Pfalz',
                      'Saarland','Sachsen','Sachsen-Anhalt','Schleswig-Holstein','Thüringen']
    
    tag_count()
    
    mask = ~tag_counts.index.isin(tags_to_remove)
    tags_without_regions = tag_counts[mask]
    top_tags_without_regions = tags_without_regions.head(topX)
    return top_tags_without_regions