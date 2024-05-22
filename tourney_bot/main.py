import discord

import config

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f"Logged in as {client.user}")

@client.event
async def on_message(message):
    
    if not message.content.startswith("!"):
        return
    
    if message.content.startswith("!hello"):
        await message.channel.send(f"Hello {message.author.mention}!")

    if message.content.startswith("!setup"):
        print(message.mentions)
        # await message.channel.send(f"Hello {message.author.mention}!")
client.run(config.token)


