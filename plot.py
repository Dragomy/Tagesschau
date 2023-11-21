import pandas as pd


# Yeah there is no input handling when you are stupid this function breaks
#Please fix this at some point!!


# If you input a dataframe that has a tag categorie this returns a list of all tags
def taglist(tmp_df):
    taglist = [tag for tags_list in tmp_df['tags'] for tag in tags_list]
    return taglist


#This should return a list of all text as well as the number of times the tag exists in the dataset
def taglist_counted(tmp_df):
    taglist = [tag for tags_list in tmp_df['tags'] for tag in tags_list]
    taglist_counted = pd.Series(taglist).value_counts()
    return taglist_counted


def taglist_no_regions(tmp_df):
    taglist = [tag for tags_list in tmp_df['tags'] for tag in tags_list]
    taglist_counted = pd.Series(taglist).value_counts()
    
    to_remove = ['Bundesländer','Baden-Württemberg','Bayern','Berlin',
                      'Brandenburg','Bremen','Hamburg','Hessen',
                      'Mecklenburg-Vorpommern','Niedersachsen','Nordrhein-Westfalen',
                      'Rheinland-Pfalz','Saarland','Sachsen','Sachsen-Anhalt',
                      'Schleswig-Holstein','Thüringen']
    
    mask = ~taglist_counted.index.isin(to_remove)
    taglist_no_regions = taglist_counted[mask]
    return taglist_no_regions