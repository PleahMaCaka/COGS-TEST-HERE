import os
from pathlib import Path

import nextcord
from nextcord.ext import commands

from etc.config import OWNER, TOKEN, PREFIX, activity_name, activity_type

client = commands.Bot(command_prefix=PREFIX, owner_id=OWNER, help_command=None)
cwd = Path(__file__).parents[0]

if __name__ == "__main__":
    for filename in os.listdir(str(cwd) + "/Cogs"):
        if filename.endswith(".py") and not filename.startswith("_"):
            client.load_extension(f"cogs.{filename[:-3]}")
client.remove_command('example')


@client.event
async def on_ready():
    print('=====================')
    print(client.user.name)
    print(client.user.id)
    print('=====================')
    activity = nextcord.Game(activity_name)
    await client.change_presence(status=activity_type, activity=activity)


client.run(TOKEN)
