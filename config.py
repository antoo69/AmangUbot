import os
from os import getenv
from dotenv import load_dotenv
from distutils.util import strtobool


load_dotenv(".env")


API_ID = int(getenv("API_ID", "22739204")) #optional
API_HASH = getenv("API_HASH", "047114959f334260b425d5a2d3a5487d") #optional
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "").split()))
DEEP_AI = getenv("DEEP_AI", "d7394561-0528-4714-a1ee-edd7020b48e1")
OWNER_ID = int(getenv("OWNER_ID", "7342395108") or 0)
ADMIN1_ID = list(map(int, getenv("ADMIN1_ID", "7342395108").split()))
ADMIN2_ID = list(map(int, getenv("ADMIN2_ID", "7083782157").split()))
ADMIN3_ID = list(map(int, getenv("ADMIN2_ID", "2073506739").split()))
ADMIN4_ID = list(map(int, getenv("ADMIN2_ID", "918837361").split()))


ADMIN1_ID.append(7342395108)
ADMIN2_ID.append(7083782157)
ADMIN3_ID.append(2073506739)
ADMIN4_ID.append(918837361)

MONGO_URL = getenv("MONGO_URL", "mongodb+srv://musicbot9809:buburayam1@cluster0.vwbhb.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
BOT_TOKEN = getenv("BOT_TOKEN", "7369864257:AAF06oTzl5eW2BOE0T34xSqzgos1VpLApNw")
BOT_WORKERS = int(getenv("BOT_WORKERS", "2"))
USER_WORKERS = int(getenv("BOT_WORKERS", "8"))
PM_AUTO_BAN = strtobool(getenv("PM_AUTO_BAN", "True"))
ALIVE_PIC = getenv("ALIVE_PIC", "https://telegra.ph/file/a23e9cf302c1da667bd89.jpg")
ALIVE_TEXT = getenv("ALIVE_TEXT", "ʙᴏᴛ ɪᴅᴜᴘ ʏᴀ ᴋᴏɴᴛᴏʟ ....")
PM_LOGGER = getenv("PM_LOGGER", None)
OPENAI_API = getenv("OPENAI_API", "")
BOTLOG_CHATID = int(getenv("BOTLOG_CHATID") or 0)
BLACKLIST_GCAST = {int(x) for x in getenv("BLACKLIST_GCAST", "").split()}
GIT_TOKEN = getenv("GIT_TOKEN") #personal access token
HEROKU_API_KEY = getenv("HEROKU_API_KEY")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
BRANCH = getenv("BRANCH", "amang") #don't change
REPO_URL = getenv("REPO_URL", "https://github.com/amanqs/AmangUbot")
CMD_HNDLR = getenv("CMD_HNDLR", ".")
SUPPORT = int(getenv("SUPPORT", "-1002079962899"))
CHANNEL = int(getenv("CHANNEL", "-1001574189667"))
SESSION1 = getenv("SESSION1", "BQFa-QQAk2c4tKVXXrTFwwGnBnVYt3psx407u7RLaaWxvrsuV-yz8jQO-3F7s1VKW6-w9gxsexKKicxYzaq0JArPrSVUem0cWAfOKLQs2UXP3M4m5GFvYbmVukuPU0Y1m_O7AoKBOu_hlV7sVuaTCVEllwor3qhbVUzG5wWgJ78PGe3zyaw9uBLYva2nbYpbWRX14XkjrZeLITb5iYmwHX1xJXRHdV4yuDueeQRXMCMIBYDDtjg6rPRTd9SxwzgpJK2N2ST8GYqLaaFwISvfsdNlyt-x9AkKTAy3FOhnz5W_y-nCa4SCJrONY592JaEkgu7cXyWttREakW24L0-wSg5TVxKEdwAAAAG1pA7kAA")
SESSION2 = getenv("SESSION2", "")
SESSION3 = getenv("SESSION3", "")
SESSION4 = getenv("SESSION4", "")
SESSION5 = getenv("SESSION5", "")
SESSION6 = getenv("SESSION6", "")
SESSION7 = getenv("SESSION7", "")
SESSION8 = getenv("SESSION8", "")
SESSION9 = getenv("SESSION9", "")
SESSION10 = getenv("SESSION10", "")
SESSION11 = getenv("SESSION11", "")
SESSION12 = getenv("SESSION12", "")
SESSION13 = getenv("SESSION13", "")
SESSION14 = getenv("SESSION14", "")
SESSION15 = getenv("SESSION15", "")
SESSION16 = getenv("SESSION16", "")
SESSION17 = getenv("SESSION17", "")
SESSION18 = getenv("SESSION18", "")
SESSION19 = getenv("SESSION19", "")
SESSION20 = getenv("SESSION20", "")
SESSION21 = getenv("SESSION21", "")
SESSION22 = getenv("SESSION22", "")
SESSION23 = getenv("SESSION23", "")
SESSION24 = getenv("SESSION24", "")
SESSION25 = getenv("SESSION25", "")
SESSION26 = getenv("SESSION26", "")
SESSION27 = getenv("SESSION27", "")
SESSION28 = getenv("SESSION28", "")
SESSION29 = getenv("SESSION29", "")
SESSION30 = getenv("SESSION30", "")
SESSION31 = getenv("SESSION31", "")
SESSION32 = getenv("SESSION32", "")
SESSION33 = getenv("SESSION33", "")
SESSION34 = getenv("SESSION34", "")
SESSION35 = getenv("SESSION35", "")
