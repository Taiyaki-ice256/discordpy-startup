import asyncio
import discord
from discord.ext import commands

import os
import traceback

loop = asyncio.get_event_loop()

bot = commands.Bot(command_prefix='/')
bot1token = os.environ['DISCORD_BOT_TOKEN1']
bot2token = os.environ['DISCORD_BOT_TOKEN2']
bot3token = os.environ['DISCORD_BOT_TOKEN3']
bot4token = os.environ['DISCORD_BOT_TOKEN4']

bot_one = commands.Bot(loop=loop, command_prefix="1;;")
bot_two = commands.Bot(loop=loop, command_prefix="2;;")
bot_three = commands.Bot(loop=loop, command_prefix="3;;")
bot_four = commands.Bot(loop=loop, command_prefix="4;;")

ch1 = 700507967857885235
ch2 = 700507983930720287
ch3 = 700508005866668033
ch4 = 700508021419147544
auto1 = "off"


lv1 = "10000000"


two = "false"
three = "false"
four = "false"
fire = "false"

@bot_one.event
async def on_message(message):
    global fire
    global ch1
    global auto1
    global lv1
    if message.guild.id == 378472113394417674:
        if message.content.startswith('1;on'):
            if message.author.id == 266912885643411459:
                auto1 = "on"
        if message.content.startswith('1;off'):
            if message.author.id == 266912885643411459:
                auto1 = "off"
        if message.content.startswith('1;chs'):
            if message.author.id == 266912885643411459:
                ch1 = message.channel.id
        if message.channel.id == ch1:
            if auto1 == "on":
                if message.author.id == 526620171658330112:
                    if "]の攻撃！" in message.content:
                        if "の攻撃！[" in message.content:
                            sleep(2)
                            reply = "::atk "
                            print("attack")
                            await message.channel.send(reply)
                        else:
                            print("petkill")
                    elif "ダメージを受けた。" in message.content:
                        async with message.channel.typing():
                            sleep(2)
                            reply = "::atk "
                            print("attack")
                            await message.channel.send(reply)
                    elif "は華麗にかわした！" in message.content:
                        async with message.channel.typing():
                            sleep(2)
                            reply = "::atk "
                            print("attack")
                            await message.channel.send(reply)
                    elif message.embeds[0:]:
                        if message.embeds[0].title:
                            print(message.embeds[0].title)
                            if "【超激レア】" in message.embeds[0].title:
                                reply = "<@266912885643411459> "
                                print("mention")
                                await message.channel.send(reply)
                            elif "Lv." + lv1 + " " in message.embeds[0].title:
                                reply = "<@266912885643411459> しゅうりょう！"
                                print("mention")
                                await message.channel.send(reply)
                            elif "が待ち構えている...！" in message.embeds[0].title:
                                async with message.channel.typing():
                                    sleep(2)
                                    reply = "::atk "
                                    print("attack")
                                    await message.channel.send(reply)
    if message.author.id == 266912885643411459:
        if message.content.startswith('1;ls'):
            lv1 = message.content[5::]
            print("Lv." + lv1)
            reply = message.content[5::]
            str(reply)
            print(reply)
            reply.replace(' ', '')
            print(reply)
            await message.channel.send(reply)
        if message.content.startswith('1;s'):
            reply = message.content[3::]
            str(reply)
            print(reply)
            reply.replace(' ', '')
            print(reply)
            await message.channel.send(reply)
        if message.content.startswith('allsay'):
            reply = message.content[6::]
            str(reply)
            reply.replace(' ', '')
            print(reply)
            await message.channel.send(reply)
        if message.content.startswith('1;a'):
            reply = '::atk '
            await message.channel.send(reply)
        if message.content.startswith('1;f'):
            reply = '::i f '
            await message.channel.send(reply)
        if message.content.startswith('all;a'):
            reply = '::atk '
            fire = "false"
            await message.channel.send(reply)
        if message.content.startswith('all;f'):
            reply = '::i f '
            fire = "true"
            await message.channel.send(reply)
@bot_two.event
async def on_message(message):
    global two
    global fire
    if message.author.id == 266912885643411459:
        if message.content.startswith('2;s'):
            reply = message.content[3::]
            str(reply)
            print(reply)
            reply.replace(' ', '')
            print(reply)
            await message.channel.send(reply)
        if message.content.startswith('allsay'):
            reply = message.content[6::]
            str(reply)
            reply.replace(' ', '')
            print(reply)
            await message.channel.send(reply)
        if message.content.startswith('2;a'):
            reply = '::atk '
            await message.channel.send(reply)
        if message.content.startswith('2;f'):
            reply = '::i f '
            await message.channel.send(reply)
        if message.content.startswith('all;a'):
            two = "true"
            fire = "false"
        if message.content.startswith('all;f'):
            two = "true"
            fire = "true"
    if message.author.id == 526620171658330112:
        if message.guild.id == 378472113394417674:
            if 'siriusの攻撃！' in message.content:
                print("しりうす")
                if two == "true":
                    reply = '::atk '
                    if fire == "true":
                        reply = '::i f '
                    await message.channel.send(reply)
                    two = "false"
            if "！siriusは" in message.content:
                print("sirius fire")
                if two == "true":
                    reply = '::atk '
                    if fire == "true":
                        reply = '::i f '
                    await message.channel.send(reply)
                    two = "false"
            if len(message.embeds) is 0:
                return
            if message.embeds[0].description:
                #前のBOT ID入れる
                if "開発者が猫大好き" in message.embeds[0].description:
                    print("ceres fire")
                    if two == "true":
                        reply = '::atk '
                        if fire == "true":
                            reply = '::i f '
                        await message.channel.send(reply)
                        two = "false"
                    #print(message.embeds[0].description)
            
@bot_three.event
async def on_message(message):
    global three
    global fire
    if message.author.id == 266912885643411459:
        if message.content.startswith('3;s'):
            reply = message.content[3::]
            str(reply)
            print(reply)
            reply.replace(' ', '')
            print(reply)
            await message.channel.send(reply)
        if message.content.startswith('allsay'):
            reply = message.content[6::]
            str(reply)
            reply.replace(' ', '')
            print(reply)
            await message.channel.send(reply)
        if message.content.startswith('3;a'):
            reply = '::atk '
            await message.channel.send(reply)
        if message.content.startswith('3;f'):
            reply = '::i f '
            await message.channel.send(reply)
        if message.content.startswith('all;a'):
            three = "true"
            fire = "false"
        if message.content.startswith('all;f'):
            three = "true"
            fire = "true"
    if message.guild.id == 378472113394417674:
        if 'Ceresの攻撃！' in message.content:
            if three == "true":
                reply = '::atk '
                if fire == "true":
                    reply = '::i f '
                await message.channel.send(reply)
                three = "false"
        if "！Ceresは" in message.content:
            if three == "true":
                reply = '::atk '
                if fire == "true":
                    reply = '::i f '
                await message.channel.send(reply)
                three = "false"
        #print(str(len(message.embeds)))
        if len(message.embeds) is 0:
            return
        if message.embeds[0].description:
            if two == "false":
                #前のBOT ID入れる
                if "開発者が猫大好き" in message.embeds[0].description:
                    print("iris fire")
                    if three == "true":
                        reply = '::atk '
                        if fire == "true":
                            reply = '::i f '
                        await message.channel.send(reply)
                        three = "false"
@bot_four.event
async def on_message(message):
    global four
    global fire
    if message.author.id == 266912885643411459:
        if message.content.startswith('4;s'):
            reply = message.content[3::]
            str(reply)
            print(reply)
            reply.replace(' ', '')
            print(reply)
            await message.channel.send(reply)
        if message.content.startswith('allsay'):
            reply = message.content[6::]
            str(reply)
            reply.replace(' ', '')
            print(reply)
            await message.channel.send(reply)
        if message.content.startswith('4;a'):
            reply = '::atk '
            await message.channel.send(reply)
        if message.content.startswith('4;f'):
            reply = '::i f '
            await message.channel.send(reply)
        if message.content.startswith('all;a'):
            four = "true"
            fire = "false"
        if message.content.startswith('all;f'):
            four = "true"
            fire = "true"
    if message.guild.id == 378472113394417674:
        if 'irisの攻撃！' in message.content:
            if four == "true":
                reply = '::atk '
                if fire == "true":
                    reply = '::i f '
                await message.channel.send(reply)
                four = "false"
        if "！irisは" in message.content:
            if four == "true":
                reply = '::atk '
                if fire == "true":
                    reply = '::i f '
                await message.channel.send(reply)
                four = "false"
        #print(str(len(message.embeds)))
        if len(message.embeds) is 0:
            return
        if message.embeds[0].description:
            if three == "false":
                #前のBOT ID入れる
                if "開発者が猫大好き" in message.embeds[0].description:
                    print("eris fire")
                    if four == "true":
                        reply = '::atk '
                        if fire == "true":
                            reply = '::i f '
                        await message.channel.send(reply)
                        four = "false"


loop.create_task(bot_two.start(bot2token, bot=False))
loop.create_task(bot_three.start(bot3token, bot=False))
loop.create_task(bot_four.start(bot4token, bot=False))
bot_one.run(bot1token, bot=False)
