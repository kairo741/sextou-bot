import discord
from discord.ext import commands

class OnMemberJoinEvent(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # @commands.Cog.listener()
    # async def on_member_join(self, member: discord.Member):
    #     channel = discord.utils.get(member.guild.text_channels, name="boas-vindas")
    #     if channel:
    #         await channel.send(f"🎉 Olá {member.mention}, bem-vindo(a) ao servidor! 🚀")

async def setup(bot):
    await bot.add_cog(OnMemberJoinEvent(bot))
