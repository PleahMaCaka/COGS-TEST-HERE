import os

from discord.ext import commands
from discord.ext.commands import bot
from discord.ext.commands.core import is_owner


class ReloadCogs(commands.Cog):

    def __init__(self, app):
        self.app = app

    @commands.command(name="reload", aliases=["리로드"])
    @is_owner()
    async def _reload(self, ctx, args1=False):
        for filename in os.listdir("Cogs"):
            if filename.endswith(".py"):
                bot.reload_extension(f"Cogs.{filename[:-3]}")
                print(f"[RELOAD] {filename}")
        await ctx.send("모든 명령어를 다시 불러왔습니다.")


def setup(app):
    app.add_cog(ReloadCogs(app))
