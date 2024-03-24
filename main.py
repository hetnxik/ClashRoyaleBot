import os

from dotenv import load_dotenv
import disnake
from disnake.ext import commands

intents = disnake.Intents.all()
client = commands.Bot(command_prefix="cr.", intents=intents, case_insensitive=True, status=disnake.Status.dnd, activity=disnake.Activity(type=disnake.ActivityType.playing, name="Clash Royale"))


@client.event
async def on_ready():
    print("ready")

load_dotenv()
token = os.getenv("TOKEN")

for folder in os.listdir("./commands"):
    if not folder.startswith("."):
        for file in os.listdir(f"./commands/{folder}"):
            if file.endswith(".py") and not file.startswith("_") and not file.startswith("."):
                client.load_extension(f"commands.{folder}.{file[:-3]}")
                print(f"loaded category: {file}")

client.run(token)
