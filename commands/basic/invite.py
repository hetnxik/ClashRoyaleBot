import disnake
from disnake.ext import commands


class Invite(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client

    @commands.slash_command(name="invite", description="Get the invite link to add the bot to one of your servers!")
    async def invite(self, inter: disnake.ApplicationCommandInteraction):
        link = "xyz"
        await inter.response.send_message(f"Here is the invite link of the bot - {link}")


def setup(client: commands.Bot):
    client.add_cog(Invite(client))
