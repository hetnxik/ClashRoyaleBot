import disnake
import requests
from disnake.ext import commands


class Basic(commands.Cog):

    def __init__(self, client: commands.Bot):
        self.client = client

    @commands.slash_command(name="profile", description="Check the stats of your account!")
    async def basicStats(self, inter: disnake.ApplicationCommandInteraction, tag: str) -> None:
        headers = {"Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6IjE5MWNjZGJjLTkxOTQtNGFjMy1iODM2LTg5N2MwMzg0N2VkNyIsImlhdCI6MTY1OTI0MTI0MCwic3ViIjoiZGV2ZWxvcGVyLzQwZDEwMGNlLWJlMDItYjE2ZC0xOTE0LWZjMTY3YTQ1ODM1YyIsInNjb3BlcyI6WyJyb3lhbGUiXSwibGltaXRzIjpbeyJ0aWVyIjoiZGV2ZWxvcGVyL3NpbHZlciIsInR5cGUiOiJ0aHJvdHRsaW5nIn0seyJjaWRycyI6WyI0NS43OS4yMTguNzkiXSwidHlwZSI6ImNsaWVudCJ9XX0.xKggFnrjgYcennASoA-mnACYuDb_Oi9QgTFHY-shiO-fOSrYsvUKItYEZYB2qh-ECuoS7Uv307ZY2oOKc2wBNQ"}

        response = requests.get(url=f"https://proxy.royaleapi.dev/v1/players/%23{tag}", headers=headers)
        if response.status_code == 200:
            info = response.json()
            base_embed = disnake.Embed(title=f"Stats for {info['name']}")
            base_embed.add_field(name="Trophies:", value=info["trophies"], inline=True)
            base_embed.add_field(name="Highest Trophies:", value=info["bestTrophies"], inline=True)
            base_embed.add_field(name="Battle Count:", value=info["battleCount"], inline=False)
            base_embed.add_field(name="Wins:", value=info["wins"], inline=True)
            base_embed.add_field(name="Three Crown Wins:", value=info["threeCrownWins"], inline=True)
            base_embed.add_field(name="Losses:", value=info["losses"], inline=True)
            base_embed.add_field(name="Clan:", value=info["clan"]["name"], inline=False)
            base_embed.add_field(name="Arena:", value=info["arena"]["name"])
            base_embed.add_field(name="Badges:", value=len(info["badges"]))
            base_embed.add_field(name="Achievements:", value=len(info["achievements"]))
            base_embed.add_field(name="Cards:", value=f'{len(info["cards"])}/107')
            base_embed.add_field(name="Favourite Card", value=info["currentFavouriteCard"]["name"])
            url: str = info["currentFavouriteCard"]["iconUrls"]["medium"]
            print(url)
            base_embed.set_thumbnail(url=url)

            await inter.response.send_message(embed=base_embed)


def setup(client: commands.Bot):
    client.add_cog(Basic(client))
