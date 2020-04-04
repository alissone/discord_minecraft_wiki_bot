from nested_lookup import nested_lookup
import json
import urllib.request
from DuckDuckGoTools import duck_summary
from FuzzySearch import get_nouns, valid_distance, compute_distances

def search_in_recipes(query,recipe_vocabulary,thresh=65):
    recipes_found = []
    nouns = get_nouns(query)
    for word in nouns:
        print(word)
        recipes_found.append(valid_distance(compute_distances(word,recipe_vocabulary),thresh))
    if recipes_found:
        return recipes_found

def get_crafting_image(query, only_url=False):
    result = False
    with open('recipes.json') as recipes_file:
        recipes = json.load(recipes_file)
        recipes_vocabulary = list(recipes.keys())

        valid_queries = search_in_recipes(query, recipes_vocabulary)
        print("valid_queries",valid_queries)

        for result in (nested_lookup(valid_queries[0].title(), recipes)):
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