from commons import ui

def run():
    root = ui.tk.Tk()
    root.title("Clicker")
    root.minsize(width=210,height=200)
    root.maxsize(width=210,height=200)
    ui.MainApplication(root).pack()
    root.mainloop()