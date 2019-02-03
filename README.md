# Python-Paste-Timestamp-Shortcut
I typically write the date manually as part of titles. This program will automate the process for me. 

This program will auto add the timestamp to where the cursor when a specific key binding is pressed. 

NOTE: This project is currently under development and is not complete. 

## Latest Showcase Video: 
[![Latest Showcase](https://img.youtube.com/vi/ttk-PSHRC1w/0.jpg)](https://www.youtube.com/watch?v=ttk-PSHRC1w)

# How to use this program
1. Download the executable to your computer's desktop.
2. Place cursor where you want the date to be placed. 
3. press `control`+`alt`+`0` on your keyboard to paste the date. 

# Environment
This is a simple python program that can be edited with a simple text editor. 

# installs needed dependencies
1. To type at cursor: `pip install pyautogui` 
2. For Hot Key Binding `pip install pynput` 
3. To create an executable: `pip install pyinstaller`

# Test if script runs
`python your_script.py`

# Compile script into executable
`pyinstaller --onefile <your_script_name>.py`
"This will create a standalone executable in the dist directory of your script folder. Don’t worry, if the folder doesn’t exist it will create one automatically. Notice that we passed an argument “— onefile”. This argument tells PyInstaller to create only one file. If you don’t specify this, the libraries will be distributed as separate file along with the executable."

# Journal 
2019.02.02 Created script that types the current date. [Showcase](https://www.youtube.com/watch?v=ttk-PSHRC1w&feature=youtu.be)


# References
- [Quick tip: How to start any Windows app with a keyboard shortcut](https://www.digitalcitizen.life/start-windows-apps-keyboard-shortcut)
- [pyautogui | Mouse and keyboard automation using Python](https://www.geeksforgeeks.org/mouse-keyboard-automation-using-python/)
- [pyinstaller](https://pyinstaller.readthedocs.io/en/stable/)
- [Making a Stand Alone Executable from a Python Script using PyInstaller](https://medium.com/dreamcatcher-its-blog/making-an-stand-alone-executable-from-a-python-script-using-pyinstaller-d1df9170e263)
- [Python Datetime](https://www.w3schools.com/python/python_datetime.asp)
- [Python Hotkeys](https://nitratine.net/blog/post/how-to-make-hotkeys-in-python/?utm_source=pythonanywhere&utm_medium=redirect&utm_campaign=pythonanywhere_organic_redirect)