import os

from nextcord.ext import commands
from nextcord.ext.commands.core import is_owner

from main import client, cwd


class ReloadCog(commands.Cog):

    def __init__(self, bot):
        self.app = bot

    @commands.command(name="reload", aliases=["rd"])
    @is_owner()
    async def _reload(self, ctx):
        for filename in os.listdir(str(cwd) + "/Cogs"):
            if filename.endswith(".py") and not filename.startswith("_"):
                client.load_extension(f"cogs.{filename[:-3]}")
        client.remove_command('example')
        await ctx.reply("Cogs Reload Complete!")


def setup(bot):
    bot.add_cog(ReloadCog(bot))
