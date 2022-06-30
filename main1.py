from calendar import day_abbr, month
from datetime import datetime
from datetime import timedelta
import json
import os
import time
from tkinter import COMMAND
from typing import ItemsView
from unicodedata import name
import discord
import asyncio
from discord.ext import commands
from setuptools import Command


bot = commands.Bot(command_prefix='!')

@bot.command()
async def abt(ctx):
    print(abt)
    embed_data = {
        "title": "Bot Commands",
        "description": "List of all the commands for the auction bot. Some commands will only be accessible by mods.",
        "fields": [
            {
                "name": '!abt',
                "value": 'Shows the list of all commands',
                "inline": False                
            },
            {
                "name": '!auctioninfo',
                "value": 'Gives info on the current auction',
                "inline": False
            },
            {
                "name": '!bid',
                "value": 'Places your bid on an auctioned item',
                "inline": False
            },
            {
                "name": '!bidhist <user>',
                "value": 'Shows history of a user`s bids',
                "inline": False
            },
            {
                "name": '!biddel',
                "value": 'Deletes your bid from an auctioned item',
                "inline": False
            },
            {
                "name": '!create <item> <duration> <starting bid>',
                "value": 'Creates an auction',
                "inline": False                
            },
            {
                "name": '!leaderboard',
                "value": 'Shows the bidding leaderboard for the current auction',
                "inline": False                
            },
            {
                "name": '!remove',
                "value": 'Removes an auction',
                "inline": False                
            }
        ]
    }

    await ctx.send(
        embed = discord.Embed.from_dict(embed_data)
    )
    
@bot.command()
async def info(ctx):

    await ctx.send(ctx.guild)
    await ctx.send(ctx.author)
    await ctx.send(ctx.message.id)




global CreationTime, EndingTime, ItemNameGlobal, StartingBidGlobal



@bot.command()
async def create(ctx, ItemName, AuctionDuration, StartingBid):
    global CreationTime, EndingTime, ItemNameGlobal, StartingBidGlobal
    CreationTime = int(time.time())
    EndingTime = int(time.time()) + int(AuctionDuration) * 86400
    ItemNameGlobal = ItemName
    StartingBidGlobal = StartingBid
    print(CreationTime)
    print(EndingTime)
    embeddata1 = {
        "title": f"Auction Created for {ItemName}",
        "fields": [
            {
                "name": 'Starting Bid',
                "value": f'{StartingBid} nuggets',
                "inline": True
            },
            {
                "name": 'Duration',
                "value": f'{AuctionDuration} days',
                "inline": True
            },
            {
                "name": 'Auction Creation Time',
                "value": f'<t:{CreationTime}:f>',
                "inline": True
            },
            {
                "name": 'Auction Ending Time',
                "value": f'<t:{EndingTime}:f>',
                "inline": True
            }
        ]
    }

    await ctx.send(
        embed = discord.Embed.from_dict(embeddata1)
    )
    """
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
        inline=False
    )
    embedvar.add_field(
        name='Auction Ending Time',
        value=EndingTime,
        inline=True
    )
    await ctx.send(
        embed=embedvar
    )
    """




@bot.command()

async def auctioninfo(ctx):
    print(auctioninfo)
    embed1 = discord.Embed(
        title='Current Auction'
    )
    embed1.add_field(
        name='Item Name',
        value=f'{ItemNameGlobal}',
        inline=True
    )
    embed1.add_field(
        name='Starting Bid',
        value=f'{StartingBidGlobal}',
        inline=True
    )
    embed1.add_field(
        name='Current Bid',
        value='Placeholder',
        inline=True
    )
    embed1.add_field(
        name='Time Remaining',
        value=f'{str((EndingTime-int(time.time()))/86400)} days',
        inline=True
    )
    await ctx.send(
        embed = embed1
    )



@bot.command()
async def bid(ctx, BidAmount):
    save_data = {}
    save_data["bidlist"] = {}
    
    save_data["bidlist"][BidAmount] = ctx.author.id
    with open("biddata1.json", "w") as f: 
        json.dumps(save_data, f)
        








intents = discord.Intents.default()
intents.members = True



bot.run('Insert Token Here')


