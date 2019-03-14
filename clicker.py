import win32api, win32con, time

def click():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

try:
    import keyboard

    toggle = False
    while True:
        if keyboard.is_pressed("f1"):
            toggle = not toggle

        if keyboard.is_pressed("-"):
            quit()

        time.sleep(.100)
        if toggle:
            click()

except:
    print("Error, Module Keyboard is required. Run \"pip install keyboard\" and try again")

