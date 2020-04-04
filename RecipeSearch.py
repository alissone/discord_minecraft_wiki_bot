from nested_lookup import nested_lookup
import json
import urllib.request
from DuckDuckGoTools import duck_summary

def get_crafting_image(query, only_url=False):
    result = False
    with open('recipes.json') as recipes_file:
        recipes = json.load(recipes_file)


        for result in (nested_lookup(query.title(), recipes)):
            craft_end = result['craft']
            craft_url = 'https://www.minecraft-crafting.net/app/{}'.format(craft_end)
            result = True
        if result:
            if only_url:
                return craft_url
            else:
                description = duck_summary('minecraft {}'.format(query.lower()))

                if description:
                    description += "\n"
                else:
                    description = ""

                return "How to craft {}: \n {} {}".format(query.title(),description, craft_url)