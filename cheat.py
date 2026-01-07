import tkinter as tk
import json, os, sys, random

# ================= SAFE DISCLAIMER =================
# UI ONLY - D3D STYLE SIMULATION
# NO INJECT - NO MEMORY - NO GAME ACCESS

# ================= CONFIG =================
APP = "Mr.Rm19 • Point Blank D3D Menu VVIP"
W, H = 760, 420
KEY_VVIP = "RAMDAN-LOVE-NEILLA"
CONF = "d3d_vvip.json"

# ================= THEMES =================
THEMES = {
    "BLUE":  {"bg":"#050b18","panel":"#0b1530","neon":"#00f6ff","text":"#cfe6ff"},
    "RED":   {"bg":"#120507","panel":"#2a0b10","neon":"#ff3b3b","text":"#ffd6d6"},
    "GREEN": {"bg":"#05120b","panel":"#0b2a1a","neon":"#2dff9a","text":"#d6ffef"},
}

FEATURES = [
    "Wall Hack",
    "ESP Box",
    "ESP Name",
    "No Recoil",
    "Rapid Fire",
    "Fast Reload",
    "One Hit",
    "Anti Kick"
]

ABOUT = "Mr.Rm19\nramdan19id@gmail.com\nD3D STYLE UI ONLY"

# ================= LOAD / SAVE =================
def load():
    if os.path.exists(CONF):
        try: return json.load(open(CONF))
        except: pass
    return {}

def save(d):
    json.dump(d, open(CONF,"w"), indent=2)

cfg = load()
theme_name = cfg.get("theme","BLUE")
THEME = THEMES[theme_name]

# ================= ROOT =================
root = tk.Tk()
root.title(APP)
root.geometry(f"{W}x{H}")
root.configure(bg=THEME["bg"])
root.attributes("-topmost", True)
root.overrideredirect(True)
root.attributes("-alpha", 0.92)

# ================= TITLE BAR =================
title = tk.Frame(root, bg=THEME["panel"], height=34)
title.pack(fill="x")

tk.Label(title, text=APP,
         fg=THEME["neon"], bg=THEME["panel"],
         font=("Consolas", 11, "bold")
).pack(side="left", padx=10)

# drag window
def drag(e):
    root.geometry(f"+{e.x_root}+{e.y_root}")
title.bind("<B1-Motion>", drag)

# ================= MAIN =================
main = tk.Frame(root, bg=THEME["bg"])
main.pack(fill="both", expand=True, padx=8, pady=6)

left = tk.Frame(main, bg=THEME["panel"], width=340)
left.pack(side="left", fill="y", padx=(0,6))

right = tk.Frame(main, bg=THEME["panel"])
right.pack(side="right", fill="both", expand=True)

# ================= LOGIN =================
login = tk.Frame(left, bg=THEME["panel"])
login.pack(fill="both", expand=True)

tk.Label(login, text="VVIP LOGIN",
         fg=THEME["neon"], bg=THEME["panel"],
         font=("Consolas", 14, "bold")
).pack(pady=18)

key = tk.Entry(login, bg="#000000", fg=THEME["neon"],
               insertbackground=THEME["neon"],
               font=("Consolas", 11), relief="flat")
key.pack(padx=20, pady=8, fill="x")
key.insert(0, cfg.get("key",""))

def do_login():
    if key.get() == KEY_VVIP:
        cfg["key"] = KEY_VVIP
        save(cfg)
        login.pack_forget()
        build_menu()
    else:
        key.delete(0,"end")

tk.Button(login, text="LOGIN",
          command=do_login,
          bg=THEME["neon"], fg="#000",
          font=("Consolas", 10, "bold"),
          relief="flat").pack(pady=10)

# ================= MENU =================
def build_menu():
    tk.Label(left, text="CHEAT MENU",
             fg=THEME["neon"], bg=THEME["panel"],
             font=("Consolas", 13, "bold")
    ).pack(anchor="w", padx=12, pady=10)

    states = {}
    saved = cfg.get("features",{})

    for f in FEATURES:
        row = tk.Frame(left, bg=THEME["panel"])
        row.pack(fill="x", padx=12, pady=3)

        tk.Label(row, text=f,
                 fg=THEME["text"], bg=THEME["panel"],
                 font=("Consolas", 10)
        ).pack(side="left")

        v = tk.BooleanVar(value=saved.get(f,False))
        states[f] = v

        tk.Checkbutton(row, text="ON",
                       variable=v,
                       fg=THEME["neon"], bg=THEME["panel"],
                       selectcolor=THEME["panel"],
                       activebackground=THEME["panel"],
                       font=("Consolas", 9)
        ).pack(side="right")

    def save_feat():
        cfg["features"] = {k:v.get() for k,v in states.items()}
        save(cfg)

    # ================= RIGHT PANEL =================
    tk.Label(right, text="STATUS",
             fg=THEME["neon"], bg=THEME["panel"],
             font=("Consolas", 13, "bold")
    ).pack(anchor="w", padx=12, pady=10)

    status = tk.Label(right, text="CONNECTED",
                      fg="#00ff99", bg=THEME["panel"],
                      font=("Consolas", 11))
    status.pack(anchor="w", padx=14)

    ping = tk.Label(right, text="PING: -- ms",
                    fg=THEME["text"], bg=THEME["panel"],
                    font=("Consolas", 10))
    ping.pack(anchor="w", padx=14, pady=4)

    def fake_ping():
        ping.config(text=f"PING: {random.randint(20,60)} ms")
        root.after(1000, fake_ping)
    fake_ping()

    tk.Label(right, text="\nHOTKEYS\n"
                          "F6 BLUE\nF7 RED\nF8 GREEN\n"
                          "F2 PANIC\nF12 EXIT",
             fg=THEME["text"], bg=THEME["panel"],
             font=("Consolas", 10), justify="left"
    ).pack(anchor="w", padx=14, pady=10)

    tk.Label(right, text=ABOUT,
             fg=THEME["neon"], bg=THEME["panel"],
             font=("Consolas", 10)
    ).pack(side="bottom", pady=10)

    # ================= HOTKEY =================
    def panic(e=None):
        for v in states.values(): v.set(False)
        save_feat()
        status.config(text="PANIC", fg=THEME["neon"])
        root.after(600, lambda: status.config(text="CONNECTED", fg="#00ff99"))

    def theme_switch(name):
        cfg["theme"] = name
        save(cfg)
        os.execl(sys.executable, sys.executable, *sys.argv)

    root.bind("<F2>", panic)
    root.bind("<F6>", lambda e: theme_switch("BLUE"))
    root.bind("<F7>", lambda e: theme_switch("RED"))
    root.bind("<F8>", lambda e: theme_switch("GREEN"))
    root.bind("<F12>", lambda e: root.destroy())

# ================= START =================
root.mainloop()
