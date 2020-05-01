"""команда: .obmen usd rub"""
from telethon import events
import asyncio
from datetime import datetime
import requests
from uniborg.util import admin_cmd


@borg.on(admin_cmd("obmen (.*)"))
async def _(event):
    if event.fwd_from:
        return
    start = datetime.now()
    input_str = event.pattern_match.group(1)
    input_sgra = input_str.split(" ")
    if len(input_sgra) == 3:
        try:
            nomer = float(input_sgra[0])
            currency_from = input_sgra[1].upper()
            currency_to = input_sgra[2].upper()
            request_url = "https://api.exchangeratesapi.io/latest?base={}".format(currency_from)
            current_response = requests.get(request_url).json()
            if currency_to in current_response["rates"]:
                current_rate = float(current_response["rates"][currency_to])
                rebmun = round(nomer * current_rate, 2)
                await event.edit("{} {} = {} {}".format(nomer, currency_from, rebmun, currency_to))
            else:
                await event.edit("НИЧЕГО НЕ ПОНИМАЮ")
        except e:
            await event.edit(str(e))
    else:
        await event.edit("`.obmen -число- -из- -в-`")
    end = datetime.now()
    ms = (end - start).seconds
