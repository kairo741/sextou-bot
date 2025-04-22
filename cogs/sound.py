import discord
from discord.ext import commands

from utils import constants


class Sound(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.hybrid_command(name="sound", with_app_command=True, description="Sexta dos crias sound")
    async def send_sound(self, context: commands.Context):
        await context.defer()
        await context.send(file=discord.File(constants.SEXTA_DOS_CRIAS_SOUND_MP3))

    # region Voice chat

    @commands.hybrid_command(name="play", with_app_command=True, description="Sexta dos crias no chat de voz")
    @discord.app_commands.describe(duration="Customização da duração do som")
    async def play_sextou(self, context: commands.Context, duration: int = None):
        await context.defer(ephemeral=True)
        await self.play_sound(constants.SEXTA_DOS_CRIAS_SOUND_MP3, context, duration)

    async def play_sound(self, file_name, context: commands.Context, duration: int):
        try:
            connect = True
            connected_channel = discord.utils.get(self.client.voice_clients, guild=context.guild)

            if connected_channel is None:
                connect = await self.join_channel(context)

            if connect:
                channel: discord.VoiceClient = discord.utils.get(self.client.voice_clients, guild=context.guild)
                if channel:
                    ffmpeg_options = {'executable': 'ffmpeg'}
                    if duration:
                        ffmpeg_options['options'] = f'-t {duration}'  # Limita a duração

                    source = discord.FFmpegPCMAudio(source=file_name, **ffmpeg_options)
                    channel.play(source)
                    if context.interaction:
                        await context.interaction.edit_original_response(content=constants.SEXTA_DOS_CRIAS_LYRICS)
                else:
                    await context.send("Falha ao conectar ao canal de voz.", ephemeral=True)
            else:
                await context.send("Você deve estar conectado a um canal de voz.", ephemeral=True)
        except Exception as e:
            await context.send(f"Erro ao tentar tocar música: {e}", ephemeral=True)
            print(f"Erro: {e}")

    async def join_channel(self, context: commands.Context):
        author_voice = context.message.author.voice
        if author_voice is not None:
            await author_voice.channel.connect()
            return True
        else:
            return False

    @commands.hybrid_command(name="leave", with_app_command=True, description="Sai do chat de voz")
    async def disconnect(self, context: commands.Context):
        await context.defer(ephemeral=True)
        channel: discord.VoiceClient = discord.utils.get(self.client.voice_clients, guild=context.guild)
        if channel is not None:
            await channel.disconnect(force=True)
            if context.interaction:
                await context.interaction.delete_original_response()

    @commands.hybrid_command(name="stop", with_app_command=True,
                             description="Para o som que estiver tocando no chat de voz")
    async def stop_playing(self, context: commands.Context):
        await context.defer(ephemeral=True)
        channel: discord.VoiceClient = discord.utils.get(self.client.voice_clients, guild=context.guild)
        if channel is not None:
            channel.stop()
            if context.interaction:
                await context.interaction.delete_original_response()

    # endregion


async def setup(bot):
    """Função assíncrona para adicionar este cog ao bot."""
    await bot.add_cog(Sound(bot))
