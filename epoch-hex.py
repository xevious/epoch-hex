#!/opt/homebrew/bin/python3
import time
import tkinter as tk

END_EPOCH = 2147483647

def update_display():
    now = int(time.time())
    wrapped_now = now % (2**31)
    hex_value = f"0x{wrapped_now:08x}"
    percent = min(wrapped_now / END_EPOCH, 1.0)
    percent_width = int(progress_width * percent)

    label.config(text=hex_value)

    # Clear canvas
    canvas.delete("all")

    # Draw progress bar
    canvas.create_rectangle(0, 0, percent_width, progress_height, fill="lime", width=0)  # elapsed
    canvas.create_rectangle(percent_width, 0, progress_width, progress_height, fill="#006400", width=0)  # remaining

    # Draw decade tick marks (1970–2030)
    for ts in [315532800, 631152000, 946684800, 1262304000, 1577836800, 1893456000]:
        tick_x = int((ts / END_EPOCH) * progress_width)
        canvas.create_line(tick_x, 0, tick_x, progress_height, fill="gray", width=1)

    root.after(1000, update_display)

root = tk.Tk()
root.title("Current Epoch Time")
root.configure(bg="black")
root.geometry("400x140")
root.resizable(False, False)

# Hex label
label = tk.Label(
    root,
    text="",
    font=("Courier", 32),
    fg="lime",
    bg="black"
)
label.pack(pady=(10, 0))

# Progress bar canvas
progress_width = 360
progress_height = 20
canvas = tk.Canvas(root, width=progress_width, height=progress_height, highlightthickness=0, bg="black")
canvas.pack(pady=(10, 0))

update_display()
root.mainloop()