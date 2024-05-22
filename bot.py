import discord
from dotenv import dotenv_values
from discord.ext import commands
from pathlib import Path
from discord import app_commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

config = dotenv_values("data.env")

@bot.event
async def on_ready():
    for item in Path("./cogs").iterdir():
        if str(item).endswith(".py"):
            await bot.load_extension(f"cogs.{str(item)[5:-3]}")

    print(f">> Bot is online, as {bot.user} <<")

@bot.tree.command(name = "load", description = "Load a cog")
@app_commands.describe(cog = "The cog to load")
async def load(interaction: discord.Interaction, cog: str):
    await bot.load_extension(f"cogs.{cog}")
    await interaction.response.send_message(f"Successfullu loaded {cog}")

@bot.tree.command(name = "reload", description = "Reload a cog")
@app_commands.describe(cog = "The cog to reload")
async def reload(interaction: discord.Interaction, cog: str):
    await bot.reload_extension(f"cogs.{cog}")
    await interaction.response.send_message(f"Successfullu reloaded {cog}")

@bot.tree.command(name = "unload", description = "Unload a cog")
@app_commands.describe(cog = "The cog to unload")
async def unload(interaction: discord.Interaction, cog: str):
    await bot.unload_extension(f"cogs.{cog}")
    await interaction.response.send_message(f"Successfullu reloaded {cog}")

@bot.command()
async def sync(ctx, guild_id = None):
    if ctx.author.id == config["YUYU"]:
        commands = await bot.tree.sync(guild = guild_id)
        output = "\n".join(commands)
        await ctx.send("Sucessfully sync the following commands\n" + output)
    else:
        ctx.send("You're not permitted to do so.")

    



if __name__ == "__main__":
    bot.run(config["TOKEN2"])