#!/usr/bin/env python3.6
from os import path,mkdir,name
if name == 'nt': # fix colors in windows
    from colorama import init
    init()
from src.core.consoleUI import Console
from src.core.utils.color import banner
version = '1.0'
author  = 'xzebra'
name='muZic'
version='1.0'

def main():
    shell = Console()
    shell.cmdloop(banner(version,author))

if __name__ == "__main__":
    main()
