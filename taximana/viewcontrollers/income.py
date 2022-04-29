import tkinter as tk
from taximana.constant import *
from tkmacosx import Button
from datetime import date


class Income(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='white')
        self.controller = controller
        self.controller.title("Income")

        # Navigation Bar
        navigation_frame = tk.Frame(self, width=265, height=850, bg=NAVIBAR_COLOR)
        navigation_frame.place(x=0, y=0)
        
        # Username
        username_frame = tk.Frame(navigation_frame, width=265, height=50, bg=NAVIBAR_COLOR)
        username_frame.place(x=0, y=0)
        username_label = tk.Label(username_frame, bg=NAVIBAR_COLOR, text='Username', fg='white', font=(FONT, 20))
        username_label.place(relx=.5, rely=.5,anchor= tk.CENTER)

        # Information Label
        tk.Label(navigation_frame, bg=NAVIBAR_COLOR, text='Information', fg='#FFFFFF', font=(FONT, 15)).place(x=20, y=90)

        # DashBoard
        img = tk.PhotoImage(file='taximana/asset/dashboard.png')
        logo = tk.Label(self, image=img, bg=NAVIBAR_COLOR, width=10, height=10)
        logo.place(x=70, y=185)
        logo.image = img
        dashboard = tk.Label(navigation_frame, bg=NAVIBAR_COLOR, text='Dashboard', fg='white')
        dashboard.place(x=100, y=180)

        # Driver
        img = tk.PhotoImage(file='taximana/asset/staff.png')
        logo = tk.Label(self, image=img, bg=NAVIBAR_COLOR, width=10, height=10)
        logo.place(x=70, y=255)
        logo.image = img
        driver = tk.Label(navigation_frame, bg=NAVIBAR_COLOR, text='Driver', fg='white')
        driver.place(x=100, y=250)

        # Car
        img = tk.PhotoImage(file='taximana/asset/car.png')
        logo = tk.Label(self, image=img, bg=NAVIBAR_COLOR, width=10, height=10)
        logo.place(x=70, y=325)
        logo.image = img
        car = tk.Label(navigation_frame, bg=NAVIBAR_COLOR, text='Car', fg='white')
        car.place(x=100, y=320)

        # Report
        tk.Label(navigation_frame, bg=NAVIBAR_COLOR, text='Report', fg='#FFFFFF', font=(FONT, 15)).place(x=20, y=410)

        # Income
        img = tk.PhotoImage(file='taximana/asset/income.png')
        logo = tk.Label(self, image=img, bg=NAVIBAR_COLOR, width=10, height=10)
        logo.place(x=70, y=485)
        logo.image = img
        income = tk.Label(navigation_frame, bg=NAVIBAR_COLOR, text='Income', fg='white')
        income.place(x=100, y=480)

        # Expense
        img = tk.PhotoImage(file='taximana/asset/expense.png')
        logo = tk.Label(self, image=img, bg=NAVIBAR_COLOR, width=10, height=10)
        logo.place(x=70, y=565)
        logo.image = img
        expense = tk.Label(navigation_frame, bg=NAVIBAR_COLOR, text='Expense', fg='white')
        expense.place(x=100, y=560)

        # Summary
        img = tk.PhotoImage(file='taximana/asset/summary.png')
        logo = tk.Label(self, image=img, bg=NAVIBAR_COLOR, width=10, height=10)
        logo.place(x=70, y=645)
        logo.image = img
        summary = tk.Label(navigation_frame, bg=NAVIBAR_COLOR, text='Summary', fg='white')
        summary.place(x=100, y=640)

        # LogOut Button
        logout_bt = Button(navigation_frame, width=100, pady=6, text='Sign Out',fg='black', bg="white",font=(FONT, 15), borderless=1, command=lambda:controller.show_frame('SignInController'))
        logout_bt.place(x=75, y=720)

        # Statistic Bar
        stat_frame = tk.Frame(self, width=400, height=850, bg='#FFF5D2')
        stat_frame.place(x=250, y=0)

        # Stat Label 
        tk.Label(stat_frame, text='Statistic', bg='#FFF5D2', fg='black', font=(FONT, 22)).place(x=20, y=20)

        # Date
        tk.Label(stat_frame, text=f'Date: {date.today().strftime("%B %d, %Y")}', bg='#FFF5D2', fg='black', font=(FONT, 15)).place(x=20, y=55)

        # Total Frame 
        total_frame = tk.Frame(stat_frame, width=400, height=150, bg='#FFE5A1')
        total_frame.place(x=0, y=700)
        tk.Label(total_frame, text='Total Income: 1234567 vnd', bg='#FFE5A1', fg='black', font=(FONT, 20)).place(x=60, y=33)

        # Handle Click
        dashboard.bind("<Button-1>", lambda e: controller.show_frame('DashBoard'))
        driver.bind("<Button-1>", lambda e: controller.show_frame('Driver'))
        car.bind("<Button-1>", lambda e: controller.show_frame('Car'))
        income.bind("<Button-1>", lambda e: controller.show_frame('Income'))
        expense.bind("<Button-1>", lambda e: controller.show_frame('Expense'))
        summary.bind("<Button-1>", lambda e: controller.show_frame('Summary'))

        

        