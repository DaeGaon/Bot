import discord
import asyncio
from discord.ext import commands
from discord.ext.commands import bot
from bs4 import BeautifulSoup
import requests
import os

bot = commands.Bot(command_prefix='~')

@bot.event
async def on_ready():
	print('등장')


@bot.command()
async def 롤(ctx, message):
	await ctx.send('https://www.op.gg/summoner/userName='+ message)

acess_token = os.environ["Bot_Token"]
bot.run(acess_token)
