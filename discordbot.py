import discord
import io
import os
import sys
import urllib.request
import json
import random
import datetime
import time

papagoid = "lc28UCeAjSsUqoTnZ0AU"
papagopw = "EXa_ddldd1"

print(os);
token="NzQ5OTQ5NzYwOTQ5MTkwNzQ3.X0zbJA.BrX9hwxP_xN5mmI0dc9Q-WJPxSw"
client = discord.Client()


@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.idle, activity=discord.Game("^tr | Made by Frozenn_"))
    print('bot')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('^tr'):
        from_lan = message.content[4:6]
        target_text = message.content[7:]
        print(from_lan,target_text)
        await message.channel.send("```" + pst_detection(from_lan, target_text) + "```")

def pst_detection(to_lan, target_text):
    encQuery = urllib.parse.quote(target_text)
    data = "query=" + encQuery
    url = "https://openapi.naver.com/v1/papago/detectLangs"
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id", papagoid)
    request.add_header("X-Naver-Client-Secret", papagopw)
    response = urllib.request.urlopen(request, data=data.encode("utf-8"))
    rescode = response.getcode()
    if (rescode == 200):
        from_lan = response.read().decode('utf-8')[13:15]
        return pst_translation(from_lan, to_lan, target_text)
    else:
        print("Error Code(Language_Detection):" + rescode)


def pst_translation(from_lan, to_lan, target_text):
    encText = urllib.parse.quote(target_text)
    data = "source=" + from_lan + "&target=" + to_lan + "&text=" + encText
    url = "https://openapi.naver.com/v1/papago/n2mt"
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id", papagoid)
    request.add_header("X-Naver-Client-Secret", papagopw)
    response = urllib.request.urlopen(request, data=data.encode("utf-8"))
    rescode = response.getcode()
    if (rescode == 200):
        response_body = response.read().decode('utf-8')
        jDict = json.loads(response_body)
        result = jDict['message']['result']['translatedText']
        print(result)
        return result
    else:
        print("Error Code:" + rescode)
client.run(token)

