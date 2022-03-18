import os
from random import choice

import discord
import ascii
import constants
from discord.ext import commands

client = commands.Bot(command_prefix="$ ")


@client.event
async def on_ready():
    await client.change_presence(
        activity=discord.Streaming(name="SEXTA DOS CRIAS",
                                   url="https://www.youtube.com/watch?v=6zF3H1vH-6g",
                                   platform="Sexta"))
    print("Bot sextouu")


@client.command("sextou")
async def send_video(context, version="NORMAL"):
    if version.upper() == "COMPLETE":
        await context.send(file=discord.File(constants.SEXTA_DOS_CRIAS_MP4_COMPLETE_EDITION))
    else:
        await context.send(file=discord.File(constants.SEXTA_DOS_CRIAS_MP4))


@client.command("message")
async def send_message(context):
    message = choice(
        [ascii.SEXTOU_1, ascii.SEXTOU_2, ascii.SEXTOU_3, ascii.SEXTOU_4])
    await context.send(message)


@client.command("lyrics")
async def lyrics(context):
    message = discord.Embed(title="Sexta dos crias",
                            description=constants.SEXTA_DOS_CRIAS_LYRICS,
                            colour=discord.Colour.dark_blue())
    await context.send(embed=message)


client.run(os.environ["BOT_TOKEN"])
