
import keyboard
import sys
sys.path.append(
    "C:/Users/Raphaelle/Documents/UniDocs/Automne 2021/Architecture_logiciels/lab2/6GEI311_lab2/x64/Release")

import Lab2

quit = False


def stop():
    Lab2.Quit()
    global quit
    quit = True


keyboard.on_press_key("q", lambda _: stop())
keyboard.on_press_key("p", lambda _: Lab2.PlayPause())
keyboard.on_press_key("r", lambda _: Lab2.Replay())
keyboard.on_press_key("a", lambda _: Lab2.Accelerate())

Lab2.Start("", "C:/Users/Raphaelle/Documents/UniDocs/Automne 2021/Architecture_logiciels/6GEI311_lab1/Example.avi")

while(not quit):
    pass

# Source:
# https://stackoverflow.com/questions/24072790/how-to-detect-key-presses
keyboard.unhook_all()