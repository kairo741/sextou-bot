def get_help_commands():
    return [Command("sextou", "Sextouuuu", ["complete"], None), Command("lyrics", "Letra da música", None, None)]


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
