from random import choice

import discord
from discord.ext import commands

from utils import constants


class Video(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.hybrid_command(name="sextou", with_app_command=True, description="Sextouuu 🎉")
    @discord.app_commands.describe(version="Versão do vídeo (NORMAL, COMPLETE ou ALTERNATIVE)")
    async def send_sextou(self, context: commands.Context, version: str = "NORMAL"):
        """Envia o vídeo de sexta-feira baseado na versão escolhida."""
        await context.defer()  # Deferindo a resposta para evitar timeout

        video_mapping = {
            "COMPLETE": constants.SEXTA_DOS_CRIAS_MP4_COMPLETE_EDITION,
            "ALTERNATIVE": constants.SEXTA_DOS_CRIAS_MP4_ALTERNATIVE_EDITION,
            "NORMAL": constants.SEXTA_DOS_CRIAS_MP4
        }

        file_path = video_mapping.get(version.upper(), constants.SEXTA_DOS_CRIAS_MP4)
        await context.send(file=discord.File(file_path))

    @commands.hybrid_command(name="shrek", with_app_command=True, description="Graças a Deus é sexta-feira")
    async def send_shrek(self, context: commands.Context):
        await context.defer()
        await context.send(file=discord.File(constants.SHREK_SEXTA_FEIRA_MP4))

    @commands.hybrid_command(name="urso", with_app_command=True, description="Urso da semana da sexta")
    @commands.cooldown(1, 35, commands.BucketType.user)
    async def send_urso(self, context: commands.Context):
        await context.defer()
        await context.send(file=discord.File(choice([constants.URSO_DA_SEXTA_MP4, constants.URSO_DA_MAMAR_MP4,
                                                     constants.URSO_DA_PISEIRO_MP4, constants.URSO_DA_EX_MP4,
                                                     constants.ATXES_AD_OSRU_MP4, constants.URSO_ESTOURADO_MP4,
                                                     constants.URSO_DA_sexTA_MP4, constants.URSO_REMASTER_MP4])))

    @send_urso.error
    async def send_urso_error(self, context: commands.Context, error):
        if isinstance(error, commands.CommandOnCooldown):
            await context.send(f"Espere {round(error.retry_after, 2)} segundos antes de enviar outro vídeo.",
                               ephemeral=True)

    @commands.hybrid_command(name="rockers", with_app_command=True, description="Rooockkkkers SEXTOoOoUuU")
    async def send_rockers(self, context: commands.Context):
        await context.defer()
        await context.send(file=discord.File(constants.ROCKERS_SEXTOU_MP4))

    @commands.hybrid_command(name="fring", with_app_command=True, description="Holy shit it's fring friday!")
    async def send_fring(self, context: commands.Context):
        await context.defer()
        await context.send(file=discord.File(constants.FRING_FRIDAY_MP4))


async def setup(bot):
    """Função assíncrona para adicionar este cog ao bot."""
    await bot.add_cog(Video(bot))
