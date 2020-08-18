# Discord Minecraft wiki bot

This is a chatbot that answers any user with crafting recipes for any block in the game using info from https://www.minecraft-crafting.net/.
In the future it will also answer more general questions about the game, I'm still working on a proper language model for it.

To test, simply run `python3  TestingChatbot.py`. It will answer any user in the channel like this:

![Bot in action](https://github.com/alissone/discord_minecraft_wiki_bot/raw/master/2020-08-18_09:49:18.png?raw=true)

#### Note: This project is still a WIP, many changes will be coming soon:
- Classify intent to decide wether to answer with a crafting recipe or something else
- Use Fuzzy search only with block names
- Implement instant results from DuckDuckGo API
- Avoid bias towards single-word block names
