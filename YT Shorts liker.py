import pyautogui
import webbrowser
import time
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
assets_dir = os.path.join(script_dir, "assets")

# values need to be changed as per display size currently on 1920 x 1080
# print(pyautogui.displayMousePosition()) 
#values
#start - 913, 137 - youtube search bar
#type
#search - 1260, 136 search button 

choice = input('''
What do you want to automatise:
      1. Like All Videos of a particular channel
      2. Unlike All Videos of a particular channel
      3. Like and Subscibe a particular video and its belonging channel
Enter the number preceeding to choice you targeting: 
      ''')

match choice:
    case "1":
        # channel = input("Enter the name of the Youtube Channel:  ")
        # webbrowser.open("youtube.com", new=0, autoraise=True)
        # time.sleep(3)
        # pyautogui.click(913, 137, 1) #start value
        # time.sleep(2)
        # pyautogui.write(channel + " Youtube channel")
        # pyautogui.dragTo(1260, 136) #search
        # pyautogui.click(1260, 136, 1) #search
        # time.sleep(1)
        # pyautogui.click(643, 398)
        time.sleep(2)
        
        img_path = os.path.join(assets_dir, 'shorts.png')
        try:
            short = pyautogui.locateCenterOnScreen(img_path, confidence=0.8)
            if short:
                pyautogui.moveTo(short.x, short.y, duration=1)
                pyautogui.click()
        except:
            pass

        time.sleep(2)
        pyautogui.click(414, 882)
        pyautogui.dragTo(1277, 405)
        pyautogui.click(1277, 405)
        
        while True:
            pyautogui.dragTo(1849, 642)
            pyautogui.click(1849, 642)
            time.sleep(1)
            pyautogui.dragTo(1277, 405)
            pyautogui.click(1277, 405)
            time.sleep(1)

    case "2":
        channel = input("Enter the name of the Youtube Channel:  ")
        webbrowser.open("youtube.com", new=0, autoraise=True)
        time.sleep(3)
        pyautogui.click(913, 137, 1)
        time.sleep(2)
        pyautogui.write(channel + " Youtube channel")
        pyautogui.dragTo(1260, 136)
        pyautogui.click(1260, 136, 1)
        time.sleep(1)
        pyautogui.click(643, 398)
        time.sleep(2)

        img_path = os.path.join(assets_dir, 'shorts.png')
        try:
            short = pyautogui.locateCenterOnScreen(img_path, confidence=0.8)
            if short:
                pyautogui.moveTo(short.x, short.y, duration=1)
                pyautogui.click()
                time.sleep(2)
        except:
            pass

        pyautogui.click(546, 913)
        pyautogui.dragTo(1272, 513)
        pyautogui.click(1272, 513)
        while True:
            pyautogui.dragTo(1849, 638)
            pyautogui.click(1849, 638)
            time.sleep(1)
            pyautogui.dragTo(1272, 513)
            pyautogui.click(1272, 513)
            time.sleep(1)

    case "3":
        vid = input("Enter title you want to search for auto like and subscribe: ")
        webbrowser.open("youtube.com", new=0, autoraise=True)
        time.sleep(3)
        pyautogui.click(913, 137, 1)
        time.sleep(2)
        pyautogui.write(vid)
        pyautogui.dragTo(1260, 136)
        pyautogui.click(1260, 136, 1)
        time.sleep(1)
        pyautogui.click(623, 451, 1)
        time.sleep(3)
        
        img_path_like = os.path.join(assets_dir, 'like.png')
        try:
            location_like = pyautogui.locateCenterOnScreen(img_path_like, confidence=0.8)
            if location_like:
                pyautogui.moveTo(location_like.x, location_like.y, duration=1)
                pyautogui.click()
        except:
            pass

        time.sleep(1)
        
        img_path_subs = os.path.join(assets_dir, 'subscribe.png')
        try:
            location_subs = pyautogui.locateCenterOnScreen(img_path_subs, confidence=0.8)
            if location_subs:
                pyautogui.moveTo(location_subs.x, location_subs.y, duration=1)
                pyautogui.click()
        except:
            pass

    case _ :
        print("Choice not mentioned please run the program again")