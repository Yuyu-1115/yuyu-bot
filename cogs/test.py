from email.mime import application
from click import Group
import discord
from core import Cog_Extension
from discord.ext import commands
from discord import app_commands


class Test(Cog_Extension):
    def __init__(self, bot) -> None:
        super().__init__(bot)

    @commands.command()
    async def hello(self, ctx):
        await ctx.send("Hello, world!")

    @app_commands.command(name = "add", description = "lol")
    @app_commands.guilds(discord.Object(id = 599296561079386152))
    async def plus(self, interaction: discord.Interaction, a: int, b: int):
        await interaction.response.send_message(a + b)

async def setup(bot):
    await bot.add_cog(Test(bot))