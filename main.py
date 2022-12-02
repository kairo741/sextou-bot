import os
import re
from random import choice

import discord
from discord.ui import Select, View
from discord.ext import commands
from pyfiglet import figlet_format

import ascii
import command
import constants
from spotify import spotifyclient

client = commands.Bot(command_prefix=commands.when_mentioned_or("$ "), intents=discord.Intents.all(), help_command=None)


@client.event
async def on_ready():
    await client.change_presence(
        activity=discord.Streaming(name="SEXTA DOS CRIAS",
                                   url=constants.YT_1HOUR_URL,
                                   platform="Sexta"))
    try:
        synced = await client.tree.sync()
        print(f'{len(synced)} slash commands foram sincronizados')
    except Exception as e:
        print(e)

    # print(choice([ascii.SEXTOU_1, ascii.SEXTOU_2, ascii.SEXTOU_3, ascii.SEXTOU_4]))
    print(figlet_format('SEXTOU', font=choice(ascii.ASCII_FONTS)))


@client.hybrid_command(name="sextou", with_app_command=True, description="Sextouuu")
@discord.app_commands.describe(version="Versão do video (NORMAL ou COMPLETE)")
async def send_video(context, version="NORMAL"):
    if version.upper() == "COMPLETE":
        await context.send(file=discord.File(constants.SEXTA_DOS_CRIAS_MP4_COMPLETE_EDITION))
    elif version.upper() == "ALTERNATIVE":
        await context.send(file=discord.File(constants.SEXTA_DOS_CRIAS_MP4_ALTERNATIVE_EDITION))
    else:
        await context.send(file=discord.File(constants.SEXTA_DOS_CRIAS_MP4))


@client.hybrid_command(name="sound", with_app_command=True, description="Sexta dos crias sound")
async def send_sound(context):
    await context.send(file=discord.File(constants.SEXTA_DOS_CRIAS_SOUND_MP3))


@client.hybrid_command(name="shrek", with_app_command=True, description="Graças a Deus é sexta-feira")
async def send_shrek(context):
    await context.send(file=discord.File(constants.SHREK_SEXTA_FEIRA_MP4))


@client.hybrid_command(name="urso", with_app_command=True, description="Urso da semana da sexta")
async def send_shrek(context):
    await context.send(file=discord.File(constants.URSO_DA_SEXTA_MP4))


@client.hybrid_command(name="rockers", with_app_command=True, description="Rooockkkkers SEXTOoOoUuU")
async def send_shrek(context):
    await context.send(file=discord.File(constants.ROCKERS_SEXTOU_MP4))


@client.hybrid_command(name="fring", with_app_command=True, description="Holy shit it's fring friday")
async def send_fring(context):
    await context.send(file=discord.File(constants.FRING_FRIDAY_MP4))


@client.hybrid_command(name="message", with_app_command=True, description="ASCII aleatório desenhando \"Sextou\"")
async def send_message(context):
    # message = choice(
    #     [ascii.SEXTOU_1, ascii.SEXTOU_2, ascii.SEXTOU_3, ascii.SEXTOU_4])
    message = f"```{figlet_format('SEXTOU', font=choice(ascii.ASCII_FONTS))}```"
    await context.send(message)


@client.hybrid_command(name="lyrics", with_app_command=True, description="AI AI AIAIAI 🔇 IAIAIAIAI ")
async def lyrics(context):
    message = discord.Embed(title="Sexta dos crias",
                            description=constants.SEXTA_DOS_CRIAS_LYRICS,
                            colour=discord.Colour.dark_blue())
    message.set_image(url=constants.SEXTOU_LYRICS_GIF)
    await context.send(embed=message)


@client.command("avatar")
async def send_avatar(context):
    message = discord.Embed(title="Sextouu?",
                            colour=discord.Colour.purple())
    message.set_image(url=constants.SEXTOU_AVATAR)
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
        url=constants.DJ_RAMON_SUCESSO_SPOTIFY_PIC)
    await context.send(embed=message)
    await context.send(embed=spotify_message)


@client.command("sexta?")
async def is_sexta(context):
    await context.send(choice([constants.IS_SEXTA_1, constants.IS_SEXTA_2,
                               constants.IS_SEXTA_3, constants.IS_SEXTA_4,
                               constants.IS_SEXTA_5, constants.IS_SEXTA_6,
                               constants.IS_SEXTA_7]))


@client.hybrid_command(name="hexa", with_app_command=True, description="Hexa dos Crias")
async def send_hexa(context):
    file_message = await context.send(file=discord.File(constants.HEXA_DOS_CRIAS_MP4))

    for emoji in ["🇧🇷", "🇭", "🇪", "🇽", "🇦"]:
        await file_message.add_reaction(emoji)


@client.hybrid_command(name="help", with_app_command=True, description="Exibe os todos os comandos")
async def help_message(context):
    message = discord.Embed(title="Comandos 🗡🗡💨",
                            colour=discord.Colour.dark_purple())
    message.set_footer(text="AI AI AIAIAI 🔇 IAIAIAIAI \n(SEGUUU 🗡🗡💨 RA) \nhttps://discord.gg/5d8eqqkC")

    message.add_field(name='Server do bot',
                      value="Qualquer duvida ou curiosidade, [suporte do bot](https://discord.gg/5d8eqqkC): "
                            "https://discord.gg/5d8eqqkC",
                      inline=False)
    options = []

    for com in command.get_help_commands():
        options.append(
            discord.SelectOption(
                label=com.name,
                description=com.description
            )
        )

        description = f"❂ {com.description}"
        if com.parameters is not None:
            description += "\n ❂ Parâmetros opcionais: "
            for ad_param in com.parameters:
                description += f'{ad_param}, '
            description = description[0: len(description) - 2]

        if com.aliases is not None:
            description += "\n ❂ Outros nomes desse comando: "
            for alias in com.aliases:
                description += f'{alias}, '
            description = description[0: len(description) - 2]

        message.add_field(name=f'$ {com.name}',
                          value=description,
                          inline=True)

    select = Select(placeholder="Escolha um comando",
                    min_values=1,
                    max_values=1,
                    options=options)

    async def my_callback(interaction):
        cmd = client.get_command(select.values[0])
        try:
            can_run = await cmd.can_run(context)
            if can_run:
                await context.invoke(cmd)
            else:
                context.send("Esse comando não pode ser executado pelo menu, tente com o prefixo $ ")
        except:
            context.send("Esse comando não pode ser executado pelo menu, tente com o prefixo $ ")

        await interaction.response.defer()  # comando para responder a mensagem e não causar falha na interação

    select.callback = my_callback
    view = View()
    view.add_item(select)
    view.on_error = None

    await context.send(embed=message, view=view)


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


# region Voice chat

@client.hybrid_command(name="play", with_app_command=True, description="Sexta dos crias no chat de voz")
async def play_sextou(context):
    await play_sound(constants.SEXTA_DOS_CRIAS_SOUND_MP3, context)


async def play_sound(file_name, context):
    connect = True
    connected_channel = discord.utils.get(client.voice_clients,
                                          guild=context.guild)

    if connected_channel is None:
        connect = await join_channel(context)

    if connect:
        channel = discord.utils.get(client.voice_clients, guild=context.guild)
        channel.play(
            discord.FFmpegPCMAudio(executable=constants.FFMPEG_PATH,
                                   source=file_name))
        return True
    else:
        await context.send("Você deve estar conectado a um canal de voz")


async def join_channel(context):
    author_voice = context.message.author.voice
    if author_voice is not None:
        await author_voice.channel.connect()
        return True
    else:
        return False


@client.hybrid_command(name="leave", with_app_command=True, description="Sai do chat de voz")
async def disconnect(context):
    channel = discord.utils.get(client.voice_clients, guild=context.guild)
    if channel is not None:
        await channel.disconnect(force=True)


@client.hybrid_command(name="stop", with_app_command=True, description="Para o som que estiver tocando no chat de voz")
async def stop_playing(context):
    channel = discord.utils.get(client.voice_clients, guild=context.guild)
    if channel is not None:
        channel.stop()


# endregion

client.run(os.environ["BOT_TOKEN"])
