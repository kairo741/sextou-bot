import asyncio
import os

import discord
from discord.ext import commands

# Carregar variáveis de ambiente
TOKEN = os.environ["BOT_TOKEN"]

# Configurar bot
intents = discord.Intents.all()
intents.messages = True
bot = commands.Bot(command_prefix="$ ", intents=intents, help_command=None)


async def load_cogs():
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py") and filename != "__init__.py":
            await bot.load_extension(f"cogs.{filename[:-3]}")


async def load_events():
    for filename in os.listdir("./events"):
        if filename.endswith(".py") and filename != "__init__.py":
            await bot.load_extension(f"events.{filename[:-3]}")


async def main():
    async with bot:
        await load_cogs()
        await load_events()
        await bot.start(TOKEN)


asyncio.run(main())
