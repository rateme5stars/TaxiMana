from tkinter import *
from tkmacosx import Button
from tkinter import messagebox
from taximana.constant import *

class LoginController:
    def load_view(self):
        self.login_window = Tk()
        self.login_window.title("Taxi Management")
        self.login_window.geometry('1100x600')
        self.login_window.configure(bg=LOGIN_COLOR)
        self.login_window.resizable(False, False)

        img = PhotoImage(file='taximana/asset/logo.png')
        Label(self.login_window, image=img, bg=LOGIN_COLOR).place(x=50, y=50)

        login_frame = Frame(self.login_window, width=400, height=400, bg=LOGIN_COLOR)
        login_frame.place(x=600, y=70)

        # Heading
        heading = Label(login_frame, text="Sign In", fg='black', bg=LOGIN_COLOR, font=(FONT, 32))
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
        self.password_entry.place(x=90, y=130)
        self.password_entry.insert(0, ' Password')
        self.password_entry.bind('<FocusIn>', self.on_enter_password)
        self.password_entry.bind('<FocusOut>', self.on_leave_password)

        # Line
        Frame(login_frame,width=300, height=1, bg='black').place(x=92, y=158)

        # Login Button 
        login_bt = Button(login_frame, width=200, pady=6, text='Sign In',fg='black', bg="white", borderless=1, command=self.sign_in)
        login_bt.place(x=140, y=200)

        lb = Label(login_frame, text="Don't have an account?", fg='black', bg=LOGIN_COLOR, font=(FONT, 15, 'normal'))
        lb.place(x=100, y=260)

        # Sign up button
        sign_up = Button(login_frame, width=55, text='Sign Up', bg=LOGIN_COLOR, cursor='hand2', fg='black', borderwidth=0, border=0, borderless=1)
        sign_up.place(x=280, y=260)

        self.login_window.mainloop()

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
            self.password_entry.insert(0, 'Password')
    
    # Handle sign in event
    def sign_in(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if username == 'admin' and password == '1234':
            self.login_window.destroy()
            # root = Toplevel(self.login_window)
            root = Tk()
            root.title('Taxi Management')
            root.geometry('1440x1024')
            root.config(bg='white')
            Label(root, text='Hello Mother Fucker', bg='#fff', font=('Calibri(Body)', 50, 'bold')).pack(expand=True)
            
            root.mainloop()
            
        elif username != 'admin' or password != '1234':
            messagebox.showerror('Invalid', 'Something is wrong')
            
if __name__ == "__main__":
    login = LoginController()
    login.load_view()
    
