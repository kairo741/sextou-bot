import os
from distutils.util import strtobool
import discord
from discord.ext import commands


class OnMessageEvent(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            return
        await self.react_sextou(message)

    @commands.Cog.listener()
    async def on_command(self, context):
        if strtobool(os.environ["DEBUG"]):
            user = context.author
            command = context.command
            server = context.guild
            print(f"⚙️ Comando: {command.name} | "
                  f"👤 Usuário: {user.name} (ID: {user.id}) | "
                  f"🗄️Servidor: {server.name} (ID: {server.id})")

    async def react_sextou(self, message: discord.Message):
        content = message.content.lower()
        key_words = ["sexta", "sextou", "friday"]
        if any(palavra in content for palavra in key_words):
            for emoji in ["🔥", "🇸", "🇪", "🇽", "🇹", "🇴", "🇺"]:
                await message.add_reaction(emoji)


async def setup(bot):
    await bot.add_cog(OnMessageEvent(bot))
