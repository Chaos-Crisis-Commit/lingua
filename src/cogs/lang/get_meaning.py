# pylint: disable-all
# type: ignore
import discord
from discord import Option
from discord.ext import commands
from translate import Translator
from database.sql.database import Database
from src.language.analysis import get_meaning
from typing import Optional


class GetMeaning(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @discord.slash_command(name="get_meaning", description="Get meaning of word")
    async def command(
        self,
        ctx: discord.ApplicationContext,
        text: Option(str, "Text to identify", required=True),
        from_language: Option(
            str,
            "Source language",
            choices=["en", "es", "pt-br", "fr", "it", "ja", "ko", "zh-cn", "zh-tw"],
            default="en",
            required=True,
        ),
    ):
        # emb = discord.Embed(
        #     title="Meaning Command",
        #     description="",
        #     color=discord.Colour.orange(),
        # )

        meaning = get_meaning(from_language, text)

        # emb.add_field(name="Text", value=text, inline=False)
        # emb.add_field(name="Meaning", value=meaning, inline=False)
        await ctx.respond(meaning[1])


def setup(bot: commands.Bot):
    bot.add_cog(GetMeaning(bot))
