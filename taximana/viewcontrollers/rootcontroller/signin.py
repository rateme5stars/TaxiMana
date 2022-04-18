import tkinter as tk
from tkmacosx import Button
from tkinter import messagebox
from taximana.constant import *
from pathlib import Path

class SignInController(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg=LOGIN_COLOR)
        self.controller = controller
        self.controller.title("Sign In")

        img = tk.PhotoImage(file='taximana/asset/logo.png')
        logo = tk.Label(self, image=img, bg=LOGIN_COLOR)
        logo.place(x=50, y=50)
        logo.image = img

        login_frame = tk.Frame(self, width=400, height=400, bg=LOGIN_COLOR)
        login_frame.place(x=600, y=70)

        # Heading
        heading = tk.Label(login_frame, text="Sign In", fg='black', bg=LOGIN_COLOR, font=(FONT, 32))
        heading.place(x=185, y=5)
        
        # Username Entry
        self.username_entry = tk.Entry(login_frame, highlightthickness=3, border=0, width=30, fg='black', bg=LOGIN_COLOR, font=(FONT, 15))
        self.username_entry.config(highlightbackground=LOGIN_COLOR, highlightcolor=LOGIN_COLOR)
        self.username_entry.place(x=90, y=80)
        self.username_entry.insert(0, ' Username')
        self.username_entry.bind('<FocusIn>', self.on_enter_username)
        self.username_entry.bind('<FocusOut>', self.on_leave_username)

        # Line
        tk.Frame(login_frame,width=300, height=1, bg='black').place(x=92, y=108)

        # Password Entry
        self.password_entry = tk.Entry(login_frame, highlightthickness=3, border=0, width=30, fg='black', bg=LOGIN_COLOR, font=(FONT, 15))
        self.password_entry.config(highlightbackground=LOGIN_COLOR, highlightcolor=LOGIN_COLOR)
        self.password_entry.configure(show="*")
        self.password_entry.place(x=90, y=130)
        self.password_entry.insert(0, '***')
        self.password_entry.bind('<FocusIn>', self.on_enter_password)
        self.password_entry.bind('<FocusOut>', self.on_leave_password)

        # Line
        tk.Frame(login_frame,width=300, height=1, bg='black').place(x=92, y=158)

        # Show password Button
        tk.Checkbutton(login_frame, text="Show password", bg=LOGIN_COLOR, command=self.show_password).place(x=85, y=180)

        # Login Button 
        login_bt = Button(login_frame, width=200, pady=6, text='Sign In',fg='black', bg="white", borderless=1, command=self.sign_in)
        login_bt.place(x=140, y=220)

        lb = tk.Label(login_frame, text="Don't have an account?", fg='black', bg=LOGIN_COLOR, font=(FONT, 15, 'normal'))
        lb.place(x=100, y=280)

        # Sign up button
        sign_up = Button(login_frame, width=55, text='Sign Up', cursor='hand2', fg='black', borderwidth=0, border=0, borderless=1, bg=LOGIN_COLOR,
        command=lambda: controller.show_frame('SignUpController'))
        sign_up.place(x=280, y=280)
    
    # Handle click on entry events
    def on_enter_username(self, *arg):
        self.username_entry.delete(0, 'end')

    def on_leave_username(self, *arg):
        name = self.username_entry.get()
        if name == '':
            self.username_entry.insert(0, 'Username')
    
    def on_enter_password(self, *arg):
        self.password_entry.delete(0, 'end')

    def on_leave_password(self, *arg):
        name = self.password_entry.get()
        if name == '':
            self.password_entry.insert(0, '***')
    
    def show_password(self):
        if self.password_entry.cget('show') == "*":
            self.password_entry.configure(show="")
        else:
            self.password_entry.configure(show="*")

    # Handle sign in event
    def sign_in(self):
        username = self.username_entry.get().strip()
        password = self.password_entry.get().strip()
        user_password = {f'{username}':f'{password}'}
        if Path(DATA_PATH).is_file():
            if user_password in self.check_existence():
                main = tk.Tk()
                main.title('Taxi Management')
                main.geometry('1440x1024')
                main.config(bg='white')
                tk.Label(main, text='Hello Mother Fucker', bg='#fff', font=('Calibri(Body)', 50, 'bold')).pack(expand=True)
                
                main.mainloop()
            else:
                messagebox.showerror('Invalid', 'Something is wrong')
        else:
            messagebox.showerror('Invalid', 'Something is wrong')

    def check_existence(self): 
        user_password_list = list()
        data_file = open(DATA_PATH, 'r')
        for user_password in data_file:
            user_password = eval(user_password)
            user_password_list.append(user_password)
        
        return user_password_list
    
