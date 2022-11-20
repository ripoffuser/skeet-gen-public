import os
import random
import time
import colorama
import sys
from os import system, name
from time import sleep
from colorama import Fore, Back, Style

os.system("title skeet gen v1")
colorama.init()
import time
import random


def cls():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)


    #functions
def g(rolls):
    data = "qwertyuioplkjhgfdsazxcvbnm1234567890QWERTYUIOPLKJHGFDSAZXCVBNM"
    result = ""
    while rolls >= 1:
        c = random.choice(data)
        result = c + result
        rolls = rolls - 1
    return result
