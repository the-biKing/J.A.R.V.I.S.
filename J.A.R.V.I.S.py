# pull
"""
git reset --hard
git pull

"""

import discord
import os
import requests
import json
import ssl
import urllib.request
from random import randint
import datetime
from dateutil import tz

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)


taipei_timezone = tz.gettz("Asia/Taipei")

station_dict = {
    "象山": "R02",
    "台北101/世貿": "R03",
    "信義安和": "R04",
    "大安": "R05",
    "大安森林公園": "R06",
    "東門": "R07",
    "中正紀念堂": "R08",
    "台大醫院": "R09",
    "台北車站": "R10",
    "中山": "R11",
    "雙連": "R12",
    "民權西路": "R13",
    "圓山": "R14",
    "劍潭": "R15",
    "士林": "R16",
    "芝山": "R17",
    "明德": "R18",
    "石牌": "R19",
    "唭哩岸": "R20",
    "奇岩": "R21",
    "北投": "R22",
    "新北投": "R22A",
    "復興崗": "R23",
    "忠義": "R24",
    "關渡": "R25",
    "竹圍": "R26",
    "紅樹林": "R27",
    "淡水": "R28",
    "新店": "G01",
    "新店區公所": "G02",
    "七張": "G03",
    "小碧潭": "G03A",
    "大坪林": "G04",
    "景美": "G05",
    "萬隆": "G06",
    "公館": "G07",
    "台電大樓": "G08",
    "古亭": "G09",
    "中正紀念堂": "G10",
    "小南門": "G11",
    "西門": "G12",
    "北門": "G13",
    "中山": "G14",
    "松江南京": "G15",
    "南京復興": "G16",
    "台北小巨蛋": "G17",
    "南京三民": "G19",
    "松山": "G20",
    "南勢角": "O01",
    "景安": "O02",
    "永安市場": "O03",
    "頂溪": "O04",
    "古亭": "O05",
    "東門": "O06",
    "忠孝新生": "O07",
    "松江南京": "O08",
    "行天宮": "O09",
    "中山國小": "O10",
    "民權西路": "O11",
    "大橋頭": "O12",
    "台北橋": "O13",
    "菜寮": "O14",
    "三重": "O15",
    "先嗇宮": "O16",
    "頭前庄": "O17",
    "新莊": "O18",
    "輔大": "O19",
    "丹鳳": "O20",
    "迴龍": "O21",
    "三重國小": "O50",
    "三和國中": "O51",
    "徐匯中學": "O52",
    "三民高中": "O53",
    "蘆洲": "O54",
    "頂埔": "BL01",
    "永寧": "BL02",
    "土城": "BL03",
    "海山": "BL04",
    "亞東醫院": "BL05",
    "府中": "BL06",
    "板橋": "BL07",
    "新埔": "BL08",
    "江子翠": "BL09",
    "龍山寺": "BL10",
    "西門": "BL11",
    "台北車站": "BL12",
    "善導寺": "BL13",
    "忠孝新生": "BL14",
    "忠孝復興": "BL15",
    "忠孝敦化": "BL16",
    "國父紀念館": "BL17",
    "市政府": "BL18",
    "永春": "BL19",
    "後山埤": "BL20",
    "昆陽": "BL21",
    "南港": "BL22",
    "南港展覽館": "BL23",
}
NTP = ["newtaipei", "new taipei", "New Taipei", "NTP", "ntp", "新北市"]
KHH = ["Kaoshiung", "kaoshiung", "KHH", "khh", "高雄"]
HSZ = ["HSZ", "hsz", "Hsinchu", "hsinchu", "新竹"]
TPE = ["TPE", "tpe", "Taipei", "taipei", "台北市", "台北", "臺北", "臺北市"]
TNN = ["TNN", "tnn", "Tainan", "tainan", "台南市", "台南"]
TXG = ["TXG", "txg", "Taichung", "taichung", "台中市", "台中"]
KMN = ["Kinmen", "kinmen", "金門", "KMN", "kmn"]
CYI = ["Chiayi", "chiayi", "嘉義", "cyi", "CYI"]
ILA = ["yilan", "Yilan", "宜蘭", "ila", "ILA"]
ZMI = ["Miaoli", "miaoli", "苗栗", "zmi", "ZMI"]
YUN = ["Yunlin", "yunlin", "雲林", "yun", "YUN"]
HUN = ["Hualian", "hualian", "花蓮", "hun", "HUN"]
TTT = ["TTT", "ttt", "台東", "Taidon", "taidon", "臺東"]
TYN = ["TYN", "tyn", "Taoyuan", "taoyuan", "桃園"]
NTC = ["南投", "ntc", "NTC", "Nantou", "nantou"]
PIF = ["屏東", "PIF", "pif", "pingtung", "Pingtong"]
KEL = ["kel", "KEL", "keelung", "Keelung"]
PEH = ["澎湖", "PEH", "peh", "Penghu", "penghu"]
CHW = ["Chunghua", "chunghua", "彰化", "chw", "CHW"]
LNN = ["連江", "lnn", "LNN", "Lienchiang", "lienchiang"]


url_TPE = os.environ["UBIKE_1"]
url_NTP_1 = os.environ["UBIKE_2"]
url_NTP_2 = os.environ["UBIKE_3"]
url_TYN = os.environ["UBIKE_4"]
url_weather = os.environ["WTHR_URL"]


@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))


@client.event
async def on_guild_join(guild):
    channel = guild.text_channels[
        0
    ]  # Assuming you want to send the message in the first text channel
    await channel.send(
        "My name is J.A.R.V.I.S. Just another rather very intelligence system. I'm here to help you with various tasks including playing music, weather forcast and so on."
    )


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if any(message.content.startswith(keyword) for keyword in ("jarvis", "Jarvis")):
        # self_intro
        self_intro = ["who are u", "who r u", "who are you", "what are you"]
        for item in self_intro:
            if item in message.content:
                await message.channel.send(
                    "Allow me to introduce myself, my name is J.A.R.V.I.S. Just another rather very intelligence system. I'm designed to help you with various tasks, including music, weather forcast and so on. If you come up with some new function that i should have, feel free to tell my creater to add them."
                )

        # Response
        response = ["you there", "u there", "hello"]
        for item in response:
            if item in message.content:
                await message.channel.send("At your service, sir.")
                return

        # weather
        weather = ["weather"]
        for item in weather:
            if item in message.content:

                def get_weather(x):
                    data = requests.get(url_weather)
                    data_json = data.json()
                    location = data_json["records"]["location"]
                    quote = ""
                    for i in location:
                        if i["locationName"] == x:
                            city = i["locationName"]  # 縣市名稱
                            wx8 = i["weatherElement"][0]["time"][0]["parameter"][
                                "parameterName"
                            ]  # 天氣現象
                            pop8 = i["weatherElement"][1]["time"][0]["parameter"][
                                "parameterName"
                            ]  # 最高溫
                            mint8 = i["weatherElement"][2]["time"][0]["parameter"][
                                "parameterName"
                            ]  # 最低溫
                            maxt8 = i["weatherElement"][4]["time"][0]["parameter"][
                                "parameterName"
                            ]  # 降雨機率
                            text = ""
                            if int(maxt8) >= 33:
                                quote = "記得隨時補充水分"
                            if int(mint8) <= 14:
                                text = "請注意保暖"
                            if int(pop8) >= 80:
                                text = "建議帶雨傘出門"
                            else:
                                quote = (
                                    f"{city}未來 12 小時{wx8}，最高溫 {maxt8} 度，最低溫 {mint8} 度，降雨機率 {pop8} %"
                                    + text
                                )
                    return quote

                for item in CYI:
                    if item in message.content:
                        await message.channel.send(get_weather("嘉義縣"))
                        return
                for item in NTP:
                    if item in message.content:
                        await message.channel.send(get_weather("新北市"))
                        return
                for item in TPE:
                    if item in message.content:
                        await message.channel.send(get_weather("臺北市"))
                        return
                for item in HSZ:
                    if item in message.content:
                        await message.channel.send(get_weather("新竹市"))
                        return
                for item in TNN:
                    if item in message.content:
                        await message.channel.send(get_weather("臺南市"))
                        return
                for item in ILA:
                    if item in message.content:
                        await message.channel.send(get_weather("宜蘭市"))
                        return
                for item in ZMI:
                    if item in message.content:
                        await message.channel.send(get_weather("苗栗縣"))
                        return
                for item in YUN:
                    if item in message.content:
                        await message.channel.send(get_weather("雲林縣"))
                        return
                for item in HUN:
                    if item in message.content:
                        await message.channel.send(get_weather("花蓮縣"))
                        return
                for item in TXG:
                    if item in message.content:
                        await message.channel.send(get_weather("臺中市"))
                        return
                for item in TTT:
                    if item in message.content:
                        await message.channel.send(get_weather("臺東縣"))
                        return
                for item in TYN:
                    if item in message.content:
                        await message.channel.send(get_weather("桃園市"))
                        return
                for item in NTC:
                    if item in message.content:
                        await message.channel.send(get_weather("南投縣"))
                        return
                for item in KHH:
                    if item in message.content:
                        await message.channel.send(get_weather("高雄市"))
                        return
                for item in KMN:
                    if item in message.content:
                        await message.channel.send(get_weather("金門縣"))
                        return
                for item in PIF:
                    if item in message.content:
                        await message.channel.send(get_weather("屏東縣"))
                        return
                for item in KEL:
                    if item in message.content:
                        await message.channel.send(get_weather("基隆市"))
                        return
                for item in PEH:
                    if item in message.content:
                        await message.channel.send(get_weather("澎湖縣"))
                        return
                for item in LNN:
                    if item in message.content:
                        await message.channel.send(get_weather("連江縣"))
                        return
                for item in CHW:
                    if item in message.content:
                        await message.channel.send(get_weather("彰化縣"))
                        return

        # youbike
        youbike = ["youbike", "ubike", "YouBike", "Ubike", "youBike", "uBike"]
        for item in youbike:
            if item in message.content:
                context = ssl._create_unverified_context()
                with urllib.request.urlopen(url_TPE, context=context) as jsondata:
                    data_TPE = json.loads(jsondata.read().decode("utf-8-sig"))
                with urllib.request.urlopen(url_NTP_1, context=context) as jsondata:
                    data_NTP_1 = json.loads(jsondata.read().decode("utf-8-sig"))
                with urllib.request.urlopen(url_NTP_2, context=context) as jsondata:
                    data_NTP_2 = json.loads(jsondata.read().decode("utf-8-sig"))
                with urllib.request.urlopen(url_TYN, context=context) as jsondata:
                    data_TYN = json.loads(jsondata.read().decode("utf-8-sig"))

                station = message.content.replace("台大", "臺大").split(" ")
                nonCount = 0
                for i in data_TPE:
                    space = "  "
                    spaceInText = " "
                    for k in station:
                        if i["sna"].find(k) >= 0:
                            spaceInText = space * (23 - len(i["sna"]))
                            reply = (
                                str(i["sna"]).replace("YouBike2.0_", "")
                                + spaceInText
                                + "bike: "
                                + str(i["sbi"])
                                + " slot: "
                                + str(i["bemp"])
                            )
                            await message.channel.send(reply)
                        else:
                            nonCount += 1

                for i in data_NTP_1:
                    space = "  "
                    spaceInText = " "
                    for k in station:
                        if i["sna"].find(k) >= 0:
                            spaceInText = space * (23 - len(i["sna"]))
                            reply = (
                                str(i["sna"]).replace("YouBike2.0_", "")
                                + spaceInText
                                + "bike: "
                                + str(i["sbi"])
                                + " slot: "
                                + str(i["bemp"])
                            )
                            await message.channel.send(reply)
                        else:
                            nonCount += 1
                for i in data_NTP_2:
                    space = "  "
                    spaceInText = " "
                    for k in station:
                        if i["sna"].find(k) >= 0:
                            spaceInText = space * (23 - len(i["sna"]))
                            reply = (
                                str(i["sna"]).replace("YouBike2.0_", "")
                                + spaceInText
                                + "bike: "
                                + str(i["sbi"])
                                + " slot: "
                                + str(i["bemp"])
                            )
                            await message.channel.send(reply)
                        else:
                            nonCount += 1

                for i in data_TYN["result"]["records"]:
                    space = "  "
                    spaceInText = " "
                    for k in station:
                        if i["sna"].find(k) >= 0:
                            spaceInText = space * (23 - len(i["sna"]))
                            reply = (
                                str(i["sna"]).replace("YouBike2.0_", "")
                                + spaceInText
                                + "bike: "
                                + str(i["sbi"])
                                + " slot: "
                                + str(i["bemp"])
                            )
                            await message.channel.send(reply)
                        else:
                            nonCount += 1
                if nonCount == 4:
                    await message.channel.send("no related station found")
                return

        # bad word
        bad_word = [
            "fuck",
            "shit",
            "ass",
            "bitch",
            "cunt",
            "dick",
            "pussy",
            "nigga",
            "nigger",
            "fucker",
            "stupid",
        ]
        for item in bad_word:
            if item in message.content:
                await message.channel.send("That not very nice")
                return
        # meme,joke
        give_me = ["tell", "give", "find", "send"]
        meme = ["meme", "迷因"]
        joke = ["jokes", "joke", "funny"]
        for item in give_me:
            if item in message.content:
                for i in meme:
                    if i in message.content:
                        headers = {
                            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebkit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36"
                        }
                        response = requests.get(
                            "https://memes.tw/wtf/api", headers=headers
                        )
                        meme_data = response.json()
                        random = randint(0, 19)
                        meme_url = meme_data[random]["src"]
                        await message.channel.send(meme_url)
                        return
                for i in joke:
                    if i in message.content:
                        headers = {
                            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebkit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36"
                        }
                        response = requests.get(
                            "https://v2.jokeapi.dev/joke/Any", headers=headers
                        )
                        joke_data = response.json()
                        type = joke_data["type"]
                        if type == "single":
                            joke = joke_data["joke"]
                            await message.channel.send(joke)
                            return
                        elif type == "twopart":
                            setup = joke_data["setup"]
                            delivery = joke_data["delivery"]
                            await message.channel.send(setup)
                            await message.channel.send(delivery)
                            return
                        else:
                            print("error")
        mrt=['mrt','MRT','捷運','北捷']
        for i in mrt:
            if i in message.content:
                input=message.content.split()
                lenth=len(input)
                stationid=str(input[lenth-1]).replace(' ','')
                try:
                  test = int(stationid[2])
                  stationid = str(stationid).upper()
                except:
                  stationid=station_dict[stationid]
                current_time = datetime.datetime.now(tz=taipei_timezone)
                ct=str(current_time).split('.')[0]
                time=ct.split(' ')[1]
                weekday = current_time.strftime('%A')
                current_hour=int(time.split(':')[0])
                current_minute=int(time.split(':')[1])
                current_second=int(time.split(':')[2])
                url = 'https://tdx.transportdata.tw/api/basic/v2/Rail/Metro/StationTimeTable/TRTC?%24filter=StationID%20eq%20%27'+str(stationid)+'%27&%24top=30&%24format=JSON'  
                headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebkit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36"
                }
                response = requests.get(url, headers=headers)
                data = json.loads(response.text)
                if len(data) == 0:
                  await message.channel.send('no train found')
                  return
                for i in range(0,len(data)):
                  if data[i]['ServiceDay'][weekday]:
                    k=0
                    for k in range(0,len(data[i]['Timetables'])):
                      arrivalTime=str(data[i]['Timetables'][k]['ArrivalTime'])
                      arrival_hr=int(arrivalTime.split(':')[0])
                      if arrival_hr<5:
                        arrival_hr=arrival_hr+24
                      arrival_min=int(arrivalTime.split(':')[1])
                      time_til_train=(arrival_hr-current_hour)*60+(arrival_min-current_minute)
                      if time_til_train>0 and time_til_train<60:
                        reply1=(data[i]["StationName"]["Zh_tw"]+'to'+data[i]["DestinationStationName"]["Zh_tw"])
                        await message.channel.send(reply1)
                        await message.channel.send(data[i]["Timetables"][k]["ArrivalTime"])
                        if k+1> len(data[i]['Timetables']):
                          await message.channel.send('No more trains')
                        else:
                          await message.channel.send(data[i]["Timetables"][k+1]["ArrivalTime"])
                        break
                return    






        await message.channel.send("I don't understand.")


client.run(os.environ["TOKEN"])
