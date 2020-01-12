import threading, time
from pynput import mouse, keyboard

class Mouse(threading.Thread):
    def __init__(self, delaytimer, **kwargs):
        threading.Thread.__init__(self, **kwargs)
        self.delaytimer = delaytimer
        self.cursor = mouse.Controller()
        self.running = False
        self.program_running = True
        self.mouse_button = None

    def toggle(self):
        self.running = not self.running

    def mouse_change(self, mouse_button):
        self.mouse_button = mouse_button

    def stop(self):
        self.running = False
        self.program_running = False

    def run(self): # NOTE: In threading.Thread default runs self.run() when .start() is called.
        while self.program_running:
            while self.running:
                time.sleep(self.delaytimer)
                if self.mouse_button == "mouse1":
                    self.cursor.click(mouse.Button.left,2)
                elif self.mouse_button == "mouse2":
                    self.cursor.click(mouse.Button.right,2)
