import discord


intents = discord.Intents.default()
intents.guild_messages = True
intents.members = True
intents.message_content = True
bot = discord.Client(intents=intents)


@bot.event
async def on_ready():
    global bot_id
    app_info = await bot.application_info()
    bot_id = app_info.id
    permission_id = "65536"
    print("\n\nReady! bot invite:\n\nhttps://discordapp.com/api/oauth2/authorize?client_id=" + str(bot_id) + "&permissions=" + permission_id + "&scope=bot\n\n")


def get_discord_token():
    return open("../token/discord.txt").read().rstrip()


if __name__== "__main__" :
    discord_token = get_discord_token()
    bot.run(discord_token)
