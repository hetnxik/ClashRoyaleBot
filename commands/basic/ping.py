import disnake
from disnake.ext import commands


class Ping(commands.Cog):

    def __init__(self, client: commands.Bot):
        self.client = client

    @commands.slash_command(name="ping", description="Check the latency of the bot.")
    async def ping(self, inter: disnake.ApplicationCommandInteraction):
        await inter.response.send_message(f"The latency of the bot is: {self.client.latency}ms")


def setup(client: commands.Bot):
    client.add_cog(Ping(client))
