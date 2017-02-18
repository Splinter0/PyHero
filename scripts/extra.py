#!/usr/bin/env python
class colors: #DEFINIGN SOME COLORS
    black = "\033[90m"
    red = "\033[31m"
    green = "\033[32m"
    yellow = "\033[1;33m"
    magenta = "\033[95m"
    cyan = "\033[96m"
    white = "\033[97m"
    default = "\033[99m"
    end = '\033[0m'


def logo():
    print(colors.green+"   ___                            ")
    print("  / _ \_   _  /\  /\___ _ __ ___  ")
    print(" / /_)/ | | |/ /_/ / _ \ '__/ _ \ ")
    print("/ ___/| |_| / __  /  __/ | | (_) |")
    print("\/     \__, \/ /_/ \___|_|  \___/ ")
    print("       |___/                      "+colors.end+"By : "+colors.green+"\033[1;45mSplinter"+colors.end+"\r\n")
    print("["+colors.cyan+"*"+colors.end+"] Welcome to PyHero, a python program to control your GoPro HERO from command line!")
    print("\tThis program has tons of default GoPro commands that you can use, but it also has "+colors.green+"special"+colors.end+"\n\tcommands to control your camera better!")
    print("\t"+colors.cyan+"Github Page : "+colors.end+"\r\n")
    raw_input("[PRESS ENTER]")