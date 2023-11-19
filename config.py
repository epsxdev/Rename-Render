# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01


import re, os

id_pattern = re.compile(r'^.\d+$') 

API_ID = os.environ.get("API_ID", "29160964")

API_HASH = os.environ.get("API_HASH", "eda568bc645b8f61c93dc1582afa99e2")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "6913971805:AAHuk2Eb2NzHEt0WYJ2KJz8d0GPnpSH7rks") 

FORCE_SUB = os.environ.get("FORCE_SUB", "EpisodeStores") 

             # Don't Remove Credit @VJ_Botz
             # Subscribe YouTube Channel For Amazing Bot @Tech_VJ
             # Ask Doubt on telegram @KingVJ01

DB_NAME = os.environ.get("DB_NAME", "renamebot")     

DB_URL = os.environ.get("DB_URL", "mongodb+srv://EPISODESTORE:EPISODESTORE@cluster0.74agvw0.mongodb.net/?retryWrites=true&w=majority")
 
FLOOD = int(os.environ.get("FLOOD", "10"))

START_PIC = os.environ.get("START_PIC", "https://graph.org/file/14c7bccf1f9b94dde77f4.jpg")

ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '1388032243').split()]

PORT = os.environ.get("PORT", "8080")

# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01
