import tkinter as tk
from taximana.constant import *
from tkmacosx import Button
from datetime import date
import numpy as np

from taximana.viewcontrollers.generate_data import DriverData


class Income(tk.Frame):
    def __init__(self, parent, controller):
        driver = DriverData()
        self.last_12_month_df = driver.driver_df_list[-12:]
        tk.Frame.__init__(self, parent, bg='white')
        self.controller = controller
        self.controller.title("Income")

        # Navigation Bar
        navigation_frame = tk.Frame(self, width=250, height=850, bg=NAVIBAR_COLOR)
        navigation_frame.place(x=0, y=0)
        
        # Username
        username_frame = tk.Frame(navigation_frame, width=265, height=50, bg=NAVIBAR_COLOR)
        username_frame.place(x=0, y=0)
        username_label = tk.Label(username_frame, bg=NAVIBAR_COLOR, text='Taxi Manager', fg='white', font=(FONT, 20))
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
        em_pro = list()
        co_pro = list()
        for m in self.last_12_month_df:
            employee = sum(m.loc[m['kind'] == 'Employee']['income'])
            co_worker = sum(m.loc[m['kind'] == 'Co-Worker']['income'])
            income_employee = employee / 20000000000
            income_co = co_worker / 20000000000
            em_pro.append(income_employee)
            co_pro.append(income_co)
        
        em_height = np.array(em_pro) * 500
        co_height = np.array(co_pro) * 500

        graph = tk.Frame(self, width=850, height=500, bg='white')
        graph.place(x=320, y=100)

        tk.Frame(self, bg='black', width=1, height=502).place(x=317, y=100) # x axis
        tk.Frame(self, bg='black', width=853, height=1).place(x=317, y=602) # y axis

        tk.Frame(self, bg='black', width=5, height=1).place(x=312, y=100)
        tk.Label(self, text='20', font=(FONT, 11), bg='white').place(x=288, y=90)

        tk.Frame(self, bg='black', width=5, height=1).place(x=312, y=100+int(500*0.2))
        tk.Label(self, text='16', font=(FONT, 11), bg='white').place(x=288, y=90+int(500*0.2))

        tk.Frame(self, bg='black', width=5, height=1).place(x=312, y=100+int(500*0.4))
        tk.Label(self, text='12', font=(FONT, 11), bg='white').place(x=288, y=90+int(500*0.4))

        tk.Frame(self, bg='black', width=5, height=1).place(x=312, y=100+int(500*0.6))
        tk.Label(self, text='8', font=(FONT, 11), bg='white').place(x=288, y=90+int(500*0.6))

        tk.Frame(self, bg='black', width=5, height=1).place(x=312, y=100+int(500*0.8))
        tk.Label(self, text='4', font=(FONT, 11), bg='white').place(x=288, y=90+int(500*0.8))

        gap = 20
        w = 49
        bar1 = tk.Frame(graph, width=w, height=500, bg='white')
        bar1.place(x=0*w + 1*gap, y=0)
        tk.Frame(bar1, width=23, height=em_height[0], bg = '#2D319E').place(x=0, y=500-em_height[0])
        tk.Frame(bar1, width=23, height=co_height[0], bg = '#B57F71').place(x=26, y=500-co_height[0])

        bar2 = tk.Frame(graph, width=w, height=500, bg='white')
        bar2.place(x=1*w + 2*gap, y=0)
        tk.Frame(bar2, width=23, height=em_height[1], bg = '#2D319E').place(x=0, y=500-em_height[1])
        tk.Frame(bar2, width=23, height=co_height[1], bg = '#B57F71').place(x=26, y=500-co_height[1])

        bar3 = tk.Frame(graph, width=w, height=500, bg='white')
        bar3.place(x=2*w + 3*gap, y=0)
        tk.Frame(bar3, width=23, height=em_height[2], bg = '#2D319E').place(x=0, y=500-em_height[2])
        tk.Frame(bar3, width=23, height=co_height[2], bg = '#B57F71').place(x=26, y=500-co_height[2])

        bar4 = tk.Frame(graph, width=w, height=500, bg='white')
        bar4.place(x=3*w + 4*gap, y=0)
        tk.Frame(bar4, width=23, height=em_height[3], bg = '#2D319E').place(x=0, y=500-em_height[3])
        tk.Frame(bar4, width=23, height=co_height[3], bg = '#B57F71').place(x=26, y=500-co_height[3])

        bar5 = tk.Frame(graph, width=w, height=500, bg='white')
        bar5.place(x=4*w + 5*gap, y=0)
        tk.Frame(bar5, width=23, height=em_height[4], bg = '#2D319E').place(x=0, y=500-em_height[4])
        tk.Frame(bar5, width=23, height=co_height[4], bg = '#B57F71').place(x=26, y=500-co_height[4])

        bar6 = tk.Frame(graph, width=w, height=500, bg='white')
        bar6.place(x=5*w + 6*gap, y=0)
        tk.Frame(bar6, width=23, height=em_height[5], bg = '#2D319E').place(x=0, y=500-em_height[5])
        tk.Frame(bar6, width=23, height=co_height[5], bg = '#B57F71').place(x=26, y=500-co_height[5])

        bar7 = tk.Frame(graph, width=w, height=500, bg='white')
        bar7.place(x=6*w + 7*gap, y=0)
        tk.Frame(bar7, width=23, height=em_height[6], bg = '#2D319E').place(x=0, y=500-em_height[6])
        tk.Frame(bar7, width=23, height=co_height[6], bg = '#B57F71').place(x=26, y=500-co_height[6])

        bar8 = tk.Frame(graph, width=w, height=500, bg='white')
        bar8.place(x=7*w + 8*gap, y=0)
        tk.Frame(bar8, width=23, height=em_height[7], bg = '#2D319E').place(x=0, y=500-em_height[7])
        tk.Frame(bar8, width=23, height=co_height[7], bg = '#B57F71').place(x=26, y=500-co_height[7])

        bar9 = tk.Frame(graph, width=w, height=500, bg='white')
        bar9.place(x=8*w + 9*gap, y=0)
        tk.Frame(bar9, width=23, height=em_height[8], bg = '#2D319E').place(x=0, y=500-em_height[8])
        tk.Frame(bar9, width=23, height=co_height[8], bg = '#B57F71').place(x=26, y=500-co_height[8])

        bar10 = tk.Frame(graph, width=w, height=500, bg='white')
        bar10.place(x=9*w + 10*gap, y=0)
        tk.Frame(bar10, width=23, height=em_height[9], bg = '#2D319E').place(x=0, y=500-em_height[9])
        tk.Frame(bar10, width=23, height=co_height[9], bg = '#B57F71').place(x=26, y=500-co_height[9])

        bar11 = tk.Frame(graph, width=w, height=500, bg='white')
        bar11.place(x=10*w + 11*gap, y=0)
        tk.Frame(bar11, width=23, height=em_height[10], bg = '#2D319E').place(x=0, y=500-em_height[10])
        tk.Frame(bar11, width=23, height=co_height[10], bg = '#B57F71').place(x=26, y=500-co_height[10])

        bar12 = tk.Frame(graph, width=w, height=500, bg='white')
        bar12.place(x=11*w + 12*gap, y=0)
        tk.Frame(bar12, width=23, height=em_height[11], bg = '#2D319E').place(x=0, y=500-em_height[11])
        tk.Frame(bar12, width=23, height=co_height[11], bg = '#B57F71').place(x=26, y=500-co_height[11])

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
        
        # Note
        tk.Frame(self, width=50, height=20, bg='#2D319E').place(x=1000, y=665)
        tk.Frame(self, width=50, height=20, bg='#B57F71').place(x=1000, y=715)

        tk.Label(self, text=": Employee", bg='white', font=(FONT, 16)).place(x=1055, y=660)
        tk.Label(self, text=": Co-Worker", bg='white', font=(FONT, 16)).place(x=1055, y=710)

        # Handle Click
        dashboard.bind("<Button-1>", lambda e: controller.show_frame('DashBoard'))
        driver.bind("<Button-1>", lambda e: controller.show_frame('Driver'))
        car.bind("<Button-1>", lambda e: controller.show_frame('Car'))
        income.bind("<Button-1>", lambda e: controller.show_frame('Income'))
        expense.bind("<Button-1>", lambda e: controller.show_frame('Expense'))
        summary.bind("<Button-1>", lambda e: controller.show_frame('Summary'))

        

        