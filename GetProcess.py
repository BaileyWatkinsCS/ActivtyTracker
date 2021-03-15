import sys
from win32gui import GetForegroundWindow
import psutil
import time
import win32process
import win32gui
from idle_time import IdleMonitor
import json

def minute_passed(oldepoch):
    return time.time() - oldepoch >= 60


process_time = {}
timestamp = {}
fullList = {}
while True:
    try: 

        # isIdle = False     
        # monitor = IdleMonitor.get_monitor()
        # IdleTimes = int(monitor.get_idle_time())
        # if IdleTimes >= 5:
        #     isIdle = True
        
        try:
            current_app = psutil.Process(win32process.GetWindowThreadProcessId(
                GetForegroundWindow())[-1]).name().replace(".exe", "")
        except:
            print("Psutil Failed")
        ActiveWindow = str(win32gui.GetWindowText(win32gui.GetForegroundWindow()))
        SplitWindow = ActiveWindow.split('-')
        timestamp[current_app] = int(time.time())
        time.sleep(1)
        if current_app not in process_time.keys():
            process_time[current_app] = 0       
        process_time[current_app] = process_time[current_app] + int(time.time())-timestamp[current_app]
        
        # if IdleTimes not in process_time.keys():
        #     process_time[IdleTimes] = 0       
        # process_time[IdleTimes] = process_time[IdleTimes] + IdleTimes


        jsonTest = {
            "AppName" : current_app,
            "AppInfo" : ActiveWindow,
            "ProcessTime" : process_time[current_app]
            # "IdleTime" : process_time[IdleTimes]
        }
        json_data = json.dumps(jsonTest)
        print(json_data)
    except:
        print("Oops!", sys.exc_info()[0], "occurred.")
        break  # if user pressed a key other than the given key the loop will break
