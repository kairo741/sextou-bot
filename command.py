def get_help_commands():
    return [
        Command("sextou", "Sextouuuu 🔥", ["complete"], None),
        Command("lyrics", "Letra da música", None, None),
        Command("shrek", "Graças a Deus é sexta-feira", None, None),
        Command("fring", "Holy shit It's Fring Friday", None, None),
        Command("message", "ASCII aleatório desenhando \"Sextou\"", None, None),
        Command("sexta?", "Memes boomers horríveis de sextou", None, None),
        Command("help", "Manda essa mensagem", None, None),
        Command("avatar", "Envia a foto de perfil do bot", None, None),
        Command("playlist", "(off) Cria uma playlist no Spotify", ["rock", "pop", "metal", "etc"], None),
        Command("info", "Infos sobre o bot", None, ["infos", "author", "authors", "bot"]),
    ]


class Command:

    def __init__(self, name, description, parameters, aliases):
        """
        :param name (str): Nome do comando
        :param description (str): Descrição do comando
        :param parameters (array): Parâmetros opcionais
        :param aliases (str): Outros nomes para o comando
        """
        self.name = name
        self.description = description
        self.parameters = parameters
        self.aliases = aliases

    def __str__(self):
        return self.name
