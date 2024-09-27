# pylint: disable-all
# type: ignore
import discord
from discord.ext import commands


class Misc(commands.Cog):
    def __init__(self, bot:commands.Bot):
        self.bot = bot


    @discord.slash_command(name = "ping", description = "Returns the bot's latency")
    async def command(self, ctx: discord.ApplicationContext) -> None:
        await ctx.respond(f"Pong! {round(self.bot.latency * 1000)} ms")
            

def setup(bot:commands.Bot):
    bot.add_cog(Misc(bot))
