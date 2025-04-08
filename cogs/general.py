import asyncio
import datetime
from random import choice

import discord
from discord.ext import commands
from discord.ui import Select, View
from pyfiglet import figlet_format

from utils import constants, ascii
from .models.command_model import get_help_commands


class General(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=['info', 'infos', 'author', 'authors', 'bot'])
    async def send_author_info(self, context: commands.Context):
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

    @commands.command("avatar")
    async def send_avatar(self, context: commands.Context):
        message = discord.Embed(title="Sextouu?", colour=discord.Colour.purple())
        message.set_image(url=constants.SEXTOU_AVATAR)
        await context.send(embed=message)

    @commands.hybrid_command(name="message", with_app_command=True, description="ASCII aleatório desenhando \"Sextou\"")
    async def send_message(self, context: commands.Context):
        # message = choice(
        #     [ascii.SEXTOU_1, ascii.SEXTOU_2, ascii.SEXTOU_3, ascii.SEXTOU_4])
        message = f"```{figlet_format('SEXTOU', font=choice(ascii.ASCII_FONTS))}```"
        await context.send(message)

    @commands.hybrid_command(name="lyrics", with_app_command=True, description="AI AI AIAIAI 🔇 IAIAIAIAI ")
    async def lyrics(self, context: commands.Context):
        message = discord.Embed(title="Sexta dos crias",
                                description=constants.SEXTA_DOS_CRIAS_LYRICS,
                                colour=discord.Colour.dark_blue())
        message.set_image(url=constants.SEXTOU_LYRICS_GIF)
        await context.send(embed=message)

    @commands.hybrid_command(name="help", with_app_command=True, description="Exibe os todos os comandos")
    async def help_message(self, context: commands.Context):
        await context.defer()
        message = discord.Embed(title="Comandos 🗡🗡💨",
                                colour=discord.Colour.dark_purple())
        message.set_footer(text="AI AI AIAIAI 🔇 IAIAIAIAI \n(SEGUUU 🗡🗡💨 RA) \nhttps://discord.gg/5d8eqqkC")

        message.add_field(name='Server do bot',
                          value="Qualquer duvida ou curiosidade, [suporte do bot](https://discord.gg/5d8eqqkC): "
                                "https://discord.gg/5d8eqqkC",
                          inline=False)
        options = []

        for com in get_help_commands():
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

            message.add_field(name=f'$ `{com.name}`',
                              value=description,
                              inline=True)

        select = Select(placeholder="Escolha um comando",
                        min_values=1,
                        max_values=1,
                        options=options)

        async def my_callback(interaction):
            cmd = self.client.get_command(select.values[0])
            try:
                can_run = await cmd.can_run(context)
                if can_run:
                    await context.invoke(cmd)
                else:
                    await context.send("Esse comando não pode ser executado pelo menu, tente com o prefixo $ ")
            except:
                await context.send("Esse comando não pode ser executado pelo menu, tente com o prefixo $ ")

            await interaction.response.defer()  # comando para responder a mensagem e não causar falha na interação

        select.callback = my_callback
        view = View()
        view.add_item(select)
        view.on_error = None

        await context.send(embed=message, view=view)

    @commands.hybrid_command("pode_sextar", with_app_command=True, description="Já pode Sextar ou ta cedo?")
    async def time_until_sexta(self, context: commands.Context):
        hours, minutes, seconds, timestamp = self.calculate_time_until_sexta_6pm()
        timer = 60 if hours <= (168 - 7) else 30  # Em segundos
        embed = self.generate_timer_embed(hours, minutes, seconds)
        message = await context.send(embed=embed)
        while timer >= 0:
            hours, minutes, seconds, timestamp = self.calculate_time_until_sexta_6pm()
            await asyncio.sleep(timer / 60)
            embed = self.generate_timer_embed(hours, minutes, seconds)
            await message.edit(embed=embed)
            timer -= 1
        embed = self.generate_timer_embed(hours, minutes, seconds, f'Você poderá **SEXTAR** <t:{timestamp}:R>!!')
        await message.edit(embed=embed)

    def generate_timer_embed(self, hours, minutes, seconds, last_text=None):
        if hours <= (168 - 7):
            text = f"Faltam exatas **[{hours:02}:{minutes:02}:{seconds:02}h]({constants.YT_1HOUR_URL})** para **SEXTAR**!!!"
            return discord.Embed(title="Já pode sextar ou ta muito cedo?",
                                 description=text if last_text is None else last_text,
                                 colour=discord.Colour.dark_teal()).set_image(url=constants.MONKEY_GIF)
        else:
            return (discord.Embed(
                title=choice(constants.SEXTOU_TITLES),
                description=f"Ｆｉｎａｌｍｅｎｔｅ **ＳＥＸＴＯＵ** ｐｏｒｒａａａａａ!!!",
                colour=discord.Colour.random()).set_image(url=constants.SEXTOU_LYRICS_GIF)
                    .set_footer(text="AI AI AIAIAI 🔇 IAIAIAIAI \n(SEGUUU 🗡🗡💨 RA) \nhttps://discord.gg/5d8eqqkC"))

    def calculate_time_until_sexta_6pm(self):
        today = datetime.datetime.now()
        # Sexta-feira é o dia 4 da semana (segunda-feira é 0)
        days_ahead = 4 - today.weekday()
        if days_ahead <= 0:  # Se hoje é sexta-feira ou depois, conta para a próxima sexta
            days_ahead += 7

        # Define a próxima sexta-feira às 00:00 (meia-noite)
        next_friday = today + datetime.timedelta(days=days_ahead)
        next_friday = next_friday.replace(hour=18, minute=0, second=0, microsecond=0)
        # Calcula a diferença de tempo até a próxima sexta 18h
        time_difference = next_friday - today

        # Extrair horas, minutos e segundos da diferença de tempo
        total_seconds = int(time_difference.total_seconds())
        hours, remainder = divmod(total_seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        timestamp = round(today.timestamp() + total_seconds)
        return hours, minutes, seconds, timestamp

    @commands.command("sexta?")
    async def is_sexta(self, context: commands.Context):
        await context.send(choice([constants.IS_SEXTA_1, constants.IS_SEXTA_2,
                                   constants.IS_SEXTA_3, constants.IS_SEXTA_4,
                                   constants.IS_SEXTA_5, constants.IS_SEXTA_6,
                                   constants.IS_SEXTA_7]))


async def setup(bot):
    """Função assíncrona para adicionar este cog ao bot."""
    await bot.add_cog(General(bot))
