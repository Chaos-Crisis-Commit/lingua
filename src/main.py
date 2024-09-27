# pylint: disable-all
# type: ignore
import os
import discord
from dotenv import load_dotenv

load_dotenv()

bot = discord.Bot()


@bot.event
async def on_ready():
    print(f"{bot.user.name} is online mfs!")


@bot.event
async def on_connect():
    if bot.auto_sync_commands:
        await bot.sync_commands()
    print(f"{bot.user.name} connected.")


for filename in os.listdir("./src/cogs"):
    if filename.endswith(".py") and not filename.startswith("_"):
        bot.load_extension(f"cogs.{filename[:-3]}")
        print(f"{filename[:-3].capitalize()} Cog loaded")

bot.run(os.getenv("TOKEN"))
