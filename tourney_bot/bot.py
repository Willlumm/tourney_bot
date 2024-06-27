import discord

import config
# from tourney import Tourney

class TourneyClient(discord.Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.state = "idle"
        self.participants = {}
        self.entries = 4

    async def on_ready(self):
        print(f"Logged in as {self.user}")

    async def on_message(self, message):
        if message.author.id == self.user.id:
            return

        elif self.state != "idle" and message.content.startswith("!stop"):
            await message.channel.send("Stopping tourney.")
            self.state = "idle"

        elif self.state == "idle" and message.content.startswith("!setup"):
            await message.channel.send("Setting up tourney!\nWaiting for participants to respond...")
            for member in message.mentions:
                self.participants[member] = []
                await member.send(f"Please enter {self.entries} nominations:")
            self.state = "awaiting nominations"

        elif self.state == "awaiting nominations" and message.author in self.participants:
            nominations = message.content.split("\n")
            self.participants[message.author] += nominations
            if len(self.participants[message.author]) >= self.entries:
                await message.channel.send("Thank you for your nominations!")
            if all(len(entries) >= self.entries for entries in self.participants.values()):
                self.state == "voting"

            
intents = discord.Intents.default()
intents.message_content = True

client = TourneyClient(intents=intents)
client.run(config.token)
