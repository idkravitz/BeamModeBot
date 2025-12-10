# BeamModeBot

Clone of tg @HowGayBot

## Installation

```bash
poetry install
```

## Usage

```bash
poetry run beammodebot
```

# Config

It expects either a `.env` file or real ENV vars to exist at runtime. The env vars are:

`BOT_TOKEN` - token you obtain from `@BotFather`
`api_id` - mtproto API id, refer to telethon docs on how to obtain it
`api_hash` - mtproto API hash, refer to telethon docs on how to obtain it
`DEV_MODE` (OPTIONAL) - either `true` or `false`, case insensitive, used to display hidden percentage right in article description (If you don't know what the hell I'm talking about, just check the code)

Also, if `userlist.txt` is present at the project root directory, it is treated as a text file with user names used in fake raffles (top5, bottom5 and spin the wheel)

## Development

This project uses Poetry for dependency management. Code style doesn't exist, structuring is questionable

