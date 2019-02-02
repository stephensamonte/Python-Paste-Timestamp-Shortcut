# Check if pyautogui exists
import pyautogui as ag

import datetime
# ag.typewrite("hello Geeks !")

time = datetime.datetime.now()

timeStamp = time.strftime("%Y.%m.%d %H.%M.%S")
ag.typewrite(timeStamp)
# print(timeStamp)