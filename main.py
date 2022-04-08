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
    print(choice([ascii.SEXTOU_1, ascii.SEXTOU_2, ascii.SEXTOU_3, ascii.SEXTOU_4]))


@client.command("sextou")
async def send_video(context, version="NORMAL"):
    if version.upper() == "COMPLETE":
        await context.send(file=discord.File(constants.SEXTA_DOS_CRIAS_MP4_COMPLETE_EDITION))
    else:
        await context.send(file=discord.File(constants.SEXTA_DOS_CRIAS_MP4))


@client.command("shrek")
async def send_shrek(context):
    await context.send(file=discord.File(constants.SHREK_SEXTA_FEIRA_MP4))


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
    message.set_image(
        url="https://c.tenor.com/yenNqRV0M2oAAAAC/sexta-sexta-feira.gif")
    await context.send(embed=message)


@client.command("avatar")
async def send_avatar(context):
    message = discord.Embed(title="Sextouu?",
                            colour=discord.Colour.purple())
    message.set_image(
        url="https://cdn.discordapp.com/avatars/954427348315418694/ea558ea1dc3ae7fbeba1476a0fe4eda2.png?size=2048")
    await context.send(embed=message)


@client.command("author")
async def send_to_info(context):
    await send_author_info(context)


@client.command("info")
async def send_author_info(context):
    message = discord.Embed(title="Infos",
                            colour=discord.Colour.dark_red())

    message.add_field(name="Author do Bot - Kairo Amorim",
                      value=constants.ME_DESC,
                      inline=False)
    # To break a line
    message.add_field(name=chr(173), value=chr(173))

    message.add_field(name="DJ - DJ RAMON SUCESSO",
                      value=constants.DJ_RAMON_SUCESSO_DESC,
                      inline=False)

    spotify_message = discord.Embed(title="“O cara do tambor bolha”💦",
                               colour=discord.Colour.dark_red()).set_image(
        url="https://yt3.ggpht.com/Y50i3LmM9Vqb2x_iI5sWnYLm7hYJ5nVk8nvktGZhuWNA5uFyXfqFyEN63ra7jbiPzVA4jxcY-ota=s640"
            "-c-fcrop64=1,00000000ffffffff-nd-v1")
    await context.send(embed=message)
    await context.send(embed=spotify_message)


client.run(os.environ["BOT_TOKEN"])
