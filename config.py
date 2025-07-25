# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01


import re, os

id_pattern = re.compile(r'^.\d+$') 

API_ID = os.environ.get("API_ID", "13516702")

API_HASH = os.environ.get("API_HASH", "bf0cc3f062841935d3d5da65134ca4cf")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "8208053335:AAGj8pgdAYbYKSvlsAH2LKBo_mCJQPtTV6A") 

FORCE_SUB = os.environ.get("FORCE_SUB", "DorutoChan"
             # Don't Remove Credit @VJ_Botz
             # Subscribe YouTube Channel For Amazing Bot @Tech_VJ
             # Ask Doubt on telegram @KingVJ01

DB_NAME = os.environ.get("DB_NAME", "tanveer51749")     

DB_URL = os.environ.get("DB_URL", "mongodb+srv://tanveer51749:8QU3occg03OHqD3Z@cluster0.ulrpc0d.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
 
FLOOD = int(os.environ.get("FLOOD", "10"))

START_PIC = os.environ.get("START_PIC", "https://te.legra.ph/file/119729ea3cdce4fefb6a1.jpg")

ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '6407533831').split()]

PORT = os.environ.get("PORT", "8080")

# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01
