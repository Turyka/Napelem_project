import tkinter as tk
from tkinter import messagebox
import API_register

# Colors & Styles
BG_COLOR = "#1E1E1E"  # Dark background
FRAME_COLOR = "#2A2A2A"  # Slightly lighter dark
TEXT_COLOR = "#FFFFFF"  # White text
BUTTON_COLOR = "#3B82F6"  # Blue button
BUTTON_HOVER = "#2563EB"  # Darker blue on hover
ENTRY_BG = "#333333"  # Darker entry field
ENTRY_FG = "#FFFFFF"  # White text in entry

# Function to handle login
def registraction():
    username = entry_username.get()
    password = entry_password.get()

    token, error = API_register.register_to_laravel_api(username, password)

    if token:
        messagebox.showinfo("sikeres felvétel", f"sikeres felvétel\n token: {token}")
    else:
        messagebox.showerror("Helytelef felvétel", error)

# Create main window
root = tk.Tk()
root.title("Regisztáció")
root.geometry("400x400")
root.configure(bg=BG_COLOR)

# Frame for login form
frame = tk.Frame(root, bg=FRAME_COLOR, padx=20, pady=20, bd=2, relief="ridge")
frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

# Username label & entry
label_username = tk.Label(frame, text="Username", bg=FRAME_COLOR, fg=TEXT_COLOR, font=("Arial", 12, "bold"))
label_username.grid(row=0, column=0, sticky="w", pady=5)
entry_username = tk.Entry(frame, font=("Arial", 12), width=30, bg=ENTRY_BG, fg=ENTRY_FG, insertbackground="white", relief="flat")
entry_username.grid(row=1, column=0, pady=5)

# Password label & entry
label_password = tk.Label(frame, text="Password", bg=FRAME_COLOR, fg=TEXT_COLOR, font=("Arial", 12, "bold"))
label_password.grid(row=2, column=0, sticky="w", pady=5)
entry_password = tk.Entry(frame, font=("Arial", 12), width=30, bg=ENTRY_BG, fg=ENTRY_FG, insertbackground="white", relief="flat", show="*")
entry_password.grid(row=3, column=0, pady=5)

# Hover effects for button
def on_enter(e):
    btn_login["bg"] = BUTTON_HOVER

def on_leave(e):
    btn_login["bg"] = BUTTON_COLOR

# Login Button
btn_login = tk.Button(frame, text="Registráció", font=("Arial", 12, "bold"), bg=BUTTON_COLOR, fg="white",
                      padx=10, pady=5, width=15, borderwidth=0, relief="flat", command=registraction)
btn_login.grid(row=4, column=0, pady=15)
btn_login.bind("<Enter>", on_enter)
btn_login.bind("<Leave>", on_leave)

root.mainloop()
