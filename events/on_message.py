import discord
from discord.ext import commands
import sys


def is_debug():
    gettrace = getattr(sys, 'gettrace', None)

    if gettrace is None:
        return False
    else:
        v = gettrace()
        if v is None:
            return False
        else:
            return True


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
        if is_debug():
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
