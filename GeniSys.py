############################################################################################
# Title:         GeniSys AI
# Description:   Open source project working towards general intelligence by combining 
#                multiple separate models into one general application.
# Last Modified: 2018-07-29
############################################################################################

from Tools.Logging import Logging

class geniSysAI():

    def __init__(self):

        self.Logging = Logging()
        self.Logging.consoleLog(
            "SYSTEM",
            "GeniSys AI Initiating"
        )

geniSysAI = geniSysAI()