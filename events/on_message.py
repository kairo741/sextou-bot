import discord
from discord.ext import commands


class OnMessageEvent(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # @commands.Cog.listener()
    # async def on_message(self, message: discord.Message):
    #     if message.author == self.bot.user:
    #         return  # Ignora mensagens do próprio bot
    #
    #     content = message.content.lower()
    #     key_words = ["sexta", "sextou", "friday"]
    #
    #     if any(word in content for word in key_words):
    #         for emoji in ["🔥", "🇸", "🇪", "🇽", "🇹", "🇴", "🇺"]:
    #             await message.add_reaction(emoji)

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            return
        await self.react_sextou(message)

    async def react_sextou(self, message: discord.Message):
        content = message.content.lower()
        key_words = ["sexta", "sextou", "friday"]
        if any(palavra in content for palavra in key_words):
            for emoji in ["🔥", "🇸", "🇪", "🇽", "🇹", "🇴", "🇺"]:
                await message.add_reaction(emoji)


async def setup(bot):
    await bot.add_cog(OnMessageEvent(bot))
