from calendar import day_abbr, month
from datetime import datetime
from datetime import timedelta
import shutil
import os
import time
import csv
from turtle import end_fill, title
from unicodedata import name
import discord
import asyncio
from discord.ext import commands
from setuptools import Command
from random import randint
import threading
import logging

bot = commands.Bot(command_prefix='!')

def modCommands(ctx):
    return ctx.role.id == 915071048779726849

@bot.command()
async def abt(ctx):
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
                "name": '!lb',
                "value": 'Shows the bidding leaderboard for the current auction',
                "inline": False                
            }
        ]
    }

    await ctx.send(
        embed = discord.Embed.from_dict(embed_data)
    )
    

global CreationTime, EndingTime, ItemNameGlobal, StartingBidGlobal
EndingTime = 0


@bot.command()
async def create(ctx, ItemName, AuctionDuration, StartingBid):
    global CreationTime, EndingTime, ItemNameGlobal, StartingBidGlobal
    CreationTime = int(time.time())
    EndingTime = int(time.time()) + int(AuctionDuration)
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
    bidtuple = (944677979185872988, StartingBid)
    with open('biddata.csv', 'a', newline="\n") as csvfile:
            bids = csv.writer(csvfile, delimiter=',')
            bids.writerow(bidtuple)
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
    with open('biddata.csv', 'r', newline='\n') as csvfile:
        bids = list(csv.reader(csvfile, delimiter=','))
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
        value=f'{StartingBidGlobal} nugs',
        inline=True
    )
    embed1.add_field(
        name='Current Bid',
        value=f'{bids[-1][1]} nugs by <@{bids[-1][0]}>',
        inline=True
    )
    embed1.add_field(
        name='Time Remaining',
        value=f'<t:{EndingTime}:R>',
        inline=True
    )
    await ctx.send(
        embed = embed1
    )


@bot.command()
async def bid(ctx, bidAmount):
    global EndingTime, StartingBidGlobal
    """EndingTime = int(time.time()) + 10"""
    if EndingTime < int(time.time()):
        await ctx.send('There is currently no auction running. Please check with I8mydog or Boone for upcoming auctions.')
        return
    if EndingTime <= int(time.time()) + 15:
        EndingTime = int(time.time()) + 30
    if float(bidAmount) % 1 != 0:
        await ctx.send("Invalid Bid")
    bidtuple = (ctx.author.id, bidAmount)
    lastbid = StartingBidGlobal
    with open('biddata.csv', 'r', newline='\n') as csvfile:
        bids = list(csv.reader(csvfile, delimiter=','))
        if len(bids) != 0: 
            lastbid = bids[-1][1]
        
    if int(lastbid) + 5 <= int(bidAmount):
        with open('biddata.csv', 'a', newline="\n") as csvfile:
            bids = csv.writer(csvfile, delimiter=',')
            bids.writerow(bidtuple)
        await ctx.send(f'Bid successful! The current highest bid is {bidAmount}.')
    else:
        await ctx.send(f'Bid must be at least 5 nugs greater than {lastbid} nugs.')
    
@bot.command()
async def biddel(ctx):
    with open('biddata.csv', 'r', newline='\n') as csvfile:
        bids = list(csv.reader(csvfile, delimiter=','))
    for row in bids[::-1]:
        if int(row[0]) == ctx.author.id:
            bids.remove(row)
            await ctx.send('Bid Deleted')            
            with open('biddata.csv', 'w', newline='\n') as csvfile:
                bidlist = csv.writer(csvfile, delimiter=',')
                for row in bids:
                    bidlist.writerow(row)
            return
    await ctx.send('Bid not found')

@bot.command()
async def lb(ctx):
    with open('biddata.csv', 'r', newline='\n') as csvfile:
        bids = list(csv.reader(csvfile, delimiter=','))
        lbarray = [str(944677979185872988)]
        lbembed = discord.Embed(
            title= "Leaderboard"
        )
        for row in bids[::-1]:
            if row[0] in lbarray:
                continue
            lbembed.add_field(
                name= f'{len(lbarray)}. {row[1]} nuggets',
                value= f'<@{row[0]}>',
                inline = False
                )
            lbarray.append(row[0])
        
    await ctx.send(embed = lbembed)

@bot.command()
async def bidhist(ctx, userid):
    with open('biddata.csv', 'r', newline='\n') as csvfile:
        bids = list(csv.reader(csvfile, delimiter=','))
        bidhistfield = ''
        bidhistarray = []
        for row in bids[::-1]:
            if userid == row[0]:
                bidhistfield += f'{len(bidhistarray)+1}. {row[1]} nuggets\n'
                bidhistarray.append(row[1])
        
        bidhistembed = discord.Embed(
            title= "Bid History"    
        )
        bidhistembed.add_field(
            name= bidhistfield,
            value= f'<@{userid}>'
        )

    await ctx.send(embed = bidhistembed)

async def check(ctx, thread1):
    logging.info("Thread %s: starting", thread1)
    logging.info("Thread %s: finishing", thread1)
    while time.time() < EndingTime:
        time.sleep(0.5)
    if EndingTime < time.time():
        with open('biddata.csv', 'r', newline='\n') as csvfile:
            bids = list(csv.reader(csvfile, delimiter=','))
        endofauction = discord.Embed(
            title= "Auction Ended",    
        )
        endofauction.addfield(
            name= "The winner of the auction is",
            value= f'{bids[-1][0]} with {bids[-1][1]} nuggets!'
        )
    await ctx.send(embed = endofauction)



    




intents = discord.Intents.default()
intents.members = True



bot.run('Insert Token Here')


