from tkinter import *


class Timer:
    def __init__(self, parent):
        self.container = Frame(parent)
        self.container.pack()

        self.bottom_container = Frame(parent)  # needed for vertical orientation of widgets
        self.bottom_container.pack(side=BOTTOM)

        self.minutes = 30
        self.seconds = 0

        self.label = Label(parent, text="{0:02}:{1:02}".format(self.minutes, self.seconds), font="Arial 30", width=10)
        # label is timer display
        self.label.pack(side=TOP)

        self.button1 = Button(self.bottom_container)
        self.button1["text"] = "Start"
        self.button1.pack(side=BOTTOM, fill=X)
        self.button1.focus_force()
        self.button1.bind("<Button-1>", self.button_1_click_1)
        self.button1.bind("<space>", self.button_1_click_1)  # requires fix

        self.button2 = Button(self.bottom_container)
        self.button2["text"] = "Reset"
        self.button2.pack(ipadx=7)
        self.button2.bind("<Button-1>", self.button_2_click)

    def button_1_click_1(self, event):
        self.button1["text"] = "Start"
        if self.button1["text"] == "Start":
            self.button1["text"] = "Pause"
            self.label.after(1000, self.refresh_label)
            self.button1.bind("<Button-1>", self.button_1_click_2)
        else:
            pass

    def button_1_click_2(self, event):
        self.button1.configure(text="Resume")
        self.button1.bind("<Button-1>", self.button_1_click_1)

    def button_2_click(self, event):
        self.label.configure(text="30:00".format(self.minutes, self.seconds))
        self.minutes = 30
        self.seconds = 0
        if self.button1["text"] == "Pause":
            pass
        else:
            self.button1.configure(text="Start")

    def refresh_label(self):
        if self.minutes == 0 and self.seconds == 0:
            self.label.configure(text="Time's up!")
        elif self.button1["text"] == "Resume":
            self.label.configure(text="{0:02}:{1:02}".format(self.minutes, self.seconds))
        else:
            self.seconds -= 1

            if self.seconds == -1:
                self.seconds = 59
                self.minutes -= 1
            self.label.configure(text="{0:02}:{1:02}".format(self.minutes, self.seconds))
            self.label.after(1000, self.refresh_label)


if __name__ == "__main__":
    root = Tk()
    timer = Timer(root)
    root.mainloop()
