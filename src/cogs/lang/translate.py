# pylint: disable-all
# type: ignore
import discord
from discord import Option
from discord.ext import commands
from translate import Translator
from database.sql.database import Database
from typing import Optional


class Translate(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.database = Database("translator")
    
    def find_local(self, text) -> Optional[str]:
        query_results = self.database.select_data('rowid', 'sentences', f'sentence="{text}"') 
        if not query_results:
            return None
        return query_results[0][0]

    @discord.slash_command(name='translate', description='Translate')
    async def command(
        self,
        ctx: discord.ApplicationContext,
        text: Option(str, "Text to translate", required=True),
        from_language: Option(str, "Source language", choices=["en", "es", "pt-br", "fr", "it", "ja", "ko", "zh-cn", "zh-tw"], default='en', required=True),
        to_language: Option(str, "Target language", choices=["en", "es", "pt-br", "fr", "it", "ja", "ko", "zh-cn", "zh-tw"], default='en', required=True)
    ):
        local_query_result = self.find_local(text)
        emb = discord.Embed(
            title="Translation Command",
            description="Maybe not accurate.",
            color=discord.Colour.orange()
        )
        
        if local_query_result:
            meaning = self.database.select_data('meaning', 'meaning', f'sentence_id={local_query_result}')
            emb.add_field(name="Text", value=text, inline=False)
            emb.add_field(name="From Language", value=from_language, inline=False)
            emb.add_field(name="To Language", value=to_language, inline=True)
            emb.add_field(name="Result", value=meaning[0][0], inline=False)
            await ctx.respond("", embed=emb)
            return
        translator = Translator(provider='mymemory', from_lang=from_language, to_lang=to_language)
        translated = translator.translate(text)
        
        emb.add_field(name="Text", value=text, inline=False)
        emb.add_field(name="From Language", value=from_language, inline=False)
        emb.add_field(name="To Language", value=to_language, inline=True)
        emb.add_field(name="Result", value=translated, inline=False)
        
        await ctx.respond("", embed=emb)

def setup(bot: commands.Bot):
    bot.add_cog(Translate(bot))
