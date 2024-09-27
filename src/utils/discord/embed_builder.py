import discord
import random
from typing import Optional, List, Tuple


class EmbedBuilder:
    def __init__(self, 
                 title: Optional[str] = None, 
                 description: Optional[str] = None, 
                 color: Optional[discord.Color] = None, 
                 author_name: Optional[str] = None, 
                 author_icon: Optional[str] = None, 
                 thumbnail_url: Optional[str] = None, 
                 footer_url: Optional[str] = None):
        
        self.title = title
        self.description = description
        
        self.author_name = author_name
        self.author_icon = author_icon
        
        self.thumbnail_url = thumbnail_url
        
        self.color = color or discord.Colour.nitro_pink()
        
        # Sentences for the footer
        self.sentences = [
            "Made with <3 by the Lingua Team",
            "Consider supporting the bot. You will receive rewards!",
            "Lingua is in active development. Feature requests are welcome!",
            "Saw a bug? Report it!",
            "Have fun!"
        ]
        
        self.footer_url = footer_url or "https://cdn3.emoji.gg/emojis/31219-nerdpoint.png"
        
        self.sentence = random.choice(self.sentences)
        
        # List to hold fields
        self.fields: List[Tuple[str, str, bool]] = []

    def add_field(self, name: str, value: str, inline: bool = False) -> None:
        # Add a field to the embed
        self.fields.append((name, value, inline))

    def build(self) -> discord.Embed:
        embed = discord.Embed(title=self.title, description=self.description, color=self.color)
        
        if self.author_name:
            if self.author_icon:
                embed.set_author(name=self.author_name, icon_url=self.author_icon)
            else:
                embed.set_author(name=self.author_name)
        
        if self.thumbnail_url:
            embed.set_thumbnail(url=self.thumbnail_url)
        
        embed.set_footer(text=self.sentence, icon_url=self.footer_url)
        
        for name, value, inline in self.fields:
            embed.add_field(name=name, value=value, inline=inline)
        
        return embed
