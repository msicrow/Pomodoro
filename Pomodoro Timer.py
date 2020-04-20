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

        self.start_button = Button(self.bottom_container)
        self.start_button["text"] = "Start"
        self.start_button.pack(side=BOTTOM, fill=X)
        self.start_button.focus_force()
        self.start_button.bind("<Button-1>", self.button_1_click_1)
        self.start_button.bind("<space>", self.button_1_click_1)  # requires fix

        self.reset_button = Button(self.bottom_container)
        self.reset_button["text"] = "Reset"
        self.reset_button.pack(ipadx=7)
        self.reset_button.bind("<Button-1>", self.button_2_click)

        self.add_button = Button(self.bottom_container)
        self.add_button["text"] = "+"
        self.add_button.pack()
        self.add_button.bind("<Button-1>", self.button_3_click)

    def button_1_click_1(self, event):
        self.start_button["text"] = "Start"
        if self.start_button["text"] == "Start":
            self.start_button["text"] = "Pause"
            self.label.after(1000, self.refresh_label)
            self.start_button.bind("<Button-1>", self.button_1_click_2)
        else:
            pass

    def button_1_click_2(self, event):
        self.start_button.configure(text="Resume")
        self.start_button.bind("<Button-1>", self.button_1_click_1)

    def button_2_click(self, event):
        self.label.configure(text="30:00".format(self.minutes, self.seconds))
        self.minutes = 30
        self.seconds = 0
        if self.start_button["text"] == "Pause":
            pass
        else:
            self.start_button.configure(text="Start")

    def button_3_click(self, event):
        self.minutes += 1
        self.label.after(100, self.refresh_label)

    def refresh_label(self):
        if self.minutes == 0 and self.seconds == 0:
            self.label.configure(text="Time's up!")
        elif self.start_button["text"] == "Resume":
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
