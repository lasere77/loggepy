from tkinter import *


def test():
    print('test')

class Gui:
    def __init__(self):
        pass

    def windows(self, tilte, size, label, rule, button, entry, fonction):
        windows = Tk()
        windows.title(tilte)
        windows.iconbitmap("img/index.ico")
        windows.config(bg="gray17")
        windows.geometry(size)

        frame = Frame(windows, bg="gray17")
        frame.pack(expand="YES")

        rule = Label(frame, text=rule, bg="gray17", fg="#083def")
        rule.pack()

        windows.mainloop()

gui = Gui()
gui.windows("test", "1080x600", "label", "rule", "btn", "entry", test)

test = Gui()
test.windows("ma lubullule", "150x600", "label", "rule34", "btn", "entry", test)