import datetime
from random import choice, randint

import discord
import requests
from discord.ext import commands

COMMAND_COUNTER = {}
USER_COMMAND_COUNTER = {}
class Stats(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.hybrid_command(name="status_sextou", with_app_command=True,
                           description="Mostra se a sexta está boa ou não...")
    async def status_sextou(self, ctx: commands.Context, me=False):
        await ctx.defer()
        today = datetime.datetime.now()
        if today.weekday() != 4:  # Valida se é sexta
            await ctx.send("🚫 O comando `status_sextou` só funciona na sexta-feira! ⏳")
            COMMAND_COUNTER.clear()
            USER_COMMAND_COUNTER.clear()
            return

        user = ctx.author
        commands_list = COMMAND_COUNTER
        command_goal = 30
        if me:
            commands_list = USER_COMMAND_COUNTER[user.id]
            command_goal = 5

        total_cmds = sum(commands_list.values())
        description = f"Hoje já foram usados **`{total_cmds}`** comandos no bot!"
        footer_message = "Bora aumentar esse número? Sextoouuu! 🕺💃"
        embed_color = discord.Color.dark_gray()

        if me:
            description = f"Hoje você já usou **`{total_cmds}`** comandos no bot!"
        if total_cmds >= command_goal:
            footer_message = "🔥 Agora sim, Sextouuuu! Essa sexta tá insana! 🚀🎉"
            embed_color = discord.Color.random()

        if not commands_list:
            embed = discord.Embed(
                title="📊 Status Sextou",
                description="Ainda ninguém usou o bot hoje. Vamos começar o sextou? 🎉",
                color=embed_color,
                timestamp=today
            )
        else:
            embed = discord.Embed(
                title="📊 Status Sextou 🔥",
                description=description,
                color=embed_color,
                timestamp=today,
            )

        for cmd, used_amount in commands_list.items():
            embed.add_field(name=f"**{cmd}**", value=f"`{used_amount} vezes`", inline=False)

        if not me:
            embed.set_thumbnail(url=choice([constants.SEXTOU_LYRICS_GIF, constants.SEXTOU_HOMER_GIF]))
        else:
            embed.set_author(name=user.display_name, icon_url=user.avatar.url, url=constants.YT_1HOUR_URL)
        embed.set_footer(text=footer_message)

        await ctx.send(embed=embed)

async def setup(bot):
    """Função assíncrona para adicionar este cog ao bot."""
    await bot.add_cog(Stats(bot))
