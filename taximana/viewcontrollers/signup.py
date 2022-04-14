from tkinter import *
from tkmacosx import Button
from tkinter import messagebox
from taximana.constant import *
from pathlib import Path

class SignUpController:
    def load_view(self):
        self.signup_window = Tk()
        self.signup_window.title("Taxi Management")
        self.signup_window.geometry('1100x600')
        self.signup_window.configure(bg=LOGIN_COLOR)
        self.signup_window.resizable(False, False)

        img = PhotoImage(file='taximana/asset/logo.png')
        Label(self.signup_window, image=img, bg=LOGIN_COLOR).place(x=50, y=50)

        login_frame = Frame(self.signup_window, width=400, height=400, bg=LOGIN_COLOR)
        login_frame.place(x=600, y=70)

        # Heading
        heading = Label(login_frame, text="Sign Up", fg='black', bg=LOGIN_COLOR, font=(FONT, 32))
        heading.place(x=185, y=5)
        
        # Username Entry
        self.username_entry = Entry(login_frame, highlightthickness=3, border=0, width=30, fg='black', bg=LOGIN_COLOR, font=(FONT, 15))
        self.username_entry.config(highlightbackground=LOGIN_COLOR, highlightcolor=LOGIN_COLOR)
        self.username_entry.place(x=90, y=80)
        self.username_entry.insert(0, ' Username')
        self.username_entry.bind('<FocusIn>', self.on_enter_username)
        self.username_entry.bind('<FocusOut>', self.on_leave_username)

        # Line
        Frame(login_frame,width=300, height=1, bg='black').place(x=92, y=108)

        # Password Entry
        self.password_entry = Entry(login_frame, highlightthickness=3, border=0, width=30, fg='black', bg=LOGIN_COLOR, font=(FONT, 15))
        self.password_entry.config(highlightbackground=LOGIN_COLOR, highlightcolor=LOGIN_COLOR)
        self.password_entry.configure(show="*")
        self.password_entry.place(x=90, y=130)
        self.password_entry.insert(0, '***')
        self.password_entry.bind('<FocusIn>', self.on_enter_password)
        self.password_entry.bind('<FocusOut>', self.on_leave_password)

        # Line
        Frame(login_frame,width=300, height=1, bg='black').place(x=92, y=158)

        # Confirm Password Entry
        self.confirm_entry = Entry(login_frame, highlightthickness=3, border=0, width=30, fg='black', bg=LOGIN_COLOR, font=(FONT, 15))
        self.confirm_entry.config(highlightbackground=LOGIN_COLOR, highlightcolor=LOGIN_COLOR)
        self.confirm_entry.configure(show="*")
        self.confirm_entry.place(x=90, y=180)
        self.confirm_entry.insert(0, '***')
        self.confirm_entry.bind('<FocusIn>', self.on_enter_confirm)
        self.confirm_entry.bind('<FocusOut>', self.on_leave_confirm)

        # Line
        Frame(login_frame,width=300, height=1, bg='black').place(x=92, y=208)

        Checkbutton(login_frame, text="Show password", bg=LOGIN_COLOR, command=self.show_password).place(x=85, y=230)

        # Sign Up Button 
        login_bt = Button(login_frame, width=200, pady=6, text='Sign Up',fg='black', bg="white", borderless=1, command=self.sign_up)
        login_bt.place(x=140, y=270)

        lb = Label(login_frame, text="Already have an account?", fg='black', bg=LOGIN_COLOR, font=(FONT, 15, 'normal'))
        lb.place(x=100, y=320)

        # Sign up button
        sign_up = Button(login_frame, width=55, text='Sign In', bg=LOGIN_COLOR, cursor='hand2', fg='black', borderwidth=0, border=0, borderless=1)
        sign_up.place(x=280, y=320)

        self.signup_window.mainloop()

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
        for user_password in data_file:
            user_password = eval(user_password)
            for existing_username, _ in user_password.items():
                existing_username_list.append(existing_username)
                if username in existing_username_list:
                    return True
                else:
                    return False

if __name__ == "__main__":
    signup = SignUpController()
    signup.load_view()