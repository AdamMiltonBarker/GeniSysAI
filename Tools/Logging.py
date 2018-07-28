############################################################################################
# Title:         GeniSys AI Logging
# Description:   Class to handle all application logging.
# Last Modified: 2018-07-29
############################################################################################

import time

class Logging():
    
    def consoleLog(self, status, message):
        
        print("["+status+"] "+message+" | "+ time.strftime("%c"))
    
    def fileLog(self, status, message):
        
        print("["+status+"] "+message+" | "+ time.strftime("%c"))


