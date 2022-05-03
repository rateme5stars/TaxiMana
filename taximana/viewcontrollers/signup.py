import tkinter as tk
from tkmacosx import Button
from tkinter import messagebox
from taximana.constant import *
from pathlib import Path
import os

class SignUpController(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg=LOGIN_COLOR)
        self.controller = controller
        self.controller.title("Sign In")

        img = tk.PhotoImage(file='taximana/asset/logo.png')
        logo = tk.Label(self, image=img, bg=LOGIN_COLOR)
        logo.place(x=50, y=150)
        logo.image = img

        signup = tk.Frame(self, width=400, height=400, bg=LOGIN_COLOR)
        signup.place(x=600, y=120)

        # Heading
        heading = tk.Label(signup, text="Sign Up", fg='black', bg=LOGIN_COLOR, font=(FONT, 32))
        heading.place(x=185, y=85)
        
        # Username Entry
        self.username_entry = tk.Entry(signup, highlightthickness=3, border=0, width=30, fg='black', bg=LOGIN_COLOR, font=(FONT, 15))
        self.username_entry.config(highlightbackground=LOGIN_COLOR, highlightcolor=LOGIN_COLOR)
        self.username_entry.place(x=90, y=130)
        self.username_entry.insert(0, ' Username')
        self.username_entry.bind('<FocusIn>', self.on_enter_username)
        self.username_entry.bind('<FocusOut>', self.on_leave_username)

        # Line
        tk.Frame(signup,width=300, height=1, bg='black').place(x=92, y=158)

        # Password Entry
        self.password_entry = tk.Entry(signup, highlightthickness=3, border=0, width=30, fg='black', bg=LOGIN_COLOR, font=(FONT, 15))
        self.password_entry.config(highlightbackground=LOGIN_COLOR, highlightcolor=LOGIN_COLOR)
        self.password_entry.configure(show="*")
        self.password_entry.place(x=90, y=180)
        self.password_entry.insert(0, '***')
        self.password_entry.bind('<FocusIn>', self.on_enter_password)
        self.password_entry.bind('<FocusOut>', self.on_leave_password)

        # Line
        tk.Frame(signup,width=300, height=1, bg='black').place(x=92, y=208)

        # Confirm Password Entry
        self.confirm_entry = tk.Entry(signup, highlightthickness=3, border=0, width=30, fg='black', bg=LOGIN_COLOR, font=(FONT, 15))
        self.confirm_entry.config(highlightbackground=LOGIN_COLOR, highlightcolor=LOGIN_COLOR)
        self.confirm_entry.configure(show="*")
        self.confirm_entry.place(x=90, y=230)
        self.confirm_entry.insert(0, '***')
        self.confirm_entry.bind('<FocusIn>', self.on_enter_confirm)
        self.confirm_entry.bind('<FocusOut>', self.on_leave_confirm)

        # Line
        tk.Frame(signup,width=300, height=1, bg='black').place(x=92, y=258)

        tk.Checkbutton(signup, text="Show password", bg=LOGIN_COLOR, command=self.show_password).place(x=85, y=280)

        # Sign Up Button 
        login_bt = Button(signup, width=200, pady=6, text='Sign Up',fg='black', bg="white", borderless=1, command=self.sign_up)
        login_bt.place(x=140, y=320)

        lb = tk.Label(signup, text="Already have an account?", fg='black', bg=LOGIN_COLOR, font=(FONT, 15, 'normal'))
        lb.place(x=100, y=370)

        # Sign In button
        sign_up = Button(signup, width=55, text='Sign In', bg=LOGIN_COLOR, cursor='hand2', fg='black', borderwidth=0, border=0, borderless=1, command=lambda: controller.show_frame('SignInController'))
        sign_up.place(x=280, y=370)

    

    # Handle click on entry events
    def on_enter_username(self, *arg):
        self.username_entry.delete(0, 'end')

    def on_leave_username(self, *arg):
        name = self.username_entry.get()
        if name == '':
            self.username_entry.insert(0, ' Username')
    
    def on_enter_password(self, *arg):
        self.password_entry.delete(0, 'end')

    def on_leave_password(self, *arg):
        name = self.password_entry.get()
        if name == '':
            self.password_entry.insert(0, '***')
    
    def on_enter_confirm(self, *arg):
        self.confirm_entry.delete(0, 'end')

    def on_leave_confirm(self, *arg):
        name = self.confirm_entry.get()
        if name == '':
            self.confirm_entry.insert(0, '***')
    
    def show_password(self):
        if self.password_entry.cget('show') == "*" or self.confirm_entry.cget('show') == "*":
            self.password_entry.configure(show="")
            self.confirm_entry.configure(show="")
        else:
            self.password_entry.configure(show="*")
            self.confirm_entry.configure(show="*")
    
    # Handle sign in event
    def sign_up(self):
        username = self.username_entry.get().strip()
        password = self.password_entry.get().strip()
        confirm = self.confirm_entry.get().strip()
        user_password = {username:password}

        if password == confirm:
            if Path(DATA_PATH).is_file():
                if self.check_existence(username=username):
                    messagebox.showerror('Invalid','Username already exist')
                else:
                    file = open(DATA_PATH, 'a')
                    file.write(f'{user_password}\n')
                    file.close()
                    messagebox.showinfo('Sign Up', 'Successfully sign up')
            else:
                file = open(DATA_PATH, 'w')
                file.write(f'{user_password}\n')
                file.close()
                messagebox.showinfo('Sign Up', 'Successfully sign up')

    def check_existence(self, username):
        existing_username_list = list()
        data_file = open(DATA_PATH, 'r')
        if os.path.getsize(DATA_PATH) != 0:
            for login_info in data_file:
                login_json = eval(login_info)
                for existing_username, _ in login_json.items():
                    existing_username_list.append(existing_username)
            if username in existing_username_list:
                return True
            else:
                return False
        elif os.path.getsize(DATA_PATH) == 0: 
            return False