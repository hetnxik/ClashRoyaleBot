import disnake
import requests
from disnake.ext import commands


class Clan(commands.Cog):

    def __init__(self, client: commands.Bot):
        self.client = client

    @commands.slash_command(name="clan", description="Get info about a clan!")
    async def clan(self, inter: disnake.ApplicationCommandInteraction, tag: str):
        headers = {
            "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6IjE5MWNjZGJjLTkxOTQtNGFjMy1iODM2LTg5N2MwMzg0N2VkNyIsImlhdCI6MTY1OTI0MTI0MCwic3ViIjoiZGV2ZWxvcGVyLzQwZDEwMGNlLWJlMDItYjE2ZC0xOTE0LWZjMTY3YTQ1ODM1YyIsInNjb3BlcyI6WyJyb3lhbGUiXSwibGltaXRzIjpbeyJ0aWVyIjoiZGV2ZWxvcGVyL3NpbHZlciIsInR5cGUiOiJ0aHJvdHRsaW5nIn0seyJjaWRycyI6WyI0NS43OS4yMTguNzkiXSwidHlwZSI6ImNsaWVudCJ9XX0.xKggFnrjgYcennASoA-mnACYuDb_Oi9QgTFHY-shiO-fOSrYsvUKItYEZYB2qh-ECuoS7Uv307ZY2oOKc2wBNQ"}
        response = requests.get(url=f"https://proxy.royaleapi.dev/v1/clans/%23{tag}", headers=headers)
        if response.status_code == 200:
            info = response.json()
            clanEmbed = disnake.Embed(title="Clan Information.", description=f"Name: **{info['name']}**\nTag: **{info['tag']}**")
            clanEmbed.add_field(name=f"Type:", value=f"{info['type']}")
            clanEmbed.add_field(name="Description:", value=f"{info['description']}")
            clanEmbed.add_field(name="Clan War Trophies:", value=f"{info['clanWarTrophies']}", inline=False)
            clanEmbed.add_field(name="Location:", value=f"{info['location']['name']}", inline=False)
            clanEmbed.add_field(name="Required Trophies:", value=f"{info['requiredTrophies']}", inline=False)
            clanEmbed.add_field(name="Donations per Week:", value=f"{info['donationsPerWeek']}", inline=False)
            clanEmbed.add_field(name="Members:", value=f"{info['members']}", inline=False)
            await inter.response.send_message(embed=clanEmbed)
            print(response.text)
        else:
            await inter.response.send_message("Some error occurred while fetching the information.")
            print(response.text)


def setup(client: commands.Bot):
    client.add_cog(Clan(client))
