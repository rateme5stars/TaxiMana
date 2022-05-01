import tkinter as tk
from taximana.constant import *
from tkmacosx import Button
from datetime import date


class Summary(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='white')
        self.controller = controller
        self.controller.title("Summary")

        # Navigation Bar
        navigation_frame = tk.Frame(self, width=250, height=850, bg=NAVIBAR_COLOR)
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

        # Stat Label 
        tk.Label(self, text='Statistic', bg='white', fg='black', font=(FONT, 22)).place(x=270, y=8)

        # Date
        tk.Label(self, text=f'Date: {date.today().strftime("%B %d, %Y")}', bg='white', fg='black', font=(FONT, 15)).place(x=270, y=55)

        # Graph
        graph = tk.Frame(self, width=850, height=500, bg='white')
        graph.place(x=320, y=100)

        tk.Frame(self, bg='black', width=1, height=502).place(x=317, y=100) # x axis
        tk.Frame(self, bg='black', width=853, height=1).place(x=317, y=602) # y axis

        tk.Frame(self, bg='black', width=5, height=1).place(x=312, y=100)
        tk.Label(self, text='100', font=(FONT, 11), bg='white').place(x=285, y=90)

        tk.Frame(self, bg='black', width=5, height=1).place(x=312, y=100+int(500*0.2))
        tk.Label(self, text='80', font=(FONT, 11), bg='white').place(x=288, y=90+int(500*0.2))

        tk.Frame(self, bg='black', width=5, height=1).place(x=312, y=100+int(500*0.4))
        tk.Label(self, text='60', font=(FONT, 11), bg='white').place(x=288, y=90+int(500*0.4))

        tk.Frame(self, bg='black', width=5, height=1).place(x=312, y=100+int(500*0.6))
        tk.Label(self, text='40', font=(FONT, 11), bg='white').place(x=288, y=90+int(500*0.6))

        tk.Frame(self, bg='black', width=5, height=1).place(x=312, y=100+int(500*0.8))
        tk.Label(self, text='20', font=(FONT, 11), bg='white').place(x=288, y=90+int(500*0.8))

        gap = 20
        w = 49
        bar1 = tk.Frame(graph, width=w, height=500, bg='white')
        bar1.place(x=0*w + 1*gap, y=0)
        bar2 = tk.Frame(graph, width=w, height=500, bg='white')
        bar2.place(x=1*w + 2*gap, y=0)
        bar3 = tk.Frame(graph, width=w, height=500, bg='white')
        bar3.place(x=2*w + 3*gap, y=0)
        bar4 = tk.Frame(graph, width=w, height=500, bg='white')
        bar4.place(x=3*w + 4*gap, y=0)
        bar5 = tk.Frame(graph, width=w, height=500, bg='white')
        bar5.place(x=4*w + 5*gap, y=0)
        bar6 = tk.Frame(graph, width=w, height=500, bg='white')
        bar6.place(x=5*w + 6*gap, y=0)
        bar7 = tk.Frame(graph, width=w, height=500, bg='white')
        bar7.place(x=6*w + 7*gap, y=0)
        bar8 = tk.Frame(graph, width=w, height=500, bg='white')
        bar8.place(x=7*w + 8*gap, y=0)
        bar9 = tk.Frame(graph, width=w, height=500, bg='white')
        bar9.place(x=8*w + 9*gap, y=0)
        bar10 = tk.Frame(graph, width=w, height=500, bg='white')
        bar10.place(x=9*w + 10*gap, y=0)
        bar11 = tk.Frame(graph, width=w, height=500, bg='white')
        bar11.place(x=10*w + 11*gap, y=0)
        bar12 = tk.Frame(graph, width=w, height=500, bg='white')
        bar12.place(x=11*w + 12*gap, y=0)

        tk.Label(self, text=('Jan'), bg='white', font=(FONT, 12)).place(x=350, y=610)
        tk.Label(self, text=('Feb'), bg='white', font=(FONT, 12)).place(x=420, y=610)
        tk.Label(self, text=('Mar'), bg='white', font=(FONT, 12)).place(x=490, y=610)
        tk.Label(self, text=('Apr'), bg='white', font=(FONT, 12)).place(x=560, y=610)
        tk.Label(self, text=('May'), bg='white', font=(FONT, 12)).place(x=625, y=610)
        tk.Label(self, text=('Jun'), bg='white', font=(FONT, 12)).place(x=695, y=610)
        tk.Label(self, text=('Jul'), bg='white', font=(FONT, 12)).place(x=765, y=610)
        tk.Label(self, text=('Aug'), bg='white', font=(FONT, 12)).place(x=835, y=610)
        tk.Label(self, text=('Sep'), bg='white', font=(FONT, 12)).place(x=905, y=610)
        tk.Label(self, text=('Oct'), bg='white', font=(FONT, 12)).place(x=975, y=610)
        tk.Label(self, text=('Nov'), bg='white', font=(FONT, 12)).place(x=1045, y=610)
        tk.Label(self, text=('Dec'), bg='white', font=(FONT, 12)).place(x=1115, y=610)

        
        bars = [bar1, bar2, bar3, bar4, bar5, bar6, bar7, bar8, bar9, bar10, bar11, bar12]
        self.create_bar(500*0.6, 500*0.2, bars)

        # Statistic 
        tk.Label(self, text="Spend 50% of total expense for maintaince per month", bg='white', font=(FONT, 15)).place(x=320, y=660)
        tk.Label(self, text="Spend 50% of total expense for salary per month", bg='white', font=(FONT, 15)).place(x=320, y=690)
        tk.Label(self, text="Average Expense per month:", bg='white', font=(FONT, 15)).place(x=320, y=720)

        # Note
        tk.Frame(self, width=50, height=20, bg='#2D319E').place(x=1000, y=665)
        tk.Frame(self, width=50, height=20, bg='#B57F71').place(x=1000, y=715)

        tk.Label(self, text=": Income", bg='white', font=(FONT, 16)).place(x=1055, y=660)
        tk.Label(self, text=": Expense", bg='white', font=(FONT, 16)).place(x=1055, y=710)

        # Handle Click
        dashboard.bind("<Button-1>", lambda e: controller.show_frame('DashBoard'))
        driver.bind("<Button-1>", lambda e: controller.show_frame('Driver'))
        car.bind("<Button-1>", lambda e: controller.show_frame('Car'))
        income.bind("<Button-1>", lambda e: controller.show_frame('Income'))
        expense.bind("<Button-1>", lambda e: controller.show_frame('Expense'))
        summary.bind("<Button-1>", lambda e: controller.show_frame('Summary'))
    
    def create_bar(self, i_height, e_height, bars):
        for bar in bars:
            bar.update()
            tk.Frame(bar, width=23, height=i_height, bg = '#2D319E').place(x=0, y=500-i_height)
            tk.Frame(bar, width=23, height=e_height, bg = '#B57F71').place(x=26, y=500-e_height)
        

        