import win32api, win32con, time, keyboard

def click():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

toggle = False
while True:
    if keyboard.is_pressed("f1"):
        toggle = not toggle

    if keyboard.is_pressed("-"):
        quit()

    time.sleep(.300)
    if toggle:
        click()
