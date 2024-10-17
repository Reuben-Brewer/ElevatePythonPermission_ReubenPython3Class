# -*- coding: utf-8 -*-

'''
Reuben Brewer, Ph.D.
reuben.brewer@gmail.com
www.reubotics.com

Apache 2 License
Software Revision A, 10/17/2024

Verified working on: Python 3.12 for Windows 10 64-bit.
'''

__author__ = 'reuben.brewer'

###########################################################
from ElevatePythonPermission_ReubenPython3Class import *
###########################################################

###########################################################
import os
import sys
import platform
import time
import datetime
import traceback
import subprocess
###########################################################

#######################################################################################################################
#######################################################################################################################
if __name__ == '__main__':

    ####################################################
    ####################################################
    global USE_ElevatePythonPermission_FLAG
    USE_ElevatePythonPermission_FLAG = 1
    ####################################################
    ####################################################

    ''' #DON'T NEED TO USE THIS IN OUR TYPICAL WAY.
    ####################################################
    ####################################################
    global ElevatePythonPermission_ReubenPython3ClassObject

    global ElevatePythonPermission_OPEN_FLAG
    ElevatePythonPermission_OPEN_FLAG = -1
    ####################################################
    ####################################################

    ####################################################
    ####################################################
    if USE_ElevatePythonPermission_FLAG == 1:
        try:

            ElevatePythonPermission_ReubenPython3ClassObject = ElevatePythonPermission_ReubenPython3Class(dict())
            ElevatePythonPermission_OPEN_FLAG = ElevatePythonPermission_ReubenPython3ClassObject.OBJECT_CREATED_SUCCESSFULLY_FLAG

        except:
            exceptions = sys.exc_info()[0]
            print("ElevatePythonPermission_ReubenPython3Class __init__: Exceptions: %s" % exceptions)
            traceback.print_exc()
    ####################################################
    ####################################################
    '''

    ####################################################
    ####################################################
    ####################################################
    print("Starting main loop for test_program_for_ElevatePythonPermission_ReubenPython3Class.py...")

    ####################################################
    ####################################################
    if USE_ElevatePythonPermission_FLAG == 1:
        try:
            ElevatePythonPermission_ReubenPython3Class.RunPythonAsAdmin()

        except:
            exceptions = sys.exc_info()[0]
            print("Exceptions: %s" % exceptions)
            traceback.print_exc()
    ####################################################
    ####################################################

    ####################################################
    ####################################################
    try:
        shell_command_to_issue = "C:\\Program Files (x86)\\MotionLab3\\_internal\\eoe_service\\IngEcatGateway.exe"
        #print("shell_command_to_issue: " + shell_command_to_issue)

        process = subprocess.Popen([shell_command_to_issue])  # subprocess.Popen doesn't wait for process to terminate
        time.sleep(2.0)

    except:
        pass
        #exceptions = sys.exc_info()[0]
        #print("Exceptions: %s" % exceptions)
        #traceback.print_exc()
    ####################################################
    ####################################################

    while 1:
        time.sleep(1.0)

    print("Exiting main program 'test_program_for_ElevatePythonPermission_ReubenPython3Class.")

    ####################################################
    ####################################################
    ####################################################

#######################################################################################################################
#######################################################################################################################