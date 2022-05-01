import tkinter as tk
from tkmacosx import Button
from datetime import date
from taximana.constant import *

class DashBoard(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='white')
        self.controller = controller
        self.controller.title("DashBoard")

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

        # Statistic Bar
        stat_frame = tk.Frame(self, width=400, height=850, bg='#FFF5D2')
        stat_frame.place(x=250, y=0)

        # Stat Label 
        tk.Label(stat_frame, text='Statistic', bg='#FFF5D2', fg='black', font=(FONT, 22)).place(x=20, y=8)

        # Date
        tk.Label(stat_frame, text=f'Date: {date.today().strftime("%B %d, %Y")}', bg='#FFF5D2', fg='black', font=(FONT, 15)).place(x=20, y=55)

        # Income Label 
        tk.Label(stat_frame, text='Income', bg='#FFF5D2', fg='black', font=(FONT, 17)).place(x=60, y=120)
        tk.Label(stat_frame, text='12345678 vnd', bg='#FFF5D2', fg='black', font=(FONT, 14)).place(x=60, y=155)

        tk.Label(stat_frame, text='Spending', bg='#FFF5D2', fg='black', font=(FONT, 17)).place(x=250, y=120)
        tk.Label(stat_frame, text='2342345 vnd', bg='#FFF5D2', fg='black', font=(FONT, 14)).place(x=250, y=155)

        tk.Label(stat_frame, text='Per Km', bg='#FFF5D2', fg='black', font=(FONT, 17)).place(x=60, y=200)
        tk.Label(stat_frame, text='12000 vnd', bg='#FFF5D2', fg='black', font=(FONT, 14)).place(x=60, y=235)

        tk.Label(stat_frame, text='Park Load', bg='#FFF5D2', fg='black', font=(FONT, 17)).place(x=250, y=200)
        tk.Label(stat_frame, text='50/80', bg='#FFF5D2', fg='black', font=(FONT, 14)).place(x=250, y=235)

        # Line 
        tk.Frame(stat_frame, width=400, height=1, bg='gray').place(x=0, y=300)

        # Order Stat
        tk.Label(stat_frame, text='Order Statistic', bg='#FFF5D2', fg='black', font=(FONT, 20)).place(x=20, y=320)

        # Graph Frame
        graph_frame1 = tk.Frame(stat_frame, bg='#FFF5D2', width=290, height=200)
        graph_frame1.place(x=70, y=380)

        tk.Frame(stat_frame, bg='black', width=293, height=1).place(x=67, y=582) # x axis
        tk.Frame(stat_frame, bg='black', width=1, height=202).place(x=67, y=380) # y axis

        tk.Frame(stat_frame, bg='black', width=5, height=1).place(x=62, y=380)
        tk.Label(stat_frame, text='100', font=(FONT, 9), bg='#FFF5D2').place(x=40, y=370)

        tk.Frame(stat_frame, bg='black', width=5, height=1).place(x=62, y=380+int(200*0.2))
        tk.Label(stat_frame, text='80', font=(FONT, 9), bg='#FFF5D2').place(x=45, y=370+int(200*0.2))

        tk.Frame(stat_frame, bg='black', width=5, height=1).place(x=62, y=380+int(200*0.4))
        tk.Label(stat_frame, text='60', font=(FONT, 9), bg='#FFF5D2').place(x=45, y=370+int(200*0.4))

        tk.Frame(stat_frame, bg='black', width=5, height=1).place(x=62, y=380+int(200*0.6))
        tk.Label(stat_frame, text='40', font=(FONT, 9), bg='#FFF5D2').place(x=45, y=370+int(200*0.6))

        tk.Frame(stat_frame, bg='black', width=5, height=1).place(x=62, y=380+int(200*0.8))
        tk.Label(stat_frame, text='20', font=(FONT, 9), bg='#FFF5D2').place(x=45, y=370+int(200*0.8))

        # Bar
        tk.Frame(graph_frame1, width=100, height=200*0.6, bg='#BA744D').place(x=25, y=200-200*0.6)
        tk.Frame(graph_frame1, width=100, height=200*0.4, bg='#557174').place(x=170, y=200-200*0.4)

        # Note 
        tk.Frame(stat_frame, width=15, height=15, bg='#BA744D').place(x=80, y=600)
        tk.Label(stat_frame, text='Accepted', bg='#FFF5D2', fg='black').place(x=100, y=595)

        tk.Frame(stat_frame, width=15, height=15, bg='#557174').place(x=200, y=600)
        tk.Label(stat_frame, text='Cancelled', bg='#FFF5D2', fg='black').place(x=220, y=595)
        
        # Total Frame 
        total_frame = tk.Frame(stat_frame, width=400, height=150, bg='#FFE5A1')
        total_frame.place(x=0, y=700)
        tk.Label(total_frame, text='Total Bookings: 1234567 vnd', bg='#FFE5A1', fg='black', font=(FONT, 20)).place(x=60, y=33)

        # Vertical line
        tk.Frame(self, width=1, height=800, bg='black').place(x=650, y=0)

        # Details
        tk.Label(self, text='Details', bg='white', fg='black', font=(FONT, 22)).place(x=700, y=8)
        img = tk.PhotoImage(file='taximana/asset/profit.png')
        logo = tk.Label(self, image=img, bg='white', width=160, height=110)
        logo.place(x=700, y=80)
        logo.image = img

        tk.Label(self, text='On Road', bg='white', fg='black', font=(FONT, 15)).place(x=900, y=90)
        tk.Label(self, text='On Order', bg='white', fg='black', font=(FONT, 15)).place(x=1000, y=90)
        tk.Label(self, text='Waiting', bg='white', fg='black', font=(FONT, 15)).place(x=1100, y=90)

        tk.Label(self, text='150', bg='white', fg='black', font=(FONT, 15)).place(x=920, y=120)
        tk.Label(self, text='50', bg='white', fg='black', font=(FONT, 15)).place(x=1020, y=120)
        tk.Label(self, text='90', bg='white', fg='black', font=(FONT, 15)).place(x=1120, y=120)

        # Line
        tk.Frame(self, width=550, height=1, bg='gray').place(x=650, y=220)

        # Profit Graph
        tk.Label(self, text='Monthly Profit', bg='white', fg='black', font=(FONT, 18)).place(x=700, y=250)

        graph_frame2 = tk.Frame(self, bg='white', width=450, height=250)
        graph_frame2.place(x=700, y=350)

        tk.Label(self, text='Billion', bg='white', font=(FONT, 12)).place(x=700, y=320)

        tk.Frame(self, bg='black', width=453, height=1).place(x=697, y=602) # x axis
        tk.Frame(self, bg='black', width=1, height=252).place(x=697, y=350) # y axis

        tk.Frame(self, bg='black', width=5, height=1).place(x=692, y=350)
        tk.Label(self, text='10', font=(FONT, 9), bg='white').place(x=675, y=342)

        tk.Frame(self, bg='black', width=5, height=1).place(x=692, y=350+int(250*0.2))
        tk.Label(self, text='8', font=(FONT, 9), bg='white').place(x=675, y=342+int(250*0.2))

        tk.Frame(self, bg='black', width=5, height=1).place(x=692, y=350+int(250*0.4))
        tk.Label(self, text='6', font=(FONT, 9), bg='white').place(x=675, y=342+int(250*0.4))

        tk.Frame(self, bg='black', width=5, height=1).place(x=692, y=350+int(250*0.6))
        tk.Label(self, text='4', font=(FONT, 9), bg='white').place(x=675, y=342+int(250*0.6))

        tk.Frame(self, bg='black', width=5, height=1).place(x=692, y=350+int(250*0.8))
        tk.Label(self, text='2', font=(FONT, 9), bg='white').place(x=675, y=342+int(250*0.8))

        # Bar
        gap = 16
        w = 20
        tk.Frame(graph_frame2, width=w, height=250*0.6, bg='#2D319E').place(x=0*w + 1*gap, y=250-250*0.6)
        tk.Frame(graph_frame2, width=w, height=250*0.6, bg='#2D319E').place(x=1*w + 2*gap, y=250-250*0.6)
        tk.Frame(graph_frame2, width=w, height=250*0.6, bg='#2D319E').place(x=2*w + 3*gap, y=250-250*0.6)
        tk.Frame(graph_frame2, width=w, height=250*0.6, bg='#2D319E').place(x=3*w + 4*gap, y=250-250*0.6)
        tk.Frame(graph_frame2, width=w, height=250*0.6, bg='#2D319E').place(x=4*w + 5*gap, y=250-250*0.6)
        tk.Frame(graph_frame2, width=w, height=250*0.6, bg='#2D319E').place(x=5*w + 6*gap, y=250-250*0.6)
        tk.Frame(graph_frame2, width=w, height=250*0.6, bg='#2D319E').place(x=6*w + 7*gap, y=250-250*0.6)
        tk.Frame(graph_frame2, width=w, height=250*0.6, bg='#2D319E').place(x=7*w + 8*gap, y=250-250*0.6)
        tk.Frame(graph_frame2, width=w, height=250*0.6, bg='#2D319E').place(x=8*w + 9*gap, y=250-250*0.6)
        tk.Frame(graph_frame2, width=w, height=250*0.6, bg='#2D319E').place(x=9*w + 10*gap, y=250-250*0.6)
        tk.Frame(graph_frame2, width=w, height=250*0.6, bg='#2D319E').place(x=10*w + 11*gap, y=250-250*0.6)
        tk.Frame(graph_frame2, width=w, height=250*0.6, bg='#2D319E').place(x=11*w + 12*gap, y=250-250*0.6)

        # Stat 
        tk.Label(self, text='Average Until Now: 123456 vnd', bg='white', font=(FONT, 15)).place(x=730, y=630)
        tk.Label(self, text='Highest Month: 123456 vnd', bg='white', font=(FONT, 15)).place(x=730, y=660)
        tk.Label(self, text='Lowest Month: 123456 vnd', bg='white', font=(FONT, 15)).place(x=730, y=690)

        # Handle Click
        dashboard.bind("<Button-1>", lambda e: controller.show_frame('DashBoard'))
        driver.bind("<Button-1>", lambda e: controller.show_frame('Driver'))
        car.bind("<Button-1>", lambda e: controller.show_frame('Car'))
        income.bind("<Button-1>", lambda e: controller.show_frame('Income'))
        expense.bind("<Button-1>", lambda e: controller.show_frame('Expense'))
        summary.bind("<Button-1>", lambda e: controller.show_frame('Summary'))

        

        