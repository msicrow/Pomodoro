from datetime import *
from tkinter import *
import time


class Timer:
    def __init__(self, parent):
        self.time_start = datetime.now()
        self.time_end = self.time_start + timedelta(seconds=0) # Pomodoro technique typically 25 minute bursts
        self.time_delta = timedelta()

        self.active = False

        self.run_count = 0

        self.container = Frame(parent)
        self.container.pack()

        self.time_display = Label(parent, text="25:00")
        self.time_display.pack()

        self.time_state = Label(parent, text="Work")
        self.time_state.pack()

        self.start_button = Button(self.container)
        self.start_button["text"] = "Start"
        self.start_button.pack()
        self.start_button.focus_force()
        self.start_button.bind("<Button-1>", self.start_click)

        self.reset_button = Button(self.container)
        self.reset_button["text"] = "Reset"
        self.reset_button.pack()
        self.reset_button.bind("<Button-1>", self.reset_click)

    def countdown(self):
        if self.active:
            if datetime.now() >= self.time_end:
                self.break_time()
            elif self.start_button["text"] == "Resume":
                self.time_display.configure(text=self.time_display["text"])
                self.time_display.after(500, self.countdown)
            else:
                time_countdown = self.time_end - datetime.now()
                time_countdown = time_countdown.seconds
                minutes, seconds = divmod(time_countdown, 60)
                self.time_display.configure(text=("%02d:%02d" % (int(minutes), int(seconds))))
                self.time_display.after(500, self.countdown)

    def break_time(self):
        if self.run_count == 1:
            self.time_state["text"] = "Work"
            self.time_end = datetime.now() + timedelta(seconds=1500)
            self.time_display.after(500, self.countdown)
            self.run_count = 0
        else:
            self.time_state["text"] = "Break"
            self.time_end = datetime.now() + timedelta(seconds=300)
            self.run_count += 1
            self.time_display.after(500, self.countdown)

    def start_click(self, event):
        self.active = True
        self.time_end = datetime.now() + timedelta(seconds=1500)
        self.countdown()
        self.start_button["text"] = "Pause"
        self.start_button.bind("<Button-1>", self.pause_click)

    def pause_click(self, event):
        self.start_button["text"] = "Resume"
        self.start_button.bind("<Button-1>", self.resume_click)
        self.time_delta = self.time_end - datetime.now()   # difference between time now and start time

    def resume_click(self, event):
        self.active = True
        self.start_button["text"] = "Pause"
        self.start_button.bind("<Button-1>", self.pause_click)
        self.time_end = datetime.now() + self.time_delta   # adding difference to end time

    def reset_click(self, event):
        self.active = False
        self.time_display.configure(text="25:00")
        self.time_end = datetime.now() + timedelta(seconds=1500)
        self.start_button["text"] = "Start"
        self.start_button.bind("<Button-1>", self.start_click)


if __name__ == "__main__":
    root = Tk()
    root.attributes("-topmost", True)
    timer = Timer(root)
    root.mainloop()
