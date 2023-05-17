import discord
from discord.ext import commands
import music
from discord_slash import SlashCommand

cogs = [music]
client = commands.Bot(command_prefix='los ', intents = discord.Intents.all())
slash = SlashCommand(client, sync_commands=True)

for i in range(len(cogs)):
    cogs[i].setup(client)



client.run("ODg3NTMyNjc0ODA0MjMyMjAz.YUFhNw.1qC3K0-rJAr4P1sg4supakdS3mE")