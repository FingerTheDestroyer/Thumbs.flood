from pystyle import Add, Center, Anime, Colors, Colorate, Write, System
from colorama import Fore, Style
import os
import fade

def cls():
    os.system('cls')

grn = '\x1b[38;5;46m'
l_grn = '\x1b[38;5;47m'
ll_grn = '\x1b[38;5;83m'
lll_grn = '\x1b[38;5;84m'
r = '\x1b[38;5;196m'

b = Fore.LIGHTBLACK_EX
w = Fore.WHITE


script_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(script_dir, os.pardir))
parent_dir = os.path.abspath(os.path.join(parent_dir, os.pardir))
file_path = os.path.join(parent_dir, "tokens.txt")


with open(file_path, "r") as f:
    tokens = f.read().splitlines()

tokens_cnt = len(tokens)




banner = f'''
                         ________                    __           ______                __   
                        /_  __/ /_  __  ______ ___  / /_  _____  / __/ /___  ____  ____/ /   
                         / / / __ \/ / / / __ `__ \/ __ \/ ___/ / /_/ / __ \/ __ \/ __  /    
                        / / / / / / /_/ / / / / / / /_/ (__  ) / __/ / /_/ / /_/ / /_/ /     
                       /_/ /_/ /_/\__,_/_/ /_/ /_/_.___/____(_)_/ /_/\____/\____/\__,_/     '''                                 


credit = f'''                                    {w}made by: {grn}Finger   {b}|   {w}discord: {grn}fg27
                              {w}────────────────────────────────────────────────
                                             {w}loaded: {b}<{grn}{tokens_cnt}{b}> {w}tokens '''


banner = fade.brazil(banner)



menu = f'''                                          

                    {w}[{grn}1{w}]: {grn}DM {l_grn}fl{ll_grn}oo{lll_grn}der
                    {w}[{grn}e{w}]: {grn}ex{l_grn}i{ll_grn}t


'''



menu_dmflooder = f'''
            {w}[{grn}OP{l_grn}TI{ll_grn}ON{lll_grn}S{w}]

            {w}[{grn}1{w}]: {grn}ed{l_grn}it
            {w}[{grn}2{w}]: {grn}go {l_grn}b{ll_grn}ac{lll_grn}k


'''

