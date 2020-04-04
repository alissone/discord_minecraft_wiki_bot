from RecipeSearch import get_crafting_image
from SynonymsTools import check_multi_syns_inside
import inflect
from SecretToken import token

import discord

TOKEN = token()

import discord

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

def craft_intent(message):
    intent_words = ['craft', 'build', 'make', 'create']
    return check_multi_syns_inside(intent_words, message.content)

def craft_recipe_search(message):
    inflect_engine = inflect.engine()

    for word in message.content.split(' '):
        crafting_recipe = get_crafting_image(word)
        if not crafting_recipe:
            plural_word = inflect_engine.plural(word)
            crafting_recipe = get_crafting_image(plural_word)
        if crafting_recipe:
            return crafting_recipe


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if craft_intent(message):
        crafting_recipe = craft_recipe_search(message)
        if crafting_recipe:
            await message.channel.send(crafting_recipe)


    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

client.run(TOKEN)