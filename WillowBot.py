import time
import pyautogui
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt


pyautogui.FAILSAFE = True ## This enables you to cancel script by moving mouse to furthest top left corner. Or press CTRL + C to cancel


## Oak logs bank run, only works near west varrock oak logs, definitely not done with this function. Not called by default
def bankRun():
    count = 0
    topCompass = pyautogui.locateOnScreen("compass.png", confidence=0.4)
    banklocation = pyautogui.locateOnScreen("bank.png", confidence=0.45)
    if (topCompass):
        while (count < 4):
            if (banklocation):
                print('True...... I see the bank')
                pyautogui.moveTo(banklocation, duration=1)
                pyautogui.click()
                break
            pyautogui.moveTo(topCompass, duration=1) ## brings cursor to the top compass minimap thingy
            pyautogui.move(90, 0) ## moves cursor on the x axis away from the compass
            pyautogui.click()
            time.sleep(5)
            count += 1
            
    else:
        print('damn cant find...')
        time.sleep(5)

## Returns user back from draynor bank to East Port Sarim
def returnbackBank():
    time.sleep(3)
    count = 0
    topCompass = pyautogui.locateOnScreen("compass.png", confidence=0.4)
    print ('Returning back to willow treezzzzz')
    if (topCompass):
        while (count < 1):
            pyautogui.moveTo(topCompass, duration=1) ## brings cursor to the top compass minimap thingy
            pyautogui.move(20, 60) ## moves cursor on the x axis away from the compass
            pyautogui.click()
            time.sleep(25)
            pyautogui.move(0, -20)
            pyautogui.click()
            count += 1
        
        time.sleep(34)    
        willowTrees()    
    else:
        print('damn cant find top compass... adjust confidence level in script for topCompass variable')
        time.sleep(5)







## Runs to the bank from East Port Sarim willow trees to draynor village
def willowbankRun():
    count = 0
    topCompass = pyautogui.locateOnScreen("compass.png", confidence=0.4)
    #banklocation = pyautogui.locateOnScreen("portsarim_bank.png", confidence=0.39)
    #bankteller = pyautogui.locateOnScreen("bankteller2.png", confidence=0.35) ##.27 worked pretty good
    fullinventory = pyautogui.locateOnScreen("fullinventory.png", confidence=0.8)
    print ('Exeucting bank run script...')
    if (topCompass):
        while (count < 2):
                try:
                    banklocation = pyautogui.locateOnScreen("portsarim_bank2.png", confidence=0.32) ## .37 worked alright
                    banklocation = pyautogui.locateOnScreen("portsarim_bank3.png", confidence=0.32) ## .37 worked alright
                except:
                    print ('Unable to find bank.')
                if (banklocation):
                    print('True...... I see the bank')
                    pyautogui.moveTo(banklocation, duration=1)
                    pyautogui.click()
                    time.sleep(16)
                bankteller = pyautogui.locateOnScreen("bankteller3.png", confidence=0.35)    
                if (bankteller):
                    count1 = 0
                    while (count1 < 2):
                        count1 += 1
                        print('Wait...... I see the bankteller now')
                        #centerofteller = pyautogui.center(bankteller)
                        pyautogui.moveTo(bankteller, duration=1)
                        pyautogui.click()  ## This click should open up bank
                        bankinventory = pyautogui.locateOnScreen("bankinventory.png", confidence=0.5) ##  .6 works pretty well
                        time.sleep(5)
                    if (bankinventory):
                        print ('Detected bank inventory opened up')
                        pyautogui.moveTo(fullinventory, duration=1)
                        pyautogui.move(20, 50)
                        pyautogui.click(button='right')
                        pyautogui.move(0, 80)
                        pyautogui.click()
                        returnbackBank() ## call a return back function now I guess
                    else:
                        time.sleep(2)
                        count2 = 0
                        while (count2 < 2):
                            try:
                                count2 += 1
                                bankinventory = pyautogui.locateOnScreen("bankinventory.png", confidence=0.5)
                                if (bankinventory):
                                    print ('Detected bank inventory opened up')
                                    pyautogui.moveTo(fullinventory, duration=1)
                                    pyautogui.move(20, 50)
                                    pyautogui.click(button='right')
                                    pyautogui.move(0, 80)
                                    pyautogui.click()
                                    returnbackBank()
                            except:
                                print ('Did not detect inventory...')
                else:
                    print ("Unable to detect bank teller. Sleeping and retrying.")
                    bankteller = pyautogui.locateOnScreen("bankteller3.png", confidence=0.34)
                    #### BOILER PLATE BEGIN
                    if (bankteller):
                        count1 = 0
                        while (count1 < 2):
                            count1 += 1
                            print('Wait...... I see the bankteller now... boiler plate section')
                            #centerofteller = pyautogui.center(bankteller)
                            pyautogui.moveTo(bankteller, duration=1)
                            pyautogui.click()  ## This click should open up bank
                            bankinventory = pyautogui.locateOnScreen("bankinventory.png", confidence=0.5) ##  .6 works pretty well
                            time.sleep(5)
                            if (bankinventory):
                                print ('Detected bank inventory opened up')
                                pyautogui.moveTo(fullinventory, duration=1)
                                pyautogui.move(20, 50)
                                pyautogui.click(button='right')
                                pyautogui.move(0, 80)
                                pyautogui.click()
                                returnbackBank() ## call a return back function now I guess
                            else:
                                time.sleep(2)
                                count2 = 0
                                while (count2 < 2):
                                    try:
                                        count2 += 1
                                        bankinventory = pyautogui.locateOnScreen("bankinventory.png", confidence=0.5)
                                        if (bankinventory):
                                            print ('Detected bank inventory opened up')
                                            pyautogui.moveTo(fullinventory, duration=1)
                                            pyautogui.move(20, 50)
                                            pyautogui.click(button='right')
                                            pyautogui.move(0, 80)
                                            pyautogui.click()
                                            returnbackBank()
                                    except:
                                        print ('Did not detect inventory...')
                        
                    
                    bankteller = pyautogui.locateOnScreen("bankteller3.png", confidence=0.32)
                    print (bankteller)
                    #### BOILER PLATE END
                    time.sleep(3)
                
                ## While count is less than 2 click to the right side of mini map to get to bank area 
                print ('Moving towards bank...')
                pyautogui.moveTo(topCompass, duration=1) ## brings cursor to the top compass minimap thingy
                pyautogui.move(135, 90) ## moves cursor on the x axis away from the compass
                pyautogui.click()
                time.sleep(40)
                print ('Adjusting cursor upwards..')
                pyautogui.move(0, -50)
                pyautogui.click()
                time.sleep(10)
                count += 1    
            
    else:
        print('damn cant find...')
        time.sleep(5)

## This function detects and cuts willow trees, and then calls the bank function when a full inventory is detected
def willowTrees():
    allTrees = ["willow.png", "willow2.png", "willow3.png", "willow4.png"]
    count = 0
    while (1==1):
        for treepic in allTrees:
            fullinventory = pyautogui.locateOnScreen("fullinventory.png", confidence=0.85)
            if (fullinventory):
                    print ('Full inventory detected. Headed to bank.')
                    willowbankRun()
                    break
            print(f"Looking for {treepic}")
            treelocation = pyautogui.locateOnScreen(treepic, confidence=0.39) ## Adjust confidence level of images (Valid entries: 0-1)
            if (treelocation):
                #fullinventory = pyautogui.locateOnScreen("fullinventory.png", confidence=0.8)
                print (f"{treelocation}")
                centeroftree = pyautogui.center(treelocation)
                pyautogui.moveTo(centeroftree, duration=1)
                pyautogui.click()
                time.sleep(40)
                 ## Break out of for loop so we restart the process and begin searching for first pic in array
                break
            else:
                print("None found, searching and waiting for more.. moving eventually")
                time.sleep(2) ## sleep 2 secs in between looking for trees to account for trees that respawn
                if (count > 3):
                    #pyautogui.moveTo(treelocation, duration=1)
                    #pyautogui.click()
                    count = 0
                count += 1
                try:
                    if (fullinventory):
                        print('Full inventory... waiting 3 times')
                        willowbankRun()
                except:
                        continue     

willowTrees()

## This is the function for woodcutting oak logs. Best location is west varrock
def oakLogs():
    allTrees = ["oak9.png", "oak10.png", "oak6.png", "oak7.png", "oak8.png", "oak4.png", "oak5.png", "oak2.png", "oak.png", "oak3.png"]
    count = 0
    while (1==1):
        for treepic in allTrees:
            print(f"Looking for {treepic}")
            treelocation = pyautogui.locateOnScreen(treepic, confidence=0.33) ## Adjust confidence level of images (Valid entries: 0-1)
            if (treelocation):
                fullinventory = pyautogui.locateOnScreen("fullinventory.png", confidence=0.8)
                print (f"{treelocation}")
                centeroftree = pyautogui.center(treelocation)
                pyautogui.moveTo(centeroftree, duration=1)
                pyautogui.click()
                time.sleep(25)
                if (fullinventory):
                    print ('Full inventory detected. Headed to bank.')
                    bankRun()
                break ## Break out of for loop so we restart the process and begin searching for first pic in array
                
            else:
                print("None found, searching and waiting for more.. moving eventually")
                #time.sleep(2) ## sleep 2 secs in between looking for trees to account for trees that respawn
                if (count > 3):
                    #pyautogui.moveTo(treelocation, duration=1)
                    #pyautogui.click()
                    count = 0
                count += 1
                try:
                    if (fullinventory):
                        print('Full inventory... waiting 3 times')
                except:
                        continue           
#oakLogs()

## Woodcutting function for regular logs
def regularLogs():
    allTrees = ["exact.png", "exact2.png", "pinetree2.png", "exact3.png", "exact4.png", "exact5.png", "pinetree.png", "leaves.png"]
    count = 0
    while (1==1):
        for treepic in allTrees:
            print(f"Looking for {treepic}")
            treelocation = pyautogui.locateOnScreen(treepic, confidence=0.4) ## Adjust confidence level of images (Valid entries: 0-1)
            if (treelocation):
                print (f"{treelocation}")
                centeroftree = pyautogui.center(treelocation)
                pyautogui.moveTo(centeroftree, duration=1)
                pyautogui.click()
                time.sleep(10)
                break ## Break out of for loop so we restart the process and begin searching for first pic in array
            else:
                print("None found, searching and waiting for more.. moving eventually")
                time.sleep(2) ## sleep 2 secs in between looking for trees to account for trees that respawn
                if (count > 3):
                    pyautogui.moveTo(treelocation, duration=1)
                    pyautogui.click()
                    count = 0
                count += 1






















#img_gray = cv.cvtColor(img_rgb, cv.COLOR_BGR2GRAY)   We get errors if we try to convert to grayscale, despite what docs do
#img = cv.imread('oakwithbackground.png',0)
    
       
#### Additional pyautogui methods
#pyautogui.moveTo(250, 300, duration=2)
#pyautogui.click()
#pyautogui.PAUSE = 10 ## Pause for 10 seconds
#Take screenshots and save to output file
#im2 = pyautogui.screenshot('output.png')
####

## LATER - try to inverse current location of tree and move to that when none are found. Essentially moves character back towards where tree was initially:
#TreeLocationString = str(treelocation)
#print(re.sub('[1-9][1-9][1-9]', 'yo', TreeLocationString))
