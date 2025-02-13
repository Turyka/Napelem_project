import tkinter as tk
from tkinter import messagebox
import requests

API_URL = "http://your-laravel-api.com/api/login"

# Function to handle login request
def login():
    username = entry_username.get()
    password = entry_password.get()

    if not username or not password:
        messagebox.showerror("Login Failed", "Please enter both username and password")
        return

    # Send login request to Laravel API
    response = requests.post(API_URL, json={"name": username, "password": password})

    if response.status_code == 200:
        data = response.json()
        auth_token = data["token"]
        messagebox.showinfo("Login Success", "Welcome, " + username + "!")

        # Store token for future requests
        with open("token.txt", "w") as token_file:
            token_file.write(auth_token)
        
    else:
        messagebox.showerror("Login Failed", response.json().get("message", "Invalid credentials"))

# Create main window
root = tk.Tk()
root.title("Login Page")
root.geometry("400x300")
root.configure(bg="#2C3E50")

# Frame for login form
frame = tk.Frame(root, bg="#34495E", padx=20, pady=20)
frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

# Username label and entry
label_username = tk.Label(frame, text="Username", bg="#34495E", fg="white", font=("Arial", 12))
label_username.grid(row=0, column=0, sticky="w", pady=5)
entry_username = tk.Entry(frame, font=("Arial", 12), width=25)
entry_username.grid(row=1, column=0, pady=5)

# Password label and entry
label_password = tk.Label(frame, text="Password", bg="#34495E", fg="white", font=("Arial", 12))
label_password.grid(row=2, column=0, sticky="w", pady=5)
entry_password = tk.Entry(frame, font=("Arial", 12), width=25, show="*")
entry_password.grid(row=3, column=0, pady=5)

# Login button with hover effect
def on_enter(e):
    btn_login["bg"] = "#1ABC9C"

def on_leave(e):
    btn_login["bg"] = "#16A085"

btn_login = tk.Button(frame, text="Login", font=("Arial", 12, "bold"), bg="#16A085", fg="white", padx=10, pady=5, command=login)
btn_login.grid(row=4, column=0, pady=15)
btn_login.bind("<Enter>", on_enter)
btn_login.bind("<Leave>", on_leave)

root.mainloop()