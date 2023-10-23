from googlesearch import search
from colorama import Fore, Style
import os
import time
from fake_useragent import UserAgent
import requests

class Color:
    BRIGHT_RED           = Style.BRIGHT + Fore.RED
    BRIGHT_CYAN          = Style.BRIGHT + Fore.CYAN
    BRIGHT_WHITE         = Style.BRIGHT + Fore.WHITE
    BRIGHT_GREEN         = Style.BRIGHT + Fore.GREEN
    BRIGHT_YELLOW        = Style.BRIGHT + Fore.YELLOW
    BRIGHT_BLUE          = Style.BRIGHT + Fore.BLUE
    BRIGHT_LIGHTWHITE_EX = Style.BRIGHT + Fore.LIGHTWHITE_EX


ua = UserAgent()

def continue_search():
    while True:
        answer = input(f"{Color.BRIGHT_CYAN}\n[<-] MYOPECS [->]{Color.BRIGHT_GREEN} - Continue the search? (yes/no): {Color.BRIGHT_YELLOW}")
        if answer.lower() in ['yes', 'y']:
            return True
        elif answer.lower() in ['no', 'n']:
            return False
        else:
            print(f"{Color.BRIGHT_RED}Invalid input. Please enter 'yes' or 'no'.")

def banners():
    print()
    print(Color.BRIGHT_LIGHTWHITE_EX + "       ███╗   ███╗██╗   ██╗ ██████╗ ██████╗ ███████╗ ██████╗███████╗")
    print(Color.BRIGHT_LIGHTWHITE_EX + "       ████╗ ████║╚██╗ ██╔╝██╔═══██╗██╔══██╗██╔════╝██╔════╝██╔════╝")
    print(Color.BRIGHT_LIGHTWHITE_EX + "       ██╔████╔██║ ╚████╔╝ ██║   ██║██████╔╝█████╗  ██║     ███████╗")
    print(Color.BRIGHT_LIGHTWHITE_EX + "       ██║╚██╔╝██║  ╚██╔╝  ██║   ██║██╔═══╝ ██╔══╝  ██║     ╚════██║")
    print(Color.BRIGHT_LIGHTWHITE_EX + "       ██║ ╚═╝ ██║   ██║   ╚██████╔╝██║     ███████╗╚██████╗███████║")
    print(Color.BRIGHT_LIGHTWHITE_EX + "       ╚═╝     ╚═╝   ╚═╝    ╚═════╝ ╚═╝     ╚══════╝ ╚═════╝╚══════╝")
    print(Color.BRIGHT_BLUE + "     ------------------ Author: Monyet C0mel ------------------------")

banners()

try:
    
    dork = input(f"{Color.BRIGHT_YELLOW}\n[<-] MYOPECS [->]{Color.BRIGHT_RED} - {Color.BRIGHT_GREEN}Dork: {Color.BRIGHT_CYAN}")
    amount = int(input(f"{Color.BRIGHT_YELLOW}\n[<-] MYOPECS [->]{Color.BRIGHT_RED} - {Color.BRIGHT_GREEN}Amount: {Color.BRIGHT_CYAN}"))
    time_seconds = int(input(f"{Color.BRIGHT_YELLOW}\n[<-] MYOPECS [->]{Color.BRIGHT_RED} - {Color.BRIGHT_GREEN}Time (Seconds): {Color.BRIGHT_CYAN}"))

    #Time Delay
    time_delay = time_seconds * 10

    custom_file_name = input(f"{Color.BRIGHT_YELLOW}\n[<-] MYOPECS[->]{Color.BRIGHT_RED} - {Color.BRIGHT_GREEN}File Name You Want to Create: {Color.BRIGHT_CYAN}")
    print(f'{Color.BRIGHT_BLUE}\n═════════════════════════════════════════════')

    result = "result"  # Specify the name of the directory
    os.makedirs(result, exist_ok=True)
    custom_file_path = os.path.join('result', custom_file_name)
  
    count = 0

    while count <= amount:
        headers = {'User-Agent': ua.random}
        for result in search(dork):
            count += 1
            with open(custom_file_path, 'a') as f:
                f.write(f'{result}\n')
            print(f'{Color.BRIGHT_WHITE}       {count}) {Color.BRIGHT_CYAN}{result}')
            if count >= amount:
                break

            time.sleep(time_delay)  # Sleep for the specified time in seconds

        if count >= amount:
            break

        print(f'{Color.BRIGHT_YELLOW}\n[<-] MYOPECS [->]{Color.BRIGHT_GREEN} - Search paused after {count} results.')
        if not continue_search():
            break

    print(f'{Color.BRIGHT_BLUE}═════════════════════════════════════════════')
    print(f'{Color.BRIGHT_YELLOW}\n[<-] MYOPECS [->] {Color.BRIGHT_GREEN}Saved: {Color.BRIGHT_GREEN}{custom_file_path}')

except ValueError:
    exit(f'{Color.BRIGHT_RED}Exit! Input error')

except KeyboardInterrupt:
    exit(f'\n\n{Color.BRIGHT_RED}Exit!')
