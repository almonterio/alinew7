import os

from dotenv import load_dotenv
from pyrogram import Client, filters
from pytgcalls import PyTgCalls

# For Local Deploy
if os.path.exists(".env"):
    load_dotenv(".env")

# Necessary Vars
API_ID = int(os.getenv("12311076"))
API_HASH = os.getenv("15c0be947edb53eda9c81fedbdc34f03")
SESSION = os.getenv("AQCT0ciRaXctvA4Ra8ukPgAVJxhiQOFXyUOyNNtarPSN_veUvhnfU1R-JUgKE6zX2MHbMMle-xWppO9aSOi6nrNdcGQ7TgRumf7Uvp_hkq2UEj8OTKDkg07STTYsW_e1fY5839cikXQ_LLXlaDho7BJ_0Gem-T_nqk4hl-ALkPvdh88LI5aO6EYbcyU3T2Babl9FPKhgyLqE-jV9qAe5HGOT8p8tjrgCkrALxb8krQh4CwXv1kKZ06p4OSJ4y7Y-glK3392gy41GEikBxB5aOReOviQ_BvKI874vplZAUzqPnMZeD4kt8juozrgPS4O8kbxyyrYCvBggjNHdC-i7XbGAaOZcMgA")
HNDLR = os.getenv("HNDLR", ".")
SUDO_USERS = list(map(int, os.getenv("5494083050").split()))


contact_filter = filters.create(
    lambda _, __, message: (message.from_user and message.from_user.is_contact)
    or message.outgoing
)

bot = Client(SESSION, API_ID, API_HASH, plugins=dict(root="MusicAndVideo"))
call_py = PyTgCalls(bot)
