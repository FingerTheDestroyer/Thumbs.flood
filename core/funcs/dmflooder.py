from core.utils.plugins import *
from main import main
import discord 
import asyncio
from datetime import datetime
import time

def confirmation():
    option = input(f"     {w}[{grn}?{w}] {grn}are you {l_grn}sure {ll_grn}?(y/n/op{lll_grn}tions)   {b}→  {w}")
    if option == "2" or option.lower() == "n":
        return "go back"
    elif option == "1": 
        return "edit"
    elif option.lower() == "y":
        return "yes"
    else:
        return "confirm again"

async def spam(uid, message, limit, token):
    os.system('title DM flooder')

    intents = discord.Intents.all()
    client = discord.Client(intents= intents)

    @client.event
    async def on_ready():
        current_time = datetime.now().strftime("[%H: %M: %S]")

        print(f"{b}{current_time} {w}[{grn}+{w}]     {grn}{client.user.name} {l_grn}loa{ll_grn}ded")
        await asyncio.sleep(1)    
        try: 
            target = await client.fetch_user(uid)
            for _ in range(limit):
                current_time = datetime.now().strftime("[%H: %M: %S]")
                try:
                    await target.send(message)
                    await asyncio.sleep(0.5)
                    print(f"{b}{current_time}  {grn}[SUCCESS]  {w}sent {message}    | {token[:-25]}...      |    bot: {client.user.name} {w}")
                except discord.Forbidden:
                    print(f"{b}{current_time} {r}[FAILURE]     {w}DMs are closed {w}")
                    return
                except Exception as e:
                    print(f"Unexpected error: {e}")
                    return
        finally:
            await client.close()
    try:
        await client.start(token)
    finally:
        await client.close()







async def dmflooder():
    while True:
        cls()

        print(banner)
        print(credit)
        print(menu_dmflooder)

        USER_ID = input(f"     {w}[{grn}?{w}] {grn}us{l_grn}er {ll_grn}id   {b}→  {w}")
        MESSAGE = input(f"     {w}[{grn}?{w}] {grn}me{l_grn}ss{ll_grn}age   {b}→  {w}")

        while True:
                limit = input(f'     {w}[{grn}?{w}] {grn}amo{l_grn}unt({ll_grn}mini{lll_grn}mum: 2)   {b}→  {w}')
                if str(limit).strip().isdigit() and int(limit) != 1:
                    limit = int(limit)
                    break
                else:
                    print("     Please enter an interger >= 2")
        
        while True:
                answer = confirmation()            
                if answer == "confirm again":
                    print("     Please enter a valid options")
                    continue
                break
        answer = answer.strip().lower()

        if answer == "go back":
            return
        elif answer == "yes":
            pass
        elif answer == "edit":
            continue

        cls()
        print("Waiting..... This should'nt take too long")


        tasks = [spam(USER_ID, MESSAGE, limit, token) for token in tokens]
        #await asyncio.run(main)
        await asyncio.gather(*tasks)
        break
    return
        
        