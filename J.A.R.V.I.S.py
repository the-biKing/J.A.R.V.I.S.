#pull
'''
git reset --hard
git pull

'''

import discord
import os
import requests
import json
import ssl
import urllib.request
from random import randint

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)


response = ['you there', 'u there', 'hello']
weather=['weather']
self_intro=['who are u','who r u','who are you','what are you']
youbike=['youbike','ubike','YouBike','Ubike','youBike','uBike']
bad_word=['fuck','shit','ass', 'bitch','cunt','dick','pussy','nigga','nigger','fucker','stupid']
giveme=['tell','give','find me']
meme=['meme','迷因']

NTP=['newtaipei','new taipei','New Taipei','NTP','ntp','新北市']
KHH=['Kaoshiung','kaoshiung','KHH','khh','高雄']
HSZ=['HSZ','hsz','Hsinchu','hsinchu','新竹']
TPE=['TPE','tpe','Taipei','taipei','台北市','台北','臺北','臺北市']
TNN=['TNN','tnn','Tainan','tainan','台南市','台南']
TXG=['TXG','txg','Taichung','taichung','台中市','台中']
KMN=["Kinmen","kinmen","金門",'KMN','kmn']
CYI=['Chiayi' ,'chiayi','嘉義','cyi','CYI']
ILA=['yilan','Yilan','宜蘭','ila','ILA']
ZMI=['Miaoli', 'miaoli','苗栗','zmi','ZMI']
YUN=['Yunlin','yunlin','雲林','yun','YUN']
HUN=['Hualian', 'hualian','花蓮','hun','HUN']
TTT=['TTT','ttt','台東','Taidon','taidon','臺東']
TYN=['TYN','tyn','Taoyuan','taoyuan','桃園']
NTC=['南投','ntc','NTC','Nantou','nantou']
PIF=['屏東','PIF','pif','pingtung','Pingtong']
KEL=['kel','KEL','keelung','Keelung']
PEH=['澎湖','PEH','peh','Penghu','penghu']
CHW=['Chunghua','chunghua','彰化','chw','CHW']
LNN=['連江','lnn','LNN','Lienchiang','lienchiang']



url_TPE = os.environ['UBIKE_1']
url_NTP_1=os.environ['UBIKE_2']
url_NTP_2=os.environ['UBIKE_3']
url_TYN = os.environ['UBIKE_4']






@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_guild_join(guild):
  channel = guild.text_channels[0] # Assuming you want to send the message in the first text channel
  await channel.send('My name is J.A.R.V.I.S. Just another rather very intelligence system. I\'m here to help you with various tasks including playing music, weather forcast and so on.')


@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if any(message.content.startswith(keyword) for keyword in ('jarvis', 'Jarvis')):
    #self_intro
    for item in self_intro:
      if item in message.content:
        await message.channel.send('Allow me to introduce myself, my name is J.A.R.V.I.S. Just another rather very intelligence system. I\'m designed to help you with various tasks, including music, weather forcast and so on. If you come up with some new function that i should have, feel free to tell my creater to add them.')
        
    # Response
    for item in response:
      if item in message.content:
        await message.channel.send('At your service, sir.')
        return
    
    # weather
    for item in weather:
      if item in message.content:
        def get_weather(x):
            url = os.environ['WTHR_URL']
            data = requests.get(url)
            data_json = data.json()
            location = data_json['records']['location']
            quote = ''
            for i in location:
              if i['locationName'] == x:
                city = i['locationName']  # 縣市名稱
                wx8 = i['weatherElement'][0]['time'][0]['parameter'][
                    'parameterName']  # 天氣現象
                pop8 = i['weatherElement'][1]['time'][0]['parameter'][
                    'parameterName']  # 最高溫
                mint8 = i['weatherElement'][2]['time'][0]['parameter'][
                    'parameterName']  # 最低溫
                maxt8= i['weatherElement'][4]['time'][0]['parameter'][
                    'parameterName']  # 降雨機率
                text=''
                if int(maxt8)>=33:
                  quote = '記得隨時補充水分'
                if int(mint8)<=14 :
                  text = '請注意保暖'
                if int(pop8)>=80:
                  text = '建議帶雨傘出門'
                else:
                  quote = f'{city}未來 12 小時{wx8}，最高溫 {maxt8} 度，最低溫 {mint8} 度，降雨機率 {pop8} %'+text
            return quote

        for item in CYI:
          if item in message.content:
            await message.channel.send(get_weather('嘉義縣'))
            return
        for item in NTP:
          if item in message.content:
            await message.channel.send(get_weather('新北市'))
            return
        for item in TPE:
          if item in message.content:
            await message.channel.send(get_weather('臺北市'))
            return
        for item in HSZ:
          if item in message.content:
            await message.channel.send(get_weather('新竹市'))
            return
        for item in TNN:
          if item in message.content:
            await message.channel.send(get_weather('臺南市'))
            return
        for item in ILA:
          if item in message.content:
            await message.channel.send(get_weather('宜蘭市'))
            return
        for item in ZMI:
          if item in message.content:
            await message.channel.send(get_weather('苗栗縣'))
            return
        for item in YUN:
          if item in message.content:
            await message.channel.send(get_weather('雲林縣'))
            return
        for item in HUN:
          if item in message.content:
            await message.channel.send(get_weather('花蓮縣'))
            return
        for item in TXG:
          if item in message.content:
            await message.channel.send(get_weather('臺中市'))
            return
        for item in TTT:
          if item in message.content:
            await message.channel.send(get_weather('臺東縣'))
            return
        for item in TYN:
          if item in message.content:
            await message.channel.send(get_weather('桃園市'))
            return
        for item in NTC:
          if item in message.content:
            await message.channel.send(get_weather('南投縣'))
            return
        for item in KHH:
          if item in message.content:
            await message.channel.send(get_weather('高雄市'))
            return
        for item in KMN:
          if item in message.content:
            await message.channel.send(get_weather('金門縣'))
            return
        for item in PIF:
          if item in message.content:
            await message.channel.send(get_weather('屏東縣'))
            return
        for item in KEL:
          if item in message.content:
            await message.channel.send(get_weather('基隆市'))
            return
        for item in PEH:
          if item in message.content:
            await message.channel.send(get_weather('澎湖縣'))
            return
        for item in LNN:
          if item in message.content:
            await message.channel.send(get_weather('連江縣'))
            return
        for item in CHW:
          if item in message.content:
            await message.channel.send(get_weather('彰化縣'))
            return

    #youbike
    for item in youbike:
      if item in message.content:
        context = ssl._create_unverified_context()
        with urllib.request.urlopen(url_TPE, context=context) as jsondata:
          data_TPE = json.loads(jsondata.read().decode('utf-8-sig')) 
        with urllib.request.urlopen(url_NTP_1, context=context) as jsondata:
          data_NTP_1 = json.loads(jsondata.read().decode('utf-8-sig')) 
        with urllib.request.urlopen(url_NTP_2, context=context) as jsondata:
          data_NTP_2 = json.loads(jsondata.read().decode('utf-8-sig')) 
        with urllib.request.urlopen(url_TYN, context=context) as jsondata:
          data_TYN = json.loads(jsondata.read().decode('utf-8-sig')) 


        station=message.content.replace("台大","臺大").split(' ')
        nonCount=0
        for i in data_TPE:
          space="  "
          spaceInText=" "
          for k in station:
            if i['sna'].find(k)>=0:
              spaceInText=space*(23-len(i['sna']))
              reply=str(i['sna']).replace("YouBike2.0_","")+spaceInText+"bike: "+str(i['sbi'] )+" slot: "+str(i['bemp'])
              await message.channel.send(reply)
            else:
              nonCount+=1

        for i in data_NTP_1:
          space="  "
          spaceInText=" "
          for k in station:
            if i['sna'].find(k)>=0:
              spaceInText=space*(23-len(i['sna']))
              reply=str(i['sna']).replace("YouBike2.0_","")+spaceInText+"bike: "+str(i['sbi'])+" slot: "+str(i['bemp'])
              await message.channel.send(reply)
            else:
              nonCount+=1
        for i in data_NTP_2:
          space="  "
          spaceInText=" "
          for k in station:
            if i['sna'].find(k)>=0:
              spaceInText=space*(23-len(i['sna']))
              reply=str(i['sna']).replace("YouBike2.0_","")+spaceInText+"bike: "+str(i['sbi'] )+" slot: "+str(i['bemp'])
              await message.channel.send(reply)
            else:
              nonCount+=1

        for i in data_TYN['result']['records']:
          space="  "
          spaceInText=" "
          for k in station:
            if i['sna'].find(k)>=0:
              spaceInText=space*(23-len(i['sna']))
              reply=str(i['sna']).replace("YouBike2.0_","")+spaceInText+"bike: "+str(i['sbi'] )+" slot: "+str(i['bemp'])
              await message.channel.send(reply)
            else:
              nonCount+=1
        if nonCount==4 :
          await message.channel.send("no related station found")
        return

    #bad word
    for item in bad_word:
      if item in message.content:
        await message.channel.send('That not very nice')
        return

    for item in giveme:
      if item in message.content:
        for item in meme:
          if item in message.content:
            headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebkit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'}
            response = requests.get("https://memes.tw/wtf/api", headers=headers)
            meme_data = response.json()
            random = randint(0,19)
            meme_url = meme_data[random]['src']          
            await message.channel.send(meme_url)



    
    await message.channel.send('I don\'t understand.')



client.run(os.environ['TOKEN'])
