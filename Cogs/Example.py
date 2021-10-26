from discord.ext import commands
from discord.ext.commands.core import is_owner


class ExampleCog(commands.Cog):

    def __init__(self, app):
        self.app = app

    @commands.command(name="Example", aliases=["Ex"])
    @is_owner()
    async def _Example(self, ctx, args1=False):
        await ctx.send("Example")


def setup(app):
    app.add_cog(ExampleCog(app))
