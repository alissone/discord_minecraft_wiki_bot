import requests
from scrapy.http import Htmlresponse
import pandas as pd
import json

def digminecraft_enchantment_scraper(url):
    resp = requests.get(url)
    response = HtmlResponse(url="", body=resp.text, encoding='utf-8')
    html_table = response.xpath("//table[@class='std_table']").get()
    dataframe = pd.read_html(html_table)
    return dataframe[0]

def dataframe_to_description(dataframe,max_cols=1):
    for i in range(len(dataframe)):
        column_titles = dataframe.iloc[i,:max_cols].index.values.tolist()
        column_descriptions = dataframe.iloc[i,:max_cols].to_string(index=False).split('\n')
        for idx, column_title in enumerate(column_titles):
            print(column_title+": **",' '.join(column_descriptions[idx].split()) + "**")

def search_in_dataframe(dataframe,query_string):
    df = dataframe.astype(str)
    return df[df.apply(lambda x: x.str.contains(query_string)).any(axis=1)]

def dataframe_to_columns(dataframe):
    list_of_series = []
    for column in dataframe.columns:
        list_of_series.append(dataframe[column])
    return list_of_series

list_of_pages = [
    'https://www.digminecraft.com/lists/chestplate_enchantment_list_pc.php',
    'https://www.digminecraft.com/lists/bow_enchantment_list_pc.php',
    'https://www.digminecraft.com/lists/helmet_enchantment_list_pc.php',
    'https://www.digminecraft.com/lists/leggings_enchantment_list_pc.php',
    'https://www.digminecraft.com/lists/boots_enchantment_list_pc.php',
    'https://www.digminecraft.com/lists/fishing_rod_enchantment_list_pc.php',
    'https://www.digminecraft.com/lists/axe_enchantment_list_pc.php',
    'https://www.digminecraft.com/lists/pickaxe_enchantment_list_pc.php',
    'https://www.digminecraft.com/lists/shovel_enchantment_list_pc.php',
    'https://www.digminecraft.com/lists/trident_enchantment_list_pc.php',
    'https://www.digminecraft.com/lists/crossbow_enchantment_list_pc.php',
]
list_of_names = [
    'sword',
    'bow',
    'helmet',
    'leggings'
    'boots',
    'fishingrod',
    'axe',
    'pickaxe',
    'shovel',
    'trident',
    'crossbow'
]

for idx, url in enumerate(list_of_pages):
    filename = 'enchantments_{}.json'.format(list_of_names[idx])
    print("Downloading {}...".format(filename))

    df = digminecraft_enchantment_scraper(url)
    json_df = df.to_json()

    print("Saving {}...".format(filename))
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(json_df, f, ensure_ascii=False, indent=4)