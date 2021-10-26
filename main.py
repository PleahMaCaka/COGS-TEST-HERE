import discord
from discord.ext import commands
import os
from etc.config import OWNER, TOKEN, PREFIX, GAME

bot = commands.Bot(command_prefix=PREFIX, owner_id=OWNER, help_command=None)

for filename in os.listdir("Cogs"):
    if filename.endswith(".py"):
        bot.load_extension(f"Cogs.{filename[:-3]}")
bot.remove_command('Example')


@bot.event
async def on_ready():
    print('=====================')
    print(bot.user.name)
    print(bot.user.id)
    print('=====================')
    game = discord.Game(GAME)
    await bot.change_presence(status=discord.Status.online, activity=game)


bot.run(TOKEN)
