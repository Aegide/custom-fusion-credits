import discord
from discord import app_commands


intents = discord.Intents.default()
intents.guild_messages = True
intents.members = True
intents.message_content = True
bot = discord.Client(intents=intents)
tree = app_commands.CommandTree(bot)


@bot.event
async def on_ready():
    global bot_id
    await tree.sync()
    app_info = await bot.application_info()
    bot_id = app_info.id
    permission_id = "65536"
    print("\n\nReady! bot invite:\n\nhttps://discordapp.com/api/oauth2/authorize?client_id=" + str(bot_id) + "&permissions=" + permission_id + "&scope=bot\n\n")


@tree.command(name="quoi", description="what")
async def chat(interaction: discord.Interaction, *, message: str):
    if interaction.user == bot.user:
        return
    await interaction.response.send_message("feur")


@tree.command(name="where", description="où")
async def chat(interaction: discord.Interaction):
    if interaction.user == bot.user:
        return
    channel = await interaction.channel._get_channel()
    await interaction.response.send_message(channel.name)


def get_discord_token():
    return open("./token/discord.txt").read().rstrip()


if __name__== "__main__" :
    discord_token = get_discord_token()
    bot.run(discord_token)
