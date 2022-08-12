# Please read this modules documentation -> https://github.com/codeuk/pipware

# This is just a simple prgram to showcase that you should only download trusted packages.
# PIPWARE will print your data on screen but real package malware(s) will send it away without you knowing.

import requests, platform
from requests import get as GET
SYS = platform.uname()

class PROGRAM():

    def __init__(self):
        self.INFO = {
            "IP":  GET('https://api.ipify.org/').text,
            "SYS": SYS.system,
            "USER":SYS.node,
            "VER": SYS.release,
            "PC":  SYS.machine
        }

    def MENU(self):
        print("""                    
                                    PIPWARE -> codeuk/pipware                                                                
                [*] Make sure you double check that you're installing the correct package!
                [*] Also, don't run any sketchy packages and only use trusted ones.\n""")

    def WARE(self):
        self.MENU()

        for key in self.INFO:
            print(f"        {key} -> {self.INFO[key]}")
        print()

PIP = PROGRAM()
PIP.WARE()
