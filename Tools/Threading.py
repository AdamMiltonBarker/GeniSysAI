############################################################################################
# Title:         GeniSys AI Threading
# Description:   Class to handle all application threading.
# Last Modified: 2018-07-29
############################################################################################

import multiprocessing

class Threading():
    
    def __init__(self):
        
        self.processes = []

    def appendProcess(self, target):
        
        self.processes.append(multiprocessing.Process(target=target))

    def getProcesses(self):

        return self.processes

    def getProcessesCount(self):

        return len(self.processes)

    def runProccesses(self):

        self.processes[-1].start()


