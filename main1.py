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

"""
!auctioninfo: Gives info on current auction\n!bid: Places your bid on an auctioned item\n!bidhist <user>: Shows history of a user`s bids\n!bidremove: Removes your bid from an auctioned item\n!create <item> <duration> <starting bid>: Creates an auction\n!help: Shows commands\n!leaderboard: Shows bidding leaderboard for the current auction\n!remove: removes an auction
"""

@bot.command()
async def info(ctx):

    await ctx.send(ctx.guild)
    await ctx.send(ctx.author)
    await ctx.send(ctx.message.id)

CreationTime = '<t:{int(time.time())}:f>'

@bot.command()
async def create(ctx, ItemName, AuctionDuration, StartingBid):
    
    EndingTime = CreationTime + (AuctionDuration * 86400)

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



"""
relative time stamps
"""
    
"""
client = discord.Client()

@client.event
async def on_ready():
    print('Auction bot is now online!')

client.run('OTQ0Njc3OTc5MTg1ODcyOTg4.YhFF7Q.s3z0MC6V8Czo7l4PCw0jP-X_gGk')
"""
class AuctionBot(discord.Client):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.target_message_id = 953104372332658688

    async def on_ready(self):
        print('Auction bot is now online! - sharp')

    async def on_raw_reaction_add(self, payload):
        if payload.message_id != self.target_message_id:
                return

        guild = Client.get_guild(payload.guild_id)

        if payload.emoji.name == '🦈':
            role = discord.utils.get(guild.roles, name='Auction Shark')
            await payload.member.add_roles(role)

    async def on_raw_reaction_remove(self, payload):
        if payload.message_id != self.target_message_id:
                return

        guild = Client.get_guild(payload.guild_id)
        member = guild.get_member(payload.user_id)

        if payload.emoji.name == '🦈':
            role = discord.utils.get(guild.roles, name='Auction Shark')
            await member.remove_roles(role)



intents = discord.Intents.default()
intents.members = True

Client = AuctionBot(intents=intents)



bot.run('OTQ0Njc3OTc5MTg1ODcyOTg4.YhFF7Q.s3z0MC6V8Czo7l4PCw0jP-X_gGk')

Client.run('OTQ0Njc3OTc5MTg1ODcyOTg4.YhFF7Q.s3z0MC6V8Czo7l4PCw0jP-X_gGk')


# https://www.youtube.com/watch?v=XL6ABuJ0XO0&list=PL6gx4Cwl9DGAHdJdtEl0-XiRfPRAvpbSz&index=3

    


