
#!/usr/bin/env python3
import tkinter as tk
import subprocess

def close_youtube():
    subprocess.run(["/home/mks/scripts/stop_youtube.sh"])
def open_keyboard():
    subprocess.Popen(["onboard"])

root = tk.Tk()
root.overrideredirect(True)          # keine Fensterdekoration
root.attributes("-topmost", True)
root.geometry("480x50+0+30")          # X/Y-Position anpassen, z.B. Ecke wo Tou$
root.configure(bg="black")


btn_kbd = tk.Button(root, text="⌨", command=open_keyboard,
                     bg="gray20", fg="white", font=("Arial", 14), borderwidth=0)

btn_kbd.pack(side="left", fill="both", expand=True)


btn_close = tk.Button(root, text="✕", command=close_youtube,
                       bg="red", fg="white", font=("Arial", 14), borderwidth=0)

btn_close.pack(side="left", fill="both", expand=True)

# Wichtig: sich selbst regelmäßig nach vorne holen, falls Chromium
# versucht, sich draufzulegen
def keep_on_top():
    root.lift()
    root.attributes("-topmost", True)
    root.after(500, keep_on_top)

keep_on_top()
root.mainloop()