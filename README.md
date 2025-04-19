# 🤖 Sextou Bot

Um bot do Discord feito com amor, música e comandos bizarros — especialmente preparado para sextar!

![um gif do vídeo principal do comando "sextou" do bot](https://c.tenor.com/yenNqRV0M2oAAAAC/sexta-sexta-feira.gif "Gif Sextou")

## 🌳 Estrutura do Projeto

```
sextou-bot/
├── cogs/                         # Módulos (comandos e funcionalidades)
│   ├── __init__.py
│   ├── general.py                # Comandos gerais
│   ├── video.py                  # Comandos relacionados a vídeos
│   ├── sound.py                  # Comandos relacionados a sons
│   ├── stats.py                  # Comandos relacionados a status
│   ├── api.py                    # Integração com APIs externas
│   │── movies/                   # Funcionalidades relacionadas à API TheMovieDB
│   │── spotify/                  # Funcionalidades relacionadas à API do Spotify
│   └── models/
│       └── command_model.py      # Modelos de dados utilizados pelos cogs
│
├── database/                     # Banco de dados do bot (EM DESENV)
│   └── __init__.py
│
├── events/                       # Eventos do bot
│   ├── __init__.py
│   ├── on_ready.py               # Ações ao iniciar o bot
│   ├── on_message.py             # Processamento de mensagens
│   └── on_member_join.py         # Mensagens de boas-vindas (EM DESENV)
│
├── utils/                        # Utilitários e helpers
│   ├── __init__.py
│   ├── ascii.py                  # Fontes ASCII para o figlet
│   └── constants.py              # Constantes globais (URLs, emojis, etc.)
│
├── files/                        # Arquivos estáticos utilizados pelo bot
│   ├── images/
│   ├── videos/
│   └── sounds/
│
├── main.py                       # Ponto de entrada do bot
├── .env                          # Variáveis de ambiente (como tokens)
├── requirements.txt              # Dependências do projeto
└── README.txt                    # Este arquivo
```

## 🛠️ Como rodar

1. Instale as dependências:

```bash
pip install -r requirements.txt
```

2. Configure seu `.env` com as chaves necessárias (exemplo: `DISCORD_TOKEN`, `THEMOVIEDB_TOKEN`).

3. Rode o bot:

```bash
python main.py
```

## 📦 Bibliotecas principais

- `discord.py` (core)
- `aiohttp` (para chamadas async externas)
- `pyfiglet` (arte ASCII)

## 📜 Comandos Disponíveis

| Comando              | Descrição                                               | Parâmetros                |
|----------------------|---------------------------------------------------------|---------------------------|
| `$ sextou`           | Sextouuuu 🔥                                            | `complete`, `alternative` |
| `$ lyrics`           | Letra da música                                         | —                         |
| `$ shrek`            | Graças a Deus é sexta-feira                             | —                         |
| `$ fring`            | Holy shit It's Fring Friday                             | —                         |
| `$ rockers`          | Rooockkkkers SEXTOoOoUuU                                | —                         |
| `$ urso`             | Urso da semana da sexta                                 | —                         |
| `$ sound`            | MP3 do sexta dos crias                                  | —                         |
| `$ message`          | ASCII aleatório desenhando "Sextou"                     | —                         |
| `$ sexta?`           | Memes boomers horríveis de sextou                       | —                         |
| `$ help`             | Manda essa mensagem                                     | —                         |
| `$ avatar`           | Envia a foto de perfil do bot                           | —                         |
| `$ info`             | Infos sobre o bot                                       | —                         |
| `$ play`             | Sexta dos crias no voice chat                           | —                         |
| `$ stop`             | Para de tocar enquanto está no voice                    | —                         |
| `$ leave`            | Sai do voice chat                                       | —                         |
| `$ filme`            | Envia uma sugestão de filme para assistir               | —                         |
| `$ serie`            | Envia uma sugestão de série para assistir               | —                         |
| `$ pode_sextar`      | Exibe quanto tempo falta para a *Sexta*                 | —                         |
| `$ sextou_historico` | Exibe um fato histórico que ocorreu em uma sexta-feira! | —                         |
| `$ status_sextou`    | Mostra se a sexta está boa ou não...                    | `me`                      |

---

Desenvolvido com muitas segundas contando os segundos para as sextas por [@KairoAmorim](https://www.github.com/kairo741)

Com a benção sonora do inigualável [DJ Ramon Sucesso](https://www.instagram.com/djramonsucessofc/). 🎶🔥