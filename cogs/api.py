import datetime
from random import choice, randint
import os
import discord
import requests
from datetime import timedelta
from discord.ext import commands
from cogs.movies import shows_service as show_service

shows_service = show_service.ShowsService(os.environ["THEMOVIEDB_TOKEN"])


class ApiConsumer(commands.Cog):
    def __init__(self, client):
        self.client = client

    def get_historic_friday_event(self):
        mm = str(randint(1, 12)).zfill(2)
        dd = str(randint(1, 31 if mm != '02' else 28)).zfill(2)

        url = f"https://pt.wikipedia.org/api/rest_v1/feed/onthisday/all/{mm}/{dd}"
        response = requests.get(url)

        if response.status_code == 200:
            events = response.json()["events"]
            if events:
                friday_events = []
                month = int(mm)
                day = int(dd)
                for event in events:
                    year = event["year"]
                    try:
                        event_date = datetime.date(year, month, day)
                        if event_date.weekday() == 4:  # Verifica se é sexta-feira
                            friday_events.append(event)
                    except ValueError:
                        continue  # Ignora datas inválidas

                if friday_events:
                    random_event = choice(friday_events)
                    thumbnail = random_event["pages"][0]["originalimage"]['source']
                    final_date = datetime.date(random_event["year"], month, day)
                    return random_event['text'], thumbnail, final_date
            else:
                return "Não encontrei eventos históricos de sexta-feira para hoje! 😢"
        else:
            return "Erro ao buscar eventos históricos! 🚨"

    @commands.hybrid_command(name="sextou_historico", with_app_command=True,
                             description="Exibe um fato histórico que ocorreu em uma sexta-feira!")
    async def historic_friday(self, context: commands.Context):
        await context.defer()
        description, thumbnail, date = self.get_historic_friday_event()
        timestamp = datetime.datetime.combine(date, datetime.datetime.min.time(), tzinfo=datetime.timezone.utc)
        timestamp.replace(hour=0, minute=0, second=0, microsecond=0)
        embed = discord.Embed(title=f'📅 Na sexta-feira de **{date.strftime("%d/%m/%Y")}**',
                              colour=discord.Colour.random(),
                              description=description, timestamp=timestamp)
        embed.set_image(url=thumbnail)
        await context.send(embed=embed)

    # region Movies/Series

    @commands.hybrid_command(name="filme", with_app_command=True,
                             description="Envia uma sugestão de filme para assistir")
    async def send_show(self, context: commands.Context):
        await context.defer()
        show = shows_service.get_one_popular_movie_detailed()

        message = discord.Embed(title=f'🎥 {show.title}', colour=discord.Colour.random())

        message.add_field(name=f'Avaliação:',
                          value=f'⭐ | {(show.vote_average * 10):.2f}%',
                          inline=False)
        message.add_field(name='Classificação:',
                          value=f'🔞 | Filme +18' if show.adult else f'🟩 | Livre para todos os públicos',
                          inline=False)

        message.add_field(name=f'Data de lançamento',
                          value=f'🗓️ | {datetime.datetime.strptime(show.release_date, "%Y-%m-%d").strftime("%d/%m/%Y")}',
                          inline=False)
        message.add_field(name=f'Duração',
                          value=f'⌛ | {str(timedelta(minutes=show.runtime))[:-3]}h',
                          inline=False)
        genres_message = ""
        for genre in show.genres:
            genres_message += f'• {genre["name"]}\n'

        if genres_message != "":
            message.add_field(name=f'Gênero(s)',
                              value=genres_message,
                              inline=False)

        if show.overview != "":
            message.add_field(name=f'Sinopse',
                              value=f'📄 | {show.overview}',
                              inline=False)

        message.set_image(url=f'https://image.tmdb.org/t/p/original{show.poster_path}')
        await context.send(embed=message)

    @commands.hybrid_command(name="serie", with_app_command=True,
                             description="Envia uma sugestão de série para assistir")
    async def send_show(self, context: commands.Context):
        await context.defer()
        show = shows_service.get_one_popular_show_detailed()

        message = discord.Embed(title=f'🎥 {show.name}', colour=discord.Colour.random())

        message.add_field(name=f'Avaliação:',
                          value=f'⭐ | {(show.vote_average * 10):.2f}%',
                          inline=False)
        message.add_field(name='Classificação:',
                          value=f'🔞 | Série +18' if show.adult else f'🟩 | Livre para todos os públicos',
                          inline=False)

        if show.first_air_date != "":
            message.add_field(name=f'1° episódio lançado',
                              value=f'🗓️ | {datetime.datetime.strptime(show.first_air_date, "%Y-%m-%d").strftime("%d/%m/%Y")}',
                              inline=True)
        if show.last_air_date != "":
            message.add_field(name=f'Último episódio lançado',
                              value=f'🗓️ | {datetime.datetime.strptime(show.last_air_date, "%Y-%m-%d").strftime("%d/%m/%Y")}',
                              inline=True)

        # Pular uma linha
        message.add_field(name=f'',
                          value=f'',
                          inline=False)

        message.add_field(name=f'Número de episódios',
                          value=f'🔢 | {show.number_of_episodes}',
                          inline=True)
        message.add_field(name=f'Número de temporadas',
                          value=f'🔢 | {show.number_of_seasons}',
                          inline=True)
        genres_message = ""
        for genre in show.genres:
            genres_message += f'• {genre["name"]}\n'

        if genres_message != "":
            message.add_field(name=f'Gênero(s)',
                              value=genres_message,
                              inline=False)

        if show.overview != "":
            message.add_field(name=f'Sinopse',
                              value=f'📄 | {show.overview}',
                              inline=False)

        if show.homepage != "":
            message.add_field(name=f'URL',
                              value=f"🔗 | [Acessar]({show.homepage})",
                              inline=False)

        message.set_image(url=f'https://image.tmdb.org/t/p/original{show.poster_path}')
        await context.send(embed=message)

    # endregion


async def setup(bot):
    """Função assíncrona para adicionar este cog ao bot."""
    await bot.add_cog(ApiConsumer(bot))
