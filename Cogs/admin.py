import contextlib
import textwrap
from __main__ import bot
from traceback import format_exception

import discord
from discord.ext import commands
from etc.util import Pag, clean_code


class EvalCog(commands.Cog):

    def __init__(self, app):
        self.app = app

    @commands.command(name="eval", aliases=["exec", "cmd"])
    @commands.is_owner()
    async def _eval(self, ctx, *, code):
        code = clean_code(code)

        local_variables = {
            "discord": discord,
            "commands": commands,
            "bot": bot,
            "ctx": ctx,
        }

        import io
        stdout = io.StringIO()

        try:
            with contextlib.redirect_stdout(stdout):
                exec(
                    f"async def func():\n{textwrap.indent(code, '    ')}", local_variables,
                )

                obj = await local_variables["func"]()
                result = f"{stdout.getvalue()}\n-- {obj}\n"
        except Exception as e:
            result = "".join(format_exception(e, e, e.__traceback__))

        pager = Pag(
            timeout=100,
            entries=[result[i: i + 2000] for i in range(0, len(result), 2000)],
            length=1,
            prefix="```py\n",
            suffix="```",
        )
        print(result)
        await pager.start(ctx)


def setup(app):
    app.add_cog(EvalCog(app))
