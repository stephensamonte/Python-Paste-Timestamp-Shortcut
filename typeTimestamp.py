
# For printing to cursor
import pyautogui as ag
# For retrieving the current date
import datetime

# ag.typewrite("hello Geeks !")
# Retrieve the current date time
time = datetime.datetime.now()

# formate the current date time and convert it into a sstring
timeStamp = time.strftime("%Y.%m.%d %H.%M.%S")

# type the current date to the cursor location
ag.typewrite(timeStamp)

# print(timeStamp)