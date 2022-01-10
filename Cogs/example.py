from nextcord.ext import commands
from nextcord.ext.commands.core import is_owner


class ExampleCog(commands.Cog):

    def __init__(self, bot):
        self.app = bot

    @commands.command(name="example", aliases=["ex", "example_command"])
    @commands.cooldown(1, 5, commands.BucketType.member)
    @is_owner()
    async def example(self, ctx, arg1=""):
        await ctx.send(f"arg1 : {arg1}")


def setup(bot):
    bot.add_cog(ExampleCog(bot))
