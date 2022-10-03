from tkinter import *
import threading
import time
TIME = 5


def handler_timer():
    global timer
    while timer >= 0:
        time_label.config(text=f"{timer} sec")
        timer -= 1
        time.sleep(1)
    text.delete('1.0', END)
    text.config(state='disabled')


def try_again():
    global timer, timer_sec
    text.delete('1.0', END)
    text.config(state='normal')
    timer = TIME
    if not timer_sec.is_alive():
        timer_sec = threading.Thread(target=handler_timer, name='timer')
        timer_sec.start()


def click(key):
    global timer
    timer = TIME

    
# Create the window
window = Tk()
window.title("Disappearing Text Writing App")
window.minsize(width=100, height=100)
window.config(padx=10, pady=10)
# Create labels
time_label = Label(text=f"{TIME} sec", width=20)
time_label.grid(column=2, row=1)
# Create text box for writing.
text = Text(window, height=3, width=32, takefocus=True, font='Arial, 18', wrap=WORD)
text.grid(column=1, row=2, columnspan=3, pady=5)
text.focus()
# bing key event to text box.
text.bind('<KeyPress>', click)
# Create button
button = Button(window, text="Try Again", command=try_again)
button.grid(column=2, row=3, pady=10)
end_btn = Button(window, text=" EXIT ", command=lambda: window.destroy())
end_btn.grid(column=3, row=3, pady=10)
# Start timer thread
timer = TIME
timer_sec = threading.Thread(target=handler_timer, name='timer')
timer_sec.start()


# Must put at the end
window.mainloop()





