from os import getenv
from dotenv import load_dotenv

load_dotenv()

#Necessary Variables 
API_ID = int(getenv("API_ID", 29400566))
API_HASH = getenv("API_HASH", "8fd30dc496aea7c14cf675f59b74ec6f")
BOT_TOKEN = getenv("BOT_TOKEN") #Put your bot token here
LOG_ID = int(getenv("LOG_ID"))
OWNER_ID = int(getenv("OWNER_ID", 5381777131)) #Go to @fallenxbot and type id and put that value here. 
SUDOERS = list(map(int, getenv("SUDOERS", "").split()))
