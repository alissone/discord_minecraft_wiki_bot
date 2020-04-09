from nested_lookup import nested_lookup
import json
import itertools
import urllib.request
from DuckDuckGoTools import duck_summary
from FuzzySearch import get_nouns, valid_distance, compute_distances, title_case_without_stopwords

def get_crafting_image(message):
    found_recipes = get_found_recipe_name(message)
    flat_recipes = list(itertools.chain(*found_recipes))
    image_urls = []

    for recipe in flat_recipes:
        if recipe.get('craft'):
            print("recipe",recipe.get('craft'))
            image_urls.append(build_crafting_image(recipe.get('name'), recipe.get('craft')))
    return image_urls

def search_in_recipes(query, recipe_vocabulary, thresh=65):
    recipes_found = []
    nouns = get_nouns(query)
    for word in nouns:
        distance = compute_distances(word, recipe_vocabulary)
        print("distance", distance)
        recipes_found.append(valid_distance(distance, thresh))
    if recipes_found:
        return recipes_found

def build_crafting_image(recipe_name, recipe_url, only_url=False):
    craft_url = 'https://www.minecraft-crafting.net/app/{}'.format(
    recipe_url)

    if only_url:
        return craft_url
    else:
        description = duck_summary('minecraft {}'.format(
            recipe_name.lower()))

        if description:
            description += "\n"
        else:
            description = ""

        return "How to craft {}: \n {} {}".format(
            recipe_name.title(), description, craft_url)

def get_found_recipe_name(query):
    with open('recipes.json') as recipes_file:
        recipes = json.load(recipes_file)
        recipes_vocabulary = list(recipes.keys())

        valid_queries = list(filter(None,search_in_recipes(query, recipes_vocabulary)))
        search_results = [
            nested_lookup(title_case_without_stopwords(valid_query), recipes)
            if valid_query else None for valid_query in valid_queries
        ]

    return search_results
