import discord
import requests
from urllib.parse import quote
from discord.ext import commands

client = discord.Client()

client = commands.Bot(command_prefix = '!')


@client.command()
async def chatbot(ctx, msg):
  url = f"https://chatbot-api.gq/?message={quote(msg)}"
  data = requests.get(url)
  await ctx.send(data.text)


client.run("TOKEN HERE")
