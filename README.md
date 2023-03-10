# WillowBot
Fully automated bot for woodcutting Willow Trees specifically in East Port Sarim. Includes a banking function and will return back to woodcutting location

Proof of concept found here:
https://www.youtube.com/watch?v=Ip6CktKNvgI


🚫 No third-party client

🚫 No plugins

🚫 No bans reported yet

**NOTE:** 
The banking function created in this script will only work if you execute the script while standing in East Port Sarim next to the willow trees. Other than that, script will only work for woodcutting in other locations.

**PREREQS:**
- Python3 (tested on 3.11.1 and 3.10.8)

**HOW TO SETUP:**
- git clone repo
- pip install -r requirements.txt

**HOW TO USE:**
- Move your OSRS character to East Port Sarim willow trees (to the right of the bar there are 4 willow trees)
- Open up your inventory so the script can detect when it is full
- Open up a powershell or cmd prompt in another window
- cd to the script installation directory: type "cd C:\Users\example\Documents\WillowBot\"
- type "python WillowBot.py"
- CTRL+C to cancel script execution for whatever reason. Can always be restarted in this same location.

**TIPS:**
- If you're having trouble with accuracy, try to imitate the screen resolution/zoom/camera angle shown in the above youtube video. This is extremely important for script functionality! Also, while not mandatory, having sprint enabled makes script much more smooth. This is by no means a finished product, but it's a start!
- Script must be executed in East Port Sarim while standing next to the Willow Trees in order to work properly
