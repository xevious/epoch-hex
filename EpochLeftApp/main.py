import time
import tkinter as tk

END_EPOCH = 2147483647

def update_timer():
    now = int(time.time())
    remaining = END_EPOCH - now
    hex_value = hex(remaining)
    label.config(text=hex_value)
    root.after(1000, update_timer)

root = tk.Tk()
root.title("End of Epoch")
root.geometry("400x100")
root.configure(bg="black")

label = tk.Label(
    root,
    text="",
    font=("Courier", 32),
    fg="lime",
    bg="black"
)
label.pack(expand=True)

update_timer()

# REQUIRED for py2app to run correctly
if __name__ == "__main__":
    root.mainloop()