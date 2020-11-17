import discord
import requests
import json

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    if message.author.bot:
        return

    if "!" in message.content:
        if message.content.startswith('!유저조회'):
            if "$" in message.content:
                userName = message.content.split("$")[1]

                userData = getUserData(userName)
                e = discord.Embed(title=userData["tierRank"])
                e.set_author(name = "유저 조회 결과")
                e.set_thumbnail(url=userData["userImage"])

                for item in userData["result"]:
                    Game = item["ChampName"] + " - " + item["GameResult"]
                    KDA = item["Kill"] + " / " + item["Death"] + " / " + item["assist"]
                    e.add_field(name=Game, value=KDA, inline=False)

                await message.channel.send(embed=e)
                getUserData(userName)
            else:
                await message.channel.send("값이 잘못 요청되었습니다.")
                await message.channel.send("!유저조회$<유저명>")

def getUserData (userName):
    response = requests.get("http://3964bf147c56.ngrok.io/?name=" + userName)
    json_val = response.json()
    return json_val

client.run('token')