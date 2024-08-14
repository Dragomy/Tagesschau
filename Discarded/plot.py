import pandas as pd

# We don't talk about duplicate code 

regions = ['Baden-Württemberg',
 'Bayern',
 'Berlin',
 'Brandenburg',
 'Bremen',
 'Hamburg',
 'Hessen',
 'Mecklenburg-Vorpommern',
 'Niedersachsen',
 'Nordrhein-Westfalen',
 'Rheinland-Pfalz',
 'Saarland',
 'Sachsen',
 'Sachsen-Anhalt',
 'Schleswig-Holstein',
 'Thüringen']


regiondict = {1: "Baden-Württemberg",
 2: "Bayern",
 3: "Berlin",
 4: "Brandenburg",
 5: "Bremen",
 6: "Hamburg",
 7: "Hessen",
 8: "Mecklenburg-Vorpommern",
 9: "Niedersachsen",
 10: "Nordrhein-Westfalen",
 11: "Rheinland-Pfalz",
 12: "Saarland",
 13: "Sachsen",
 14: "Sachsen-Anhalt",
 15: "Schleswig-Holstein",
 16: "Thüringen"}


# <!-- Tags --!>

# This function takes every tag found in the input data frame and puts it into a huge list
# For this to work the input data frame needs to have a tags column that lists tags in the format
# [tag x, tag x]
def taglist(tmp_df):
    taglist = [tag for tags_list in tmp_df['tags'] for tag in tags_list]
    return taglist


# This function takes the tag list and counts the appearance of tags in the end, all of that then is packed into a dictionary in this format:
# {"tag":  count as integer, ...}
def tags_counted(tmp_df):
    taglist = [tag for tags_list in tmp_df['tags'] for tag in tags_list]
    taglist_counted = pd.Series(taglist).value_counts().to_dict()
    return taglist_counted


# This function takes the tag list and counts the appearance of tags.
# Next a mask is created and used on the counts so all regions are removed
# In the last step all is packed into a dictionary
def tags_no_regions(tmp_df):
    taglist = [tag for tags_list in tmp_df['tags'] for tag in tags_list]
    taglist_counted = pd.Series(taglist).value_counts()

    mask = ~taglist_counted.index.isin(regions)
    taglist_no_regions = taglist_counted[mask].to_dict()
    return taglist_no_regions


# This function takes the tag list and counts the appearance of tags.
# Next a mask is created and used on the counts so everything besides the regions is removed
# In the last step all is packed into a dictionary
def tags_only_regions(tmp_df):
    taglist = [tag for tags_list in tmp_df['tags'] for tag in tags_list]
    taglist_counted = pd.Series(taglist).value_counts()

    mask = taglist_counted.index.isin(regions)
    taglist_only_regions = taglist_counted[mask].to_dict()
    return taglist_only_regions


# <!-- Regions --!>


# This function takes every region found in the input data frame and puts it into a huge list.
def regionlist(tmp_df):
    regionlist = [region for regions_list in tmp_df['regionIds'] if isinstance(regions_list, list) for region in regions_list]
    return regionlist

# This function takes the region list and counts the appearance of regionids in the end, all of that then is packed into a dictionary in this format:
# {regionId as integer :  count as integer, ...}
def regionlist_counted(tmp_df):
    regionlist = [region for regions_list in tmp_df['regionIds'] if isinstance(regions_list, list) for region in regions_list]
    regionlist_counted = pd.Series(regionlist).value_counts().to_dict()
    return regionlist_counted


def regionlist_counted_corrected_index(tmp_df):
    regionlist = [region for regions_list in tmp_df['regionIds'] if isinstance(regions_list, list) for region in regions_list]
    regionlist_counted = pd.Series(regionlist).value_counts()
    regionlist_counted.index = regionlist_counted.index.astype(int)
    regionlist_counted.index = regionlist_counted.index.map(regiondict)
    regionlist_counted = regionlist_counted.to_dict()
    return regionlist_counted


# <!-- Multiples --!>


# This function takes two dictionaries goes through the keys and if there are several same keys the values get compared and written to a separate dict
def get_dict_differences(dict1, dict2):
    tmp_dict = {key: (dict1[key], dict2[key]) for key in dict1 if dict1[key] != dict2[key]}
    differences = {key: max(value) - min(value) for key, value in tmp_dict.items()}
    return differences