from calendar import day_abbr, month
from datetime import datetime
from datetime import timedelta
from email import message
from mailbox import Message
import os
import time
from tkinter import COMMAND
import discord
import asyncio
from discord.ext import commands
from setuptools import Command


bot = commands.Bot(command_prefix='!')
bot.remove_command('help')

@bot.command()
async def help(ctx):
    embed = discord.Embed(
        title='Bot Commands',
        description='List of all the commands for the auction bot. Some commands will only be accessible by mods.'
    )
    embed.add_field(
        name='!auctioninfo',
        value='Gives info on the current auction',
        inline=False
    )
    embed.add_field(
        name='!bid',
        value='Places your bid on an auctioned item',
        inline=False
    )
    embed.add_field(
        name='!bidhist <user>',
        value='Shows history of a user`s bids',
        inline=False
    )
    embed.add_field(
        name='!biddel',
        value='Deletes your bid from an auctioned item',
        inline=False
    )
    embed.add_field(
        name='!create <item> <duration> <starting bid>',
        value='Creates an auction',
        inline=False
    )
    embed.add_field(
        name='!help',
        value='Shows the list of all commands',
        inline=False
    )
    embed.add_field(
        name='!leaderboard',
        value='Shows the bidding leaderboard for the current auction',
        inline=False
    )
    embed.add_field(
        name='!remove',
        value='Removes an auction',
        inline=False
    )
    await ctx.send(
        embed = embed
    )

@bot.command()
async def info(ctx):

    await ctx.send(ctx.guild)
    await ctx.send(ctx.author)
    await ctx.send(ctx.message.id)

CreationTime = '<t:{int(time.time())}:f>'
print(3)
@bot.command()
async def create(ctx, ItemName, AuctionDuration, StartingBid):
    
    EndingTime = CreationTime + (AuctionDuration * 86400)
    print(EndingTime)
    embedvar = discord.Embed(
        title=f'Auction Created for {ItemName}',
    )
    embedvar.add_field(
        name='Starting Bid',
        value=f'{StartingBid} nuggets',
        inline=True
    )
    embedvar.add_field(
        name='Duration',
        value=f'{AuctionDuration} days',
        inline=True
    )
    embedvar.add_field(
        name='Auction Creation Time',
        value=CreationTime,
        inline=True
    )
    embedvar.add_field(
        name='Auction End Time',
        value=EndingTime,
        inline=True
    )

    await ctx.send(
        embed=embedvar
    )


class AuctionBot(discord.Client):

    async def on_ready(self):
        print('Auction bot is now online!')




intents = discord.Intents.default()
intents.members = True

Client = AuctionBot(intents=intents)



bot.run('Insert Token Here')

Client.run('Insert Token Here')
