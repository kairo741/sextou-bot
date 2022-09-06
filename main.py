import os
import re

from random import choice
import discord
import ascii
import constants
from discord.ext import commands
from spotify import spotifyclient

client = commands.Bot(command_prefix="$ ", intents=discord.Intents.all())


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


@client.command(aliases=['info', 'infos', 'author', 'authors', 'bot'])
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


@client.command("sexta?")
async def is_sexta(context):
    await context.send(choice([constants.IS_SEXTA_1, constants.IS_SEXTA_2,
                               constants.IS_SEXTA_3, constants.IS_SEXTA_4,
                               constants.IS_SEXTA_5, constants.IS_SEXTA_6,
                               constants.IS_SEXTA_7]))


@client.command("playlist")
async def create_playlist(context, playlist_name, *genres):
    spotify_client = spotifyclient.SpotifyClient(os.environ["SPOTIFY_AUTHORIZATION_TOKEN"])
    # last_tracks = spotify_client.get_last_played_tracks(number_of_tracks)

    genres = '°'.join(genres)
    if genres.upper() == 'DJ°RAMON°SUCESSO':
        for playlist in spotify_client.get_dj_ramons_albums():
            await context.send(f"https://open.spotify.com/album/{playlist.id}")
    else:
        if genres is not None:
            genres = re.sub("\!|\'|\?|,| |", "", genres)
            genres = genres.replace("°", ",")
            genres = ','.join(list(dict.fromkeys(genres.split(','))))

        if spotify_client.validate_music_genres(genres):
            recommended_tracks = spotify_client.get_track_recommendations(genres)
            playlist = spotify_client.create_playlist(playlist_name)
            spotify_client.populate_playlist(playlist, recommended_tracks)
            genres_message = ""
            genres = genres.split(",")
            for genre in genres:
                genres_message += f"• {genre.capitalize()}\n"

            message = discord.Embed(
                title=f"Gênero{'s' if len(genres) > 1 else ''} escolhido{'s' if len(genres) > 1 else ''}",
                description=genres_message,
                colour=discord.Colour.dark_green())
            await context.send(embed=message)
            await context.send(f"Sua playlist: https://open.spotify.com/playlist/{playlist.id}")
        else:
            await context.send("""AI AI AIAIAI 🔇 IAIAIAIAI\n(SEGUUU 🗡🗡💨 RA)\nUm ou mais gêneros não são válidos!""")


client.run(os.environ["BOT_TOKEN"])
