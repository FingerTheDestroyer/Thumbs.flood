from core.funcs.dmflooder import *
from core.utils.plugins import *
import asyncio
import sys
import time

async def main():
    while True:
        cls()
        os.system('title Thumbs.flood')
        print(banner)
        print(credit)
        print(menu)

        choice = input(f"     {w}[{grn}?{w}]  {grn}IN{l_grn}P{ll_grn}UT  {b}→  {w}")

        if choice.strip() == '1':
            await dmflooder()
            input("press enter to go back")
            continue

        if choice.strip().lower() == 'e':
            sys.exit(0)
        
        else:
            continue


if __name__  == "__main__":
    asyncio.run(main())