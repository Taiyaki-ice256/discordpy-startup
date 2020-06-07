from discord.ext import commands
from time import sleep

from flask import Flask, jsonify, render_template, request
import discord
import asyncio
import random
import time
import os
import traceback

loop = asyncio.get_event_loop()

bot = commands.Bot(loop=loop, command_prefix="1;;")
bot_2 = commands.Bot(loop=loop, command_prefix="i;;")
ch1 = "None"
guild1 = "None"
auto1 = "off"
lv1 = "10000000"
autopet = "off"
autom = "on"
autocstop = "off"
automall = "off"
nowcg = "off"

mob_kill = 140

autostop1 = "off"
asg1 = "None"
asc1 = "None"

single = "off"

atknum = 0

#TOKEN = ''
TOKEN1 = os.environ["DISCORD_BOT_TOKEN"]
TOKEN2 = os.environ["DISCORD_BOT2_TOKEN"]

bjr = "on"

rmap = "off"

#@bot.event
#async def on_reaction_add(reaction, author):
#    global bjr
#    print("author" + str(author.id))
#    if author.id == 266912885643411459:
#        if bjr == "on":
#            await reaction.message.add_reaction(reaction.emoji[0])

#@bot.event
#async def on_reaction_remove(reaction, author):
#    global bjr
#    print("author" + str(author.id))
#    if author.id == 266912885643411459:
#        if bjr == "on":
#            await reaction.message.remove_reaction(reaction.emoji[0])

#@bot.event
#async def on_raw_reaction_remove(payload):
#    global bjr
#    if payload.user_id == 266912885643411459:
#        chan = bot.get_channel(payload.channel_id)
#        msgid = payload.message_id

cmd1 = 1
cmd2 = 0

@bot_2.event
async def on_message(message):
    global ch1
    global guild1
    global autom
    global auto1
    global autocstop
    global automall
    global nowcg
    global single
    global atknum
    global rmap
    global mob_kill
    global cmd1
    global cmd2
    wait = random.uniform(1, 3.5)
    if message.author.id == 266912885643411459:
        if message.content.startswith('12;s'):
            reply = message.content[4::]
            str(reply)
            print(reply)
            await message.channel.send(reply)
        if message.content.startswith('allsay'):
            reply = message.content[6::]
            str(reply)
            print(reply)
            await message.channel.send(reply)
    if message.guild.id == guild1:
        if message.channel.id == ch1:
            if cmd1 == cmd2+1:
                if message.embeds[0:]:
                    #if message.embeds[0].description:
                    if message.embeds[0].title:
                        #print(message.embeds[0].title)
                        if autom == "on":
                            if auto1 == "on":
                                if automall == "on":
                                    if "【超激レア】" in message.embeds[0].title:
                                        #auto1 = "off"
                                        reply = "<@266912885643411459> 超激"
                                        await message.channel.send(reply)
                                        auto1 = "off"
                                        reply = "> :gear: AUTO_System : off"
                                        await message.channel.send(reply)
                                        if autocstop == "off":
                                            sleep(5)
                                            reply = "> :gear: AUTO_超激レア_System : 倒すまでたぶんSTOPします"
                                            await message.channel.send(reply)
                                            nowcg = "on"
                                            reply = ";;mt "
                                            print("mention")
                                            sleep(10)
                                            await message.channel.send(reply)
                                elif "ネコしろまる" in message.embeds[0].title:
                                    reply = "<@266912885643411459> しろまる"
                                    print("mention")
                                    await message.channel.send(reply)
                                    auto1 = "off"
                                    reply = "> :gear: AUTO_System : off"
                                    await message.channel.send(reply)
                                    if autocstop == "off":
                                        reply = ";;mt ねこ"
                                        print("mention")
                                        sleep(10)
                                        await message.channel.send(reply)
                                elif "ジャックフロスト" in message.embeds[0].title:
                                    reply = "<@266912885643411459> フロスト"
                                    print("mention")
                                    await message.channel.send(reply)
                                    auto1 = "off"
                                    reply = "> :gear: AUTO_System : off"
                                    await message.channel.send(reply)
                                    if autocstop == "off":
                                        reply = ";;mt フロスト"
                                        print("mention")
                                        sleep(10)
                                        await message.channel.send(reply)
                    if message.embeds[0].title:
                        if auto1 == "on":
                            if nowcg == "off":
                                if single == "off":
                                    global autostop1
                                    if "が待ち構えている...！" in message.embeds[0].title:
                                        #await message.channel.send(str(ch1))
                                        if autostop1 == "on":
                                            autostop1 = "off"
                                            auto1 = "off"
                                            global asg1
                                            global asc1
                                            reply = "> :gear: :white_check_mark: complete!"
                                            await bot.get_guild(asg1).get_channel(asc1).send(reply)
                                            asg1 = "None"
                                            asc1 = "None"
                                        else:
                                            rkill = random.randint(120,150)
                                            if mob_kill >= rkill:
                                                mob_kill = 0
                                                rmap = "on"
                                                async with message.channel.typing():
                                                    sleep(wait)
                                                    atknum = 0
                                                    reply = "::rmap"
                                                    await message.channel.send(reply)
                                                    cmd2 += 1
                                            else:
                                                async with message.channel.typing():
                                                    sleep(wait)
                                                    atknum = 0
                                                    reply = "::atk"
                                                    await message.channel.send(reply)
                                                    cmd2 += 1
            if message.content.startswith('12;i'):
                reply = "::i i <@" + str(message.author.id) + "> "
                print("inori")
                sleep(0.8)
                await message.channel.send(reply)
            if message.embeds[0:]:
                if message.embeds[0].description:
                    if autom == "off":
                        if nowcg == "off":
                            if "アタックカンタ！" in message.embeds[0].description:
                                async with message.channel.typing():
                                    reply = "::re"
                                    print("あたっくかんたre")
                                    sleep(wait)
                                    await message.channel.send(reply)
                    if "この敵には攻撃は不可能のようだ" in message.embeds[0].description:
                        async with message.channel.typing():
                            reply = "::re"
                            print("re tsuki")
                            sleep(wait)
                            await message.channel.send(reply)
                    #print(message.embeds[0].description)
                    if "<@" + str(bot.user.id) + ">さんは現在TAOに" in message.embeds[0].description:
                        async with message.channel.typing():
                            reply = "::login"
                            print("login")
                            sleep(3)
                            await message.channel.send(reply)
                    #if "ゲームにログインしてね" in message.embeds[0].description:
                    #    async with message.channel.typing():
                    #        reply = "::login"
                    #        print("login")
                    #        sleep(10)
                    #        await message.channel.send(reply)

@bot.event
async def on_raw_message_edit(payload):
    wait = random.uniform(1, 3.5)
    if hasattr(payload.data, 'content'):
        if payload.data.embeds[0]:
            if payload.data.embeds[0].fields[2].value:
                chan = bot.get_channel(payload.channel_id)
                global ch1
                if chan.id == ch1:
                    msg = payload.data.content
                    fpet = payload.data.embeds[0].fields[2].value
                    global autopet
                    if autopet == "on":
                        if "これでいいの？" in msg:
                            global auto1
                            if "URレア" in payload.data.embeds[0].fields[2].value:
                                auto1 = "off"
                                await chan.send("<@266912885643411459> \nAUTO_System : STOP")
                            if "TAOレア" in payload.data.embeds[0].fields[2].value:
                                auto1 = "off"
                                await chan.send("<@266912885643411459> \nAUTO_System : STOP")
                            if "MMOレア" in payload.data.embeds[0].fields[2].value:
                                auto1 = "off"
                                await chan.send("<@266912885643411459> \nAUTO_System : STOP")
                    #await bot._scan_text(msg.content)
                    #await chan.send("編集")

@bot.event
async def on_message(message):
    global ch1
    global guild1
    global auto1
    global lv1
    global autopet
    global autom
    global autocstop
    global automall
    global mob_kill
    global single
    global autostop1
    global asg1
    global asc1
    global nowcg
    global atknum
    global rmap
    global cmd1
    global cmd2
    wait = random.uniform(1.5, 4.3)
    if message.content.startswith('1;;start'):
        if message.author.id == 266912885643411459:
            if ch1:
                if guild1:
                    auto1 = "on"
                    reply = "::atk "
                    await bot.get_guild(guild1).get_channel(ch1).send(reply)
                    reply = "> :gear: :white_check_mark: complete!"
                    await message.channel.send(reply)
                    cmd1 = 1
                    cmd2 = 0
                else:
                    reply = "> :gear: :no_entry_sign: Guild not set"
                    await message.channel.send(reply)
            else:
                reply = "> :gear: :no_entry_sign: Channel not set"
                await message.channel.send(reply)
    if message.content.startswith('1;;stop'):
        if message.author.id == 266912885643411459:
            if ch1:
                if guild1:
                    autostop1 = "on"
                    asg1 = message.guild.id
                    asc1 = message.channel.id
                    #reply = "> :gear: :white_check_mark: complete!"
                    reply = "> :gear: Loading...."
                    await message.channel.send(reply)
                    #reply = "::re "
                    #await bot.get_guild(guild1).get_channel(ch1).send(reply)
                    #sleep(5)
                else:
                    reply = "> :gear: :no_entry_sign: Guild not set"
                    await message.channel.send(reply)
            else:
                reply = "> :gear: :no_entry_sign: Channel not set"
                await message.channel.send(reply)
    if message.content.startswith('1;;set'):
        if message.author.id == 688305861059543046:
            guild1 = message.guild.id
            ch1 = message.channel.id
            reply = "> :gear: Guild Set :four_leaf_clover: \n> :gear: Channel Set :four_leaf_clover: "
            await message.channel.send(reply)
        if message.author.id == 266912885643411459:
            guild1 = message.guild.id
            ch1 = message.channel.id
            reply = "> :gear: Guild Set :four_leaf_clover: \n> :gear: Channel Set :four_leaf_clover: "
            await message.channel.send(reply)
    if message.content.startswith('1;gs'):
        if message.author.id == 266912885643411459:
            guild1 = message.guild.id
            reply = "> :gear: Guild Set :four_leaf_clover: "
            await message.channel.send(reply)
    if message.author.id == 688305861059543046:
        if message.content.startswith('1;a'):
            reply = '::atk 再開'
            await message.channel.send(reply)
    if message.guild.id == guild1:
        if message.content.startswith('all;on'):
            if message.author.id == 266912885643411459:
                auto1 = "on"
                reply = "> :gear: AUTO_System : on"
                await message.channel.send(reply)
        if message.content.startswith('all;off'):
            if message.author.id == 266912885643411459:
                auto1 = "off"
                reply = "> :gear: AUTO_System : off"
                await message.channel.send(reply)
        if message.content.startswith('1;on'):
            if message.author.id == 688305861059543046:
                auto1 = "on"
                reply = "> :gear: AUTO_System : on"
                await message.channel.send(reply)
            if message.author.id == 266912885643411459:
                auto1 = "on"
                reply = "> :gear: AUTO_System : on"
                await message.channel.send(reply)
        if message.content.startswith('1;off'):
            if message.author.id == 688305861059543046:
                auto1 = "off"
                reply = "> :gear: AUTO_System : off"
                await message.channel.send(reply)
            if message.author.id == 266912885643411459:
                auto1 = "off"
                reply = "> :gear: AUTO_System : off"
                await message.channel.send(reply)
        if message.content.startswith('1;chs'):
            if message.author.id == 688305861059543046:
                ch1 = message.channel.id
                reply = "> :gear: Channel Set :four_leaf_clover: "
                await message.channel.send(reply)
            if message.author.id == 266912885643411459:
                ch1 = message.channel.id
                reply = "> :gear: Channel Set :four_leaf_clover: "
                await message.channel.send(reply)
        if message.content.startswith('1;poff'):
            if message.author.id == 688305861059543046:
                autopet = "off"
                reply = "> :gear: AUTO_System_PET : off"
                await message.channel.send(reply)
            if message.author.id == 266912885643411459:
                autopet = "off"
                reply = "> :gear: AUTO_System_PET : off"
                await message.channel.send(reply)
        if message.content.startswith('1;pon'):
            if message.author.id == 688305861059543046:
                autopet = "on"
                reply = "> :gear: AUTO_System_PET : on"
                await message.channel.send(reply)
            if message.author.id == 266912885643411459:
                autopet = "on"
                reply = "> :gear: AUTO_System_PET : on"
                await message.channel.send(reply)
        if message.content.startswith('1;moff'):
            if message.author.id == 688305861059543046:
                autom = "off"
                reply = "> :gear: AUTO_Mention : off"
                await message.channel.send(reply)
            if message.author.id == 266912885643411459:
                autom = "off"
                reply = "> :gear: AUTO_Mention : off"
                await message.channel.send(reply)
        if message.content.startswith('1;mon'):
            if message.author.id == 688305861059543046:
                autom = "on"
                reply = "> :gear: AUTO_Mention : on"
                await message.channel.send(reply)
            if message.author.id == 266912885643411459:
                autom = "on"
                reply = "> :gear: AUTO_Mention : on"
                await message.channel.send(reply)
        if message.content.startswith('1;csoff'):
            if message.author.id == 688305861059543046:
                autocstop = "off"
                reply = "> :gear: AUTO_C_Stop : off"
                await message.channel.send(reply)
            if message.author.id == 266912885643411459:
                autocstop = "off"
                reply = "> :gear: AUTO_C_Stop : off"
                await message.channel.send(reply)
        if message.content.startswith('1;cson'):
            if message.author.id == 688305861059543046:
                autocstop = "on"
                reply = "> :gear: AUTO_C_Stop : on"
                await message.channel.send(reply)
            if message.author.id == 266912885643411459:
                autocstop = "on"
                reply = "> :gear: AUTO_C_Stop : on"
                await message.channel.send(reply)
        if message.content.startswith('1;malloff'):
            if message.author.id == 688305861059543046:
                automall = "off"
                reply = "> :gear: AUTO_M_All : off"
                await message.channel.send(reply)
            if message.author.id == 266912885643411459:
                automall = "off"
                reply = "> :gear: AUTO_M_All : off"
                await message.channel.send(reply)
        if message.content.startswith('1;mallon'):
            if message.author.id == 688305861059543046:
                automall = "on"
                reply = "> :gear: AUTO_M_All : on"
                await message.channel.send(reply)
            if message.author.id == 266912885643411459:
                automall = "on"
                reply = "> :gear: AUTO_M_All : on"
                await message.channel.send(reply)
        if message.content.startswith('1;ksoff'):
            if message.author.id == 688305861059543046:
                single = "off"
                reply = "> :gear: AUTO_single : off"
                await message.channel.send(reply)
            if message.author.id == 266912885643411459:
                single = "off"
                reply = "> :gear: AUTO_single : off"
                await message.channel.send(reply)
        if message.content.startswith('1;kson'):
            if message.author.id == 688305861059543046:
                single = "on"
                reply = "> :gear: AUTO_single : on"
                await message.channel.send(reply)
            if message.author.id == 266912885643411459:
                single = "on"
                reply = "> :gear: AUTO_single : on"
                await message.channel.send(reply)
        if message.content.startswith('1;info'):
            if message.author.id == 266912885643411459:
                reply = "> :dizzy: --INFO-- :clipboard:\n> :gear: AUTO_System : " + auto1 + "\n> :gear: Guild : " + str(guild1) + "\n> :gear: Channel : " + str(ch1) + "\n> :gear: AUTO_System_PET : " + autopet + "\n> :gear: AUTO_Mention : " + autom + "\n> :gear: AUTO_C_Stop : " + autocstop + "\n> :gear: AUTO_M_All : " + automall
                await message.channel.send(reply)
        if message.content.startswith('1;id'):
            if message.author.id == 266912885643411459:
                print("id")
                #reply = "id"
                #await message.channel.send(reply)
                reply = "id:" + str(ClientUser.id)
                await message.channel.send(reply)
        if message.content.startswith('1;kill'):
            if message.author.id == 266912885643411459:
                print("id")
                #reply = "id"
                #await message.channel.send(reply)
                reply = "kill:" + str(mob_kill)
                await message.channel.send(reply)
        if message.content.startswith('1;cmd'):
            if message.author.id == 266912885643411459:
                print("id")
                #reply = "id"
                #await message.channel.send(reply)
                reply = str(cmd1) + " " + str(cmd2)
                await message.channel.send(reply)
        if message.channel.id == ch1:
            if auto1 == "on":
                if message.author.id == 526620171658330112:
                    if rmap == "on1":
                        if message.embeds[0:]:
                            if message.embeds[0].description:
                                if "| Lv:" in message.embeds[0].description:
                                    async with message.channel.typing():
                                        sleep(wait)
                                        reply = "::atk "
                                        print("attack")
                                        rmap = "off"
                                        await message.channel.send(reply)
                    elif rmap == "on":
                        if message.embeds[0:]:
                            if message.embeds[0].description:
                                if "| Lv:" in message.embeds[0].description:
                                    async with message.channel.typing():
                                        sleep(wait)
                                        reply = "::rmap "
                                        print("attack")
                                        rmap = "on1"
                                        await message.channel.send(reply)
                    elif cmd1 == cmd2:
                        if "これでいいの？" in message.content:
                            if autopet == "on":
                                async with message.channel.typing():
                                    sleep(wait)
                                    reply = "ok"
                                    print("ok")
                                    await message.channel.send(reply)
                            if autopet == "off":
                                async with message.channel.typing():
                                    sleep(wait)
                                    reply = "no"
                                    print("no")
                                    await message.channel.send(reply)
                        if bot.user.name + "は" in message.content:
                            if "]の攻撃！" in message.content:
                                if "の攻撃！[" in message.content:
                                    if bot.user.name + "はやられてしまった" in message.content:
                                        async with message.channel.typing():
                                            sleep(wait)
                                            reply = "::i e "
                                            print("えりくさー")
                                            await message.channel.send(reply)
                                    else:
                                        async with message.channel.typing():
                                            sleep(wait)
                                            reply = "::atk "
                                            print("attack")
                                            await message.channel.send(reply)
                                else:
                                    print("petkill")
                            elif bot.user.name + "はやられてしまった" in message.content:
                                async with message.channel.typing():
                                    sleep(wait)
                                    reply = "::i e "
                                    print("えりくさー")
                                    await message.channel.send(reply)
                            elif "ダメージを受けた。" in message.content:
                                async with message.channel.typing():
                                    sleep(wait)
                                    reply = "::atk はんげきあたっく！"
                                    print("attack")
                                    await message.channel.send(reply)
                            elif "は華麗にかわした！" in message.content:
                                async with message.channel.typing():
                                    sleep(wait)
                                    reply = "::atk ＾＾"
                                    print("attack")
                                    await message.channel.send(reply)
                        if bot_2.user.name + "は" in message.content:
                            if "]の攻撃！" in message.content:
                                if "の攻撃！[" in message.content:
                                    async with message.channel.typing():
                                        sleep(wait)
                                        reply = "::atk "
                                        print("attack")
                                        await message.channel.send(reply)
                                else:
                                    print("petkill")
                            elif "ダメージを受けた。" in message.content:
                                async with message.channel.typing():
                                    sleep(wait)
                                    reply = "::atk あたっく！！！"
                                    print("attack")
                                    await message.channel.send(reply)
                            elif "は華麗にかわした！" in message.content:
                                async with message.channel.typing():
                                    sleep(wait)
                                    reply = "::atk :3"
                                    print("attack")
                                    await message.channel.send(reply)
                        if message.embeds[0:]:
                            if message.embeds[0].description:
                                print("desk")
                                if "<@" + str(bot.user.id) + ">はもうやられている！" in message.embeds[0].description:
                                    async with message.channel.typing():
                                        sleep(wait)
                                        reply = "::i e 復活～"
                                        print("エリクサー")
                                        await message.channel.send(reply)
                                if "を倒した！" in message.embeds[0].description:
                                    mob_kill += 1
                                    nowcg = "off"
                                    cmd1 += 1
                                if "ゲームにログインしてね" in message.embeds[0].description:
                                    async with message.channel.typing():
                                        reply = "::login"
                                        print("login")
                                        sleep(wait)
                                        await message.channel.send(reply)
                                        cmd1 += 1
                                if "<@" + str(bot_2.user.id) + ">さんは現在TAOに" in message.embeds[0].description:
                                    async with message.channel.typing():
                                        reply = "::atk "
                                        print("loginatk")
                                        sleep(wait)
                                        await message.channel.send(reply)
                                if "コマンドがまだ実行中だよ！" in message.embeds[0].description:
                                    async with message.channel.typing():
                                        reply = "<@266912885643411459> 実行中.."
                                        print("jikkou")
                                        await message.channel.send(reply)
                                if "エリクサーを使った！" in message.embeds[0].description:
                                    async with message.channel.typing():
                                        sleep(wait)
                                        reply = "::atk 復活"
                                        print("hukkatu")
                                        await message.channel.send(reply)
                            if message.embeds[0].title:
                                if auto1 == "on":
                                    if nowcg == "off":
                                        if single == "on":
                                            if "が待ち構えている...！" in message.embeds[0].title:
                                                #await message.channel.send(str(ch1))
                                                if autostop1 == "on":
                                                    autostop1 = "off"
                                                    auto1 = "off"
                                                    reply = "> :gear: :white_check_mark: complete!"
                                                    await bot.get_guild(asg1).get_channel(asc1).send(reply)
                                                    asg1 = "None"
                                                    asc1 = "None"
                                                else:
                                                    async with message.channel.typing():
                                                        sleep(wait)
                                                        reply = "::atk"
                                                        await message.channel.send(reply)

                                #print(message.embeds[0].title)
                                #if autom == "on":
                                #    if auto1 == "on":
                                #        if "ネコしろまる" in message.embeds[0].title:
                                #            reply = "<@266912885643411459> しろまる"
                                #            print("mention")
                                #            await message.channel.send(reply)
                                #            auto1 = "off"
                                #            reply = "> :gear: AUTO_System : off"
                                #            await message.channel.send(reply)
                                #            if autocstop == "off":
                                #                reply = ";;mt ねこ"
                                #                print("mention")
                                #                sleep(10)
                                #                await message.channel.send(reply)
                                #        if "ジャックフロスト" in message.embeds[0].title:
                                #            reply = "<@266912885643411459> フロスト"
                                #            print("mention")
                                #            await message.channel.send(reply)
                                #            auto1 = "off"
                                #            reply = "> :gear: AUTO_System : off"
                                #            await message.channel.send(reply)
                                #            if autocstop == "off":
                                #                reply = ";;mt フロスト"
                                #                print("mention")
                                #                sleep(10)
                                #                await message.channel.send(reply)
                                #if "【超激レア】" in message.embeds[0].title:
                                #    reply = "<@266912885643411459> 超激レア"
                                #    print("mention")
                                #    await message.channel.send(reply)
                                if "Lv." + lv1 + " " in message.embeds[0].title:
                                    reply = "<@266912885643411459> しゅうりょう！"
                                    print("mention")
                                    await message.channel.send(reply)
                                #elif "が待ち構えている...！" in message.embeds[0].title:
                                #    async with message.channel.typing():
                                #        sleep(wait)
                                #        reply = "::atk "
                                #        if autofire1 == "true":
                                #            reply = "::i f "
                                #        print("attack")
                                #        await message.channel.send(reply)
    if message.author.id == 266912885643411459:
        #if message.content.startswith('1;testid'):
        #    reply = 'ok'
        #    await message.channel.send(reply)
        #    reply = 'aaa'
        #    print("testid")
        #    mc = client.get_channel(703456539612282970)
        #    await mc.send(reply)
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

loop.create_task(bot_2.start(TOKEN2, bot=False))
bot.run(TOKEN1, bot=False)
