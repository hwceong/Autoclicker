import threading, time
from pynput import mouse, keyboard

class Mouse(threading.Thread):
    def __init__(self, delaytimer:float):
        threading.Thread.__init__(self)
        self.delaytimer = delaytimer
        self.running = False
        self.program_running = True

    def toggle(self):
        self.running = not self.running

    def exit(self):
        self.running = False
        self.program_running = False

    def run(self): # NOTE: In threading.Thread, it automatically runs self.run() when initialized.
        while self.program_running:
            while self.running:
                time.sleep(self.delaytimer)
                cursor.click(mouse.Button.left,2)

def on_press(key):
    if key == keyboard.KeyCode(char=","):
        mouse_thread.toggle()

    if key == keyboard.Key.esc:
        mouse_thread.exit()
        listener.stop()

if __name__ == '__main__':
    cursor = mouse.Controller()
    mouse_thread = Mouse(0.1)
    mouse_thread.start()

    print("Press \",\" to toggle auto clicking. Press ESC to close to program.")

    with keyboard.Listener(on_press=on_press) as listener: # NOTE: from pynput module, it the keyboard.Listener listens from keyboard input
        listener.join()
