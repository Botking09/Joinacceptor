# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01


from os import path, getenv

class Config:
    API_ID = int(getenv("API_ID", "27514811"))
    API_HASH = getenv("API_HASH", "88b650f1272ab3d38474b18d3bcc66a8")
    BOT_TOKEN = getenv("BOT_TOKEN", "6817963951:AAHDX8Hx0xI4ezaHDzfNR64RzI25ZCw5_B4")
    FSUB = getenv("FSUB", "https://t.me/+3ZDxcUv1KstiOWM1")
    CHID = int(getenv("CHID", "-1001623633000"))
    SUDO = list(map(int, getenv("SUDO", "5871038439").split()))
    MONGO_URI = getenv("MONGO_URI", "mongodb+srv://Ankitking:Ankitking@cluster0.oyrtdsm.mongodb.net/?retryWrites=true&w=majority")
    
cfg = Config()

# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01
