from random import choice

import discord
from discord.ext import commands
from pyfiglet import figlet_format
from utils import constants, ascii


class OnReadyEvent(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        await self.bot.change_presence(
            activity=discord.Streaming(
                name="SEXTA DOS CRIAS",
                url=constants.YT_1HOUR_URL
            )
        )
        try:
            synced = await self.bot.tree.sync()
            print(f'{len(synced)} slash commands foram sincronizados')
        except Exception as e:
            print(f"Erro ao sincronizar comandos: {e}")

        print(figlet_format('SEXTOU', font=choice(ascii.ASCII_FONTS)))


async def setup(bot):
    await bot.add_cog(OnReadyEvent(bot))
