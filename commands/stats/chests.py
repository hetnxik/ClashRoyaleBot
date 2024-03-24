import disnake
import requests
from disnake.ext import commands


class Chests(commands.Cog):

    def __init__(self, client: commands.Bot):
        self.client = client

    @commands.slash_command(name="upcomingchests", description="Check which chests you will be getting next!")
    async def chests(self, inter: disnake.ApplicationCommandInteraction, tag: str):
        headers = {
            "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6IjE5MWNjZGJjLTkxOTQtNGFjMy1iODM2LTg5N2MwMzg0N2VkNyIsImlhdCI6MTY1OTI0MTI0MCwic3ViIjoiZGV2ZWxvcGVyLzQwZDEwMGNlLWJlMDItYjE2ZC0xOTE0LWZjMTY3YTQ1ODM1YyIsInNjb3BlcyI6WyJyb3lhbGUiXSwibGltaXRzIjpbeyJ0aWVyIjoiZGV2ZWxvcGVyL3NpbHZlciIsInR5cGUiOiJ0aHJvdHRsaW5nIn0seyJjaWRycyI6WyI0NS43OS4yMTguNzkiXSwidHlwZSI6ImNsaWVudCJ9XX0.xKggFnrjgYcennASoA-mnACYuDb_Oi9QgTFHY-shiO-fOSrYsvUKItYEZYB2qh-ECuoS7Uv307ZY2oOKc2wBNQ"}
        response = requests.get(url=f"https://proxy.royaleapi.dev/v1/players/%23{tag}/upcomingchests", headers=headers)
        if response.status_code == 200:
            info = response.json()
            chestEmbed = disnake.Embed(title="Upcoming Chests.")
            for i in range(0, 4):
                chestEmbed.add_field(name=f"Chest after {int(info['items'][i]['index']) + 1} wins.",
                                     value=info['items'][i]['name'], inline=False)

            await inter.response.send_message(embed=chestEmbed)
        else:
            await inter.response.send_message("Some error occurred while fetching the requested information.")


def setup(client: commands.Bot):
    client.add_cog(Chests(client))



