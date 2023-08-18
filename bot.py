import asyncio
from pyrogram import Client, compose,idle
import os

from plugins.cb_data import app as Client2

TOKEN = os.environ.get("TOKEN", "6517235191:AAF0A550ymSnlbPyNJvf7otys0v6mwuluWk")

API_ID = int(os.environ.get("API_ID", "21165589"))

API_HASH = os.environ.get("API_HASH", "8cc762f4873e84a7cf0cbfd66a07244b")

STRING = os.environ.get("STRING", "")


bot = Client(

           "Renamer",

           bot_token=TOKEN,

           api_id=API_ID,

           api_hash=API_HASH,

           plugins=dict(root='plugins'))
           

if STRING:
    apps = [Client2,bot]
    for app in apps:
        app.start()
    idle()
    for app in apps:
        app.stop()
    
else:
    bot.run()
