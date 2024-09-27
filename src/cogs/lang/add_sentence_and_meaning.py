import discord
from discord.ext import commands
from discord import Option
from database.sql.database import Database


class AddSentenceAndMeaning(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.database = Database("translator")

    @discord.slash_command(
        name="addsentenceandmeaning", description="Add a sentence and its meaning"
    )
    async def command(
        self,
        ctx: discord.ApplicationContext,
        sentence=Option(str, "Sentence to add", required=True),
        meaning=Option(str, "Sentence's meaning", required=True),
    ):
        self.database.insert_data("sentences", "sentence", f'"{sentence}"')
        self.database.insert_data(
            "meaning",
            "meaning, sentence_id",
            f'"{meaning}","{self.database.cursor.lastrowid}"',
        )
        self.database.commit()
        await ctx.respond(f"Sentence: {sentence} added with meaning: {meaning}")


def setup(bot: commands.Bot):
    bot.add_cog(AddSentenceAndMeaning(bot))
