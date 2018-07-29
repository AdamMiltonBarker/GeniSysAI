############################################################################################
# Title:         GeniSys AI
# Description:   Open source project working towards general intelligence by combining 
#                multiple separate models into one general application.
# Last Modified: 2018-07-29
############################################################################################

from Tools.Logging import Logging
from Tools.Threading import Threading

from Core.ComputerVision import ComputerVision
from Core.NLU import NLU

class geniSysAI():

    def __init__(self):

        self.Logging        = Logging()
        self.Threading      = Threading()
        self.NLU            = NLU()
        self.ComputerVision = ComputerVision()

        self.Logging.consoleLog(
            "SYSTEM|OK",
            "GeniSys AI Initiated"
        )

    def startThreading(self):
        
        self.Threading.appendProcess(self.ComputerVision)
        self.Threading.appendProcess(self.NLU)

        self.Logging.consoleLog(
            "SYSTEM|OK",
            "GeniSys AI Threading Started"
        )

geniSysAI = geniSysAI()
geniSysAI.startThreading()

geniSysAI.Logging.consoleLog(
    "SYSTEM|OK",
    "GeniSys AI Exiting"
)