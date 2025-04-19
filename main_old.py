import datetime
import os

import discord
from discord.ext import commands

from cogs.movies import shows_service as show_service

FFMPEG_PATH = os.path.join("cogs/files", "ffmpeg.exe")
COMMAND_COUNTER = {}
USER_COMMAND_COUNTER = {}
client = commands.Bot(command_prefix=commands.when_mentioned_or("$ "), intents=discord.Intents.all(), help_command=None)
shows_service = show_service.ShowsService(os.environ["THEMOVIEDB_TOKEN"])


@client.event
async def on_command(ctx):
    today = datetime.datetime.now()
    if today.weekday() == 4:  # Se for sexta
        COMMAND_COUNTER[ctx.command.name] = COMMAND_COUNTER.get(ctx.command.name, 0) + 1

        # Contagem individual do usuário
        user_id = ctx.author.id
        if user_id not in USER_COMMAND_COUNTER:
            USER_COMMAND_COUNTER[user_id] = {}
        USER_COMMAND_COUNTER[user_id][ctx.command.name] = USER_COMMAND_COUNTER[user_id].get(ctx.command.name, 0) + 1


client.run(os.environ["BOT_TOKEN"])
