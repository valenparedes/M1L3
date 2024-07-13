import discord
from bot_logic import gen_pass
# The intents variable stores the bot's priviliges
intents = discord.Intents.default()
# Enabling the message-reading privelege
intents.message_content = True
# Creating a bot in the client variable and transferring it the priveleges
client = discord.Client(intents=intents)
@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$hello'):
        await message.channel.send("Hi!")
    elif message.content.startswith('$bye'):
        await message.channel.send("\U0001f642")
    else:
        await message.channel.send("Tu contraseña es: " + gen_pass(10))
client.run("MTI0MDExMjc0NTI0ODk4NTE2OQ.GvKZYD.v4_j4SLIeAS8SdrasZV3CANnjbeUZB_svErmPY")