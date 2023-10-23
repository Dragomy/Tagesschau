import os 
import json
import pandas as pd


region_names = {
        -2.0 : 'Other',
        -1.0 : 'Video (without Id)',
        0.0 : 'BadenWürttemberg',
        1.0: 'Bayern',
        2.0 : 'Berlin',
        3.0 : 'BrandenBurg',
        4.0 : 'Bremen',
        5.0 : 'Hamburg',
        6.0 : 'Hessen',
        7.0 : 'MecklenburgVorpommern',
        8.0 : 'Niedersachsen',
        9.0 : 'NordrheinWestfalen',
        10.0 : 'RheinlandPfalz',
        11.0 : 'Saarland',
        12.0 : 'Sachsen',
        13.0 : 'Sachsen-Anhalt',
        14.0 : 'SchleswigHolstein',
        15.0 : 'Thüringen',    
    }


#Shows the distribution of Region Id occurencess the Filter/Sorts above help to clean certain things.
def plot_regionId(tmp_df, plot_kind = 'bar'):
    regionlist = []
    
    region_counts = tmp_df.value_counts('regionId').sort_index() 

    for x in region_counts.index:
        y = region_names[x]
        regionlist.append(y) 

    region_counts.index = regionlist
    region_counts.plot(kind = plot_kind)