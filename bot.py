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

@bot.hybrid_command()
async def load(ctx, cog: str):
    await bot.load_extension(f"cogs.{cog}")
    await ctx.send(f"Successfully loaded {cog}")

@bot.hybrid_command()
async def reload(ctx, cog: str):
    await bot.reload_extension(f"cogs.{cog}")
    await ctx.send(f"Successfully reloaded {cog}")

@bot.hybrid_command()
async def unload(ctx, cog: str):
    await bot.unload_extension(f"cogs.{cog}")
    await ctx.send(f"Successfully unloaded {cog}")

@bot.hybrid_command()
async def sync(ctx):
    commands = await bot.tree.sync()
    output = "\n".join([item.name for item in commands])
    await ctx.send("Sucessfully sync the following commands\n" + output)

    



if __name__ == "__main__":
    bot.run(config["TOKEN"])