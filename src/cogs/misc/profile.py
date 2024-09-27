# type: ignore

import discord
from discord.ext import commands
from discord import Option
from database.sql.database import Database
from src.utils.discord.embed_builder import EmbedBuilder


class Profile(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.database = Database("profiles")

    profile = discord.SlashCommandGroup(
        name="profile", description="Customize and see your profile"
    )  # COMMAND GROUP. TO GROUP ALL THE COMMANDS INTO /PROFILE {COMMAND}

    @profile.command(name="view", description="See your profile")  # /PROFILE VIEW
    @commands.cooldown(1, 10, commands.BucketType.user)  # COMMAND COOLDOWN (10 SECONDS)
    async def command(self, ctx: discord.ApplicationContext):

        user_query = self.database.select_data(
            "*", "Users", f"user_id={ctx.author.id}"
        )  # GET THE USER ID

        if user_query:  # IF THE USER EXISTS

            user_points = user_query[0][1]  # GET THE POINTS OF THE USER

            language_query = self.database.select_data(
                "language_id", "UserLanguages", f"user_id={ctx.author.id}"
            )  # GET ALL THE LANGUAGES ID OF THE USER

            # GET ALL THE EMOJI ID OF THE LANGUAGES AND TRANSFORM IT TO A STRING ARRAY
            flags_array = []
            for language in language_query:
                flag = self.database.select_data(
                    "emoji_id", "Languages", f"language_id={language[0]}"
                )
                flags_array.append(f"{flag[0][0]}")
            flags_string = (
                "  ".join(f":{flag}:" for flag in flags_array)
                or "Do /profile addlanguage to add languages"
            )
            ##########################################################################

            # EMBED LOGIC ############################################################
            embed_builder = EmbedBuilder(
                "My Profile",
                None,
                discord.Colour.blue(),
                f"@{ctx.author.name}",
                None,
                f"{ctx.author.avatar.url}",
                f"{ctx.bot.user.avatar.url}",
            )
            embed_builder.add_field(name="Learning Languages", value=f"{flags_string}")
            embed_builder.add_field(name="Points", value=f"{user_points} 🔹")
            embed = embed_builder.build()
            await ctx.respond(embed=embed)
            ##########################################################################

        else:  # IF THE USER DO NOT EXIST, INSERT IT ON THE DATABASE
            self.database.insert_data("Users", "user_id", f"{ctx.author.id}")
            self.database.commit()
            await ctx.respond(
                "You have no profile. Execute the command again to create one",
                ephemeral=True,
            )

    @profile.command(
        name="addlanguage", description="Add a new language to your profile"
    )  # /PROFILE REMOVELANGUAGE
    @commands.cooldown(1, 10, commands.BucketType.user)  # COMMAND COOLDOWN (10 SECONDS)
    async def command(
        self,
        ctx: discord.ApplicationContext,
        language: Option(
            str,
            description="The language you want to add to your profile",
            choices=["english", "portuguese", "japanese", "spanish", "chinese"],
            required=True,
        ),
    ):

        user_exists = self.database.select_data(
            "user_id", "Users", f"user_id={ctx.author.id}"
        )

        language_id = self.database.select_data(
            "language_id", "Languages", f"language_name='{language}'"
        )

        user_has_language = self.database.select_data(
            "language_id",
            "UserLanguages",
            f"user_id={ctx.author.id} AND language_id={language_id[0][0]}",
        )

        if (
            user_exists and not user_has_language
        ):  # IF THE USERS EXISTS AND HAS THE LANGUAGE
            # self.database.custom_query(f"INSERT INTO UserLanguages WHERE user_id={ctx.author.id} AND language_id={language_id[0][0]}")
            self.database.insert_data(
                "UserLanguages",
                "user_id, language_id",
                f"{ctx.author.id}, {language_id[0][0]}",
            )
            self.database.commit()
            await ctx.respond(
                f"You added **{language.capitalize()}** to your profile", ephemeral=True
            )

        elif not user_exists:  # IF THE USER DO NOT EXIST, INSERT IT ON THE DATABASE
            self.database.insert_data("Users", "user_id", f"{ctx.author.id}")
            self.database.commit()
            await ctx.respond(
                "You have no profile. Execute **/profile view** to create one",
                ephemeral=True,
            )

        elif (
            user_has_language
        ):  # IN CASE OF THE USER NOT HAVING THE LANGUAGE OF THE COMMAND
            await ctx.respond(
                "Already have this language in your profile", ephemeral=True
            )

    @profile.command(
        name="removelanguage",
        description="Remove an exisiting language to your profile",
    )  # /PROFILE REMOVELANGUAGE
    @commands.cooldown(1, 10, commands.BucketType.user)  # COMMAND COOLDOWN (10 SECONDS)
    async def command(
        self,
        ctx: discord.ApplicationContext,
        language: Option(
            str,
            description="The language you want to add to your profile",
            choices=["english", "portuguese", "japanese", "spanish", "chinese"],
            required=True,
        ),
    ):

        user_exists = self.database.select_data(
            "user_id", "Users", f"user_id={ctx.author.id}"
        )

        language_id = self.database.select_data(
            "language_id", "Languages", f"language_name='{language}'"
        )

        user_has_language = self.database.select_data(
            "language_id",
            "UserLanguages",
            f"user_id={ctx.author.id} AND language_id={language_id[0][0]}",
        )

        if (
            user_exists and user_has_language
        ):  # IF THE USERS EXISTS AND HAS THE LANGUAGE
            self.database.custom_query(
                f"DELETE FROM UserLanguages WHERE user_id={ctx.author.id} AND language_id={language_id[0][0]}"
            )
            self.database.commit()
            await ctx.respond(
                f"You have removed **{language.capitalize()}** from your profile",
                ephemeral=True,
            )

        elif not user_exists:  # IF THE USER DO NOT EXIST, INSERT IT ON THE DATABASE
            self.database.insert_data("Users", "user_id", f"{ctx.author.id}")
            self.database.commit()
            await ctx.respond(
                "You have no profile. Execute **/profile view** to create one",
                ephemeral=True,
            )

        elif (
            not user_has_language
        ):  # IN CASE OF THE USER NOT HAVING THE LANGUAGE OF THE COMMAND
            await ctx.respond(
                "You do not have this language in your profile", ephemeral=True
            )


def setup(bot: commands.Bot):
    bot.add_cog(Profile(bot))
