import tkinter as tk
from autoclicker.commons import clicker


class MainApplication(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        self.click_key = tk.StringVar()
        self.click_key.trace("w", self.key_trace)

        #All elements
        self.frame1 = tk.Frame(
            self.parent
        )

        self.frame2 = tk.Frame(
            self.parent
        )

        self.label = tk.Label(
            self.frame1,
            text="Activation key-binding:"
        )

        self.click_entry = tk.Entry(
            self.frame1,
            textvariable=self.click_key,
            borderwidth=1,
            background=self.parent.cget('bg'),
            font="Calibiri 12 ",
            width=1
        )

        self.start_button = tk.Button(
            self.frame2,
            text="Start",
            command=self.start
        )

        self.stop_button = tk.Button(
            self.frame2,
            text="Stop",
            command=self.stop
        )

        self.left_option = tk.Checkbutton(
            self.parent,
            text="Mouse1",
            command=self.set_left,
            state=tk.DISABLED
        )

        self.right_option = tk.Checkbutton(
            self.parent,
            text="Mouse2",
            command=self.set_right,
            state=tk.DISABLED
        )

        self.msg_label = tk.Label(
            self.parent,
            text="Press 'esc' button for quick and easy stoppage of program.",
            height=6,
            wraplength=100
        )

        #Element decoration
        self.start_button.config(height=5,width=10)
        self.stop_button.config(height=5, width=10)

        #Element placements
        self.label.grid(row=0, column=0)
        self.click_entry.grid(row=0,column=1)
        self.frame1.pack()

        self.start_button.grid(row=0,column=0,padx=10,pady=2)
        self.stop_button.grid(row=1,column=0,padx=10)
        self.frame2.pack(fill="both",side="left")

        self.left_option.pack(pady=2)
        self.right_option.pack()
        self.msg_label.pack(fill=tk.BOTH)

    def key_trace(self, *args):
        value = self.click_key.get()
        if len(value) > 1: #set charlimit to 1
            self.click_key.set(value[:1])

    def start(self): #start threads
        self.start_button.config(state=tk.DISABLED)

        #threads
        self.mouse_thread = clicker.Mouse(0.1, daemon=True)
        self.key_listener = clicker.keyboard.Listener(on_press=self.on_press, daemon=True)

        self.mouse_thread.start()
        self.key_listener.start()

        self.left_option.config(state=tk.NORMAL)
        self.right_option.config(state=tk.NORMAL)

    def stop(self): #stop threads
        self.start_button.config(state=tk.NORMAL)

        self.mouse_thread.stop()
        self.mouse_thread.join()

        self.key_listener.stop()
        self.key_listener.join()

        self.left_option.deselect()
        self.right_option.deselect()
        self.left_option.config(state=tk.DISABLED)
        self.right_option.config(state=tk.DISABLED)

    def on_press(self,key):
        print(key)
        if key == clicker.keyboard.Key.esc:
            self.stop()

        elif key == clicker.keyboard.KeyCode(char=self.click_key.get()):
            self.mouse_thread.toggle()

    def set_left(self):
        self.mouse_thread.mouse_change("mouse1")
        self.right_option.deselect()

    def set_right(self):
        self.mouse_thread.mouse_change("mouse2")
        self.left_option.deselect()