# pylint: disable-all
# type: ignore

import discord
from discord.ext import commands
from discord import Option
import requests
import os
from dotenv import load_dotenv

load_dotenv()


class Animal(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.caturl = "https://api.thecatapi.com/v1/images/search"
        self.dogurl = "https://api.thedogapi.com/v1/images/search"
        self.catheader = {"x-api-key": os.getenv("CATAPI_KEY")}
        self.dogheader = {"x-api-key": os.getenv("DOGAPI_KEY")}

    @discord.slash_command(name="animal", description="Gets you motivated.")
    async def command(
        self,
        ctx: discord.ApplicationContext,
        animal: Option(str, "Dog or Cat", choices=["dog", "cat"], required=True),
    ):

        emb = discord.Embed(title=f"Look how cute this {animal} is")

        if animal == "dog":
            response = requests.get(self.dogurl, headers=self.dogheader)
            data = response.json()
            emb.set_image(url=data[0]["url"])
            await ctx.respond(f"There we go", embed=emb)
        elif animal == "cat":
            response = requests.get(self.caturl, headers=self.catheader)
            data = response.json()
            emb.set_image(url=data[0]["url"])
            await ctx.respond(f"There we go", embed=emb)


def setup(bot: commands.Bot):
    bot.add_cog(Animal(bot))
