import asyncio
from random import choice

import discord
from discord.ext import commands
from pyfiglet import figlet_format

from utils import constants, ascii


class OnReadyEvent(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.timeouts = {}  # {guild_id: asyncio.Task}

    @commands.Cog.listener()
    async def on_ready(self):
        await self.bot.change_presence(
            activity=discord.Streaming(
                name="SEXTA DOS CRIAS",
                url=constants.YT_1HOUR_URL
            )
        )
        try:
            synced = await self.bot.tree.sync()
            print(f'{len(synced)} slash commands foram sincronizados')
        except Exception as e:
            print(f"Erro ao sincronizar comandos: {e}")

        print(figlet_format('SEXTOU', font=choice(ascii.ASCII_FONTS)))

    async def schedule_disconnect(self, guild_id, vc, timeout=30):
        """Agenda desconexão após período de inatividade com verificação contínua"""
        if guild_id in self.timeouts:
            self.timeouts[guild_id].cancel()

        async def disconnect_task():
            try:
                while True:
                    await asyncio.sleep(timeout)  # Espera o período de timeout
                    print(f"Esperou {timeout}...")

                    # Verifica as condições atuais
                    if not vc.is_connected():
                        break  # Sai se já desconectado

                    if vc.is_playing() or vc.is_paused():
                        # Se estiver tocando, continua o loop e verifica novamente depois
                        continue

                    # Condições para desconexão atendidas
                    await vc.disconnect()
                    break

            except Exception as e:
                print(f"Erro no disconnect_task: {e}")
            finally:
                self.timeouts.pop(guild_id, None)

        self.timeouts[guild_id] = asyncio.create_task(disconnect_task())

    @commands.Cog.listener()
    async def on_voice_state_update(self, member, before, after):
        """Monitora mudanças de estado de voz para gerenciar desconexão automática"""

        if member.id == self.bot.user.id:
            # Quando o bot entra em um canal, inicia o timer
            if after.channel:
                vc = member.guild.voice_client
                if vc and not vc.is_playing():
                    await self.schedule_disconnect(member.guild.id, vc)
            # Quando o bot sai, limpa os timers
            elif before.channel:
                self._cleanup_timeout(member.guild.id)
            return
        # Ignora se não for um usuário humano
        if member.bot:
            return

        # Verifica todos os canais onde o bot está conectado
        for guild in self.bot.guilds:
            vc = guild.voice_client
            if not vc:
                continue

            # Se o bot foi desconectado manualmente
            if not vc.is_connected():
                self._cleanup_timeout(guild.id)
                continue

            human_members = [m for m in vc.channel.members if not m.bot]

            # Se não há mais humanos no canal
            if not human_members:
                await self.schedule_disconnect(guild.id, vc)
            # Se humanos voltaram e há timer ativo
            elif guild.id in self.timeouts:
                self._cleanup_timeout(guild.id)

    def _cleanup_timeout(self, guild_id):
        """Limpa o timeout de forma segura"""
        if guild_id in self.timeouts:
            self.timeouts[guild_id].cancel()
            del self.timeouts[guild_id]


async def setup(bot):
    await bot.add_cog(OnReadyEvent(bot))
