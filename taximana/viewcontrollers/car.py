import tkinter as tk
from taximana.constant import *
from tkmacosx import Button
from datetime import date
import tkinter.ttk as ttk
import os
import json
from pathlib import Path
from tkinter import messagebox

'''
#TODO:
- more condition engine and chassis number
'''


class Car(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='white')
        self.controller = controller
        self.controller.title("Car")

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

        # Statistic
        tk.Label(stat_frame, text='Work Well', bg='#FFF5D2', fg='black', font=(FONT, 17)).place(x=60, y=120)
        tk.Label(stat_frame, text='12345678 vnd', bg='#FFF5D2', fg='black', font=(FONT, 14)).place(x=60, y=155)

        tk.Label(stat_frame, text='Maintain', bg='#FFF5D2', fg='black', font=(FONT, 17)).place(x=250, y=120)
        tk.Label(stat_frame, text='2342345 vnd', bg='#FFF5D2', fg='black', font=(FONT, 14)).place(x=250, y=155)

        tk.Label(stat_frame, text='Out Date', bg='#FFF5D2', fg='black', font=(FONT, 17)).place(x=60, y=200)
        tk.Label(stat_frame, text='12000 vnd', bg='#FFF5D2', fg='black', font=(FONT, 14)).place(x=60, y=235)

        tk.Label(stat_frame, text='Valid', bg='#FFF5D2', fg='black', font=(FONT, 17)).place(x=250, y=200)
        tk.Label(stat_frame, text='50/80', bg='#FFF5D2', fg='black', font=(FONT, 14)).place(x=250, y=235)

        # Horizontal Line 
        tk.Frame(stat_frame, width=400, height=1, bg='gray').place(x=0, y=300)

        tk.Label(stat_frame,text='License Plate:', bg='#FFF5D2', fg='black', font=(FONT, 12)).place(x=10, y=320)
        self.license_plate_entry = tk.Entry(stat_frame, highlightthickness=3, border=0, width=25, fg='black', bg='#FFF5D2', font=(FONT, 12))
        self.license_plate_entry.config(highlightbackground='#FFF5D2', highlightcolor='#FFF5D2')
        self.license_plate_entry.place(x=100, y=320)
        tk.Frame(stat_frame,width=230, height=1, bg='black').place(x=103, y=345)

        tk.Label(stat_frame,text='Brand:', bg='#FFF5D2', fg='black', font=(FONT, 12)).place(x=10, y=360)
        self.brand_entry = tk.Entry(stat_frame, highlightthickness=3, border=0, width=25, fg='black', bg='#FFF5D2', font=(FONT, 12))
        self.brand_entry.config(highlightbackground='#FFF5D2', highlightcolor='#FFF5D2')
        self.brand_entry.place(x=55, y=360)
        tk.Frame(stat_frame,width=252, height=1, bg='black').place(x=58, y=385)

        tk.Label(stat_frame,text='Model:', bg='#FFF5D2', fg='black', font=(FONT, 12)).place(x=10, y=400)
        self.model_entry = tk.Entry(stat_frame, highlightthickness=3, border=0, width=25, fg='black', bg='#FFF5D2', font=(FONT, 12))
        self.model_entry.config(highlightbackground='#FFF5D2', highlightcolor='#FFF5D2')
        self.model_entry.place(x=55, y=400)
        tk.Frame(stat_frame,width=252, height=1, bg='black').place(x=58, y=425)

        tk.Label(stat_frame,text='Seats:', bg='#FFF5D2', fg='black', font=(FONT, 12)).place(x=10, y=440)
        self.seats_entry = tk.Entry(stat_frame, highlightthickness=3, border=0, width=25, fg='black', bg='#FFF5D2', font=(FONT, 12))
        self.seats_entry.config(highlightbackground='#FFF5D2', highlightcolor='#FFF5D2')
        self.seats_entry.place(x=55, y=440)
        tk.Frame(stat_frame,width=252, height=1, bg='black').place(x=58, y=465)

        tk.Label(stat_frame,text='Engine Number:', bg='#FFF5D2', fg='black', font=(FONT, 12)).place(x=10, y=480)
        self.engine_num_entry = tk.Entry(stat_frame, highlightthickness=3, border=0, width=25, fg='black', bg='#FFF5D2', font=(FONT, 12))
        self.engine_num_entry.config(highlightbackground='#FFF5D2', highlightcolor='#FFF5D2')
        self.engine_num_entry.place(x=120, y=480)
        tk.Frame(stat_frame,width=252, height=1, bg='black').place(x=123, y=505)

        tk.Label(stat_frame,text='Chassis Number:', bg='#FFF5D2', fg='black', font=(FONT, 12)).place(x=10, y=520)
        self.chassis_num_entry = tk.Entry(stat_frame, highlightthickness=3, border=0, width=25, fg='black', bg='#FFF5D2', font=(FONT, 12))
        self.chassis_num_entry.config(highlightbackground='#FFF5D2', highlightcolor='#FFF5D2')
        self.chassis_num_entry.place(x=120, y=520)
        tk.Frame(stat_frame,width=252, height=1, bg='black').place(x=123, y=545)

        tk.Label(stat_frame,text='Import Day:', bg='#FFF5D2', fg='black', font=(FONT, 12)).place(x=10, y=560)
        self.import_entry = tk.Entry(stat_frame, highlightthickness=3, border=0, width=25, fg='black', bg='#FFF5D2', font=(FONT, 12))
        self.import_entry.config(highlightbackground='#FFF5D2', highlightcolor='#FFF5D2')
        self.import_entry.place(x=100, y=560)
        tk.Frame(stat_frame,width=252, height=1, bg='black').place(x=103, y=585)
        
        tk.Label(stat_frame,text='Registration Deadline:', bg='#FFF5D2', fg='black', font=(FONT, 12)).place(x=10, y=600)
        self.regist_dl_entry = tk.Entry(stat_frame, highlightthickness=3, border=0, width=25, fg='black', bg='#FFF5D2', font=(FONT, 12))
        self.regist_dl_entry.config(highlightbackground='#FFF5D2', highlightcolor='#FFF5D2')
        self.regist_dl_entry.place(x=145, y=600)
        tk.Frame(stat_frame,width=223, height=1, bg='black').place(x=148, y=625)

        tk.Label(stat_frame,text='Travelled(Km):', bg='#FFF5D2', fg='black', font=(FONT, 12)).place(x=10, y=640)
        self.travelled_entry = tk.Entry(stat_frame, highlightthickness=3, border=0, width=25, fg='black', bg='#FFF5D2', font=(FONT, 12))
        self.travelled_entry.config(highlightbackground='#FFF5D2', highlightcolor='#FFF5D2')
        self.travelled_entry.place(x=100, y=640)
        tk.Frame(stat_frame,width=248, height=1, bg='black').place(x=103, y=665)
        
        tk.Label(stat_frame,text='Car ID:', bg='#FFF5D2', fg='black', font=(FONT, 12)).place(x=10, y=680)
        self.car_id_entry = tk.Entry(stat_frame, highlightthickness=3, border=0, width=25, fg='black', bg='#FFF5D2', font=(FONT, 12))
        self.car_id_entry.config(highlightbackground='#FFF5D2', highlightcolor='#FFF5D2')
        self.car_id_entry.place(x=60, y=680)
        tk.Frame(stat_frame,width=252, height=1, bg='black').place(x=63, y=705)

        tk.Label(stat_frame,text='Driver ID:', bg='#FFF5D2', fg='black', font=(FONT, 12)).place(x=10, y=720)
        self.driver_id_entry = tk.Entry(stat_frame, highlightthickness=3, border=0, width=25, fg='black', bg='#FFF5D2', font=(FONT, 12))
        self.driver_id_entry.config(highlightbackground='#FFF5D2', highlightcolor='#FFF5D2')
        self.driver_id_entry.place(x=90, y=720)
        tk.Frame(stat_frame,width=252, height=1, bg='black').place(x=93, y=745)

        # Clear Button
        add_bt = Button(stat_frame, width=50, pady=6, text='Clear',fg='black', bg="white",font=(FONT, 10), borderless=1, command=self.clear_add_entries)
        add_bt.place(x=100, y=760)

        # Add Button
        add_bt = Button(stat_frame, width=50, pady=6, text='Add',fg='black', bg="white",font=(FONT, 10), borderless=1, command=self.add_click)
        add_bt.place(x=170, y=760)

        # Update Button
        update_bt = Button(stat_frame, width=50, pady=6, text='Change',fg='black', bg="white",font=(FONT, 10), borderless=1, command=self.change_click)
        update_bt.place(x=240, y=760)

        # Remove Button
        remove_bt = Button(stat_frame, width=50, pady=6, text='Remove',fg='black', bg="white",font=(FONT, 10), borderless=1, command=self.remove_click)
        remove_bt.place(x=310, y=760)

        # Vertical line
        tk.Frame(self, width=1, height=800, bg='black').place(x=650, y=0)

        # Tree View
        self.treev = ttk.Treeview(self, select='browse')
        self.treev.place(x=651, y=0)
        verscrlbar = tk.Scrollbar(self, orient='vertical', command=self.treev.yview)
        self.treev.configure(xscrollcommand=verscrlbar.set)
        self.treev['columns'] = ('1', '2', '3')
        self.treev['show'] = 'headings'
        self.treev.column('1', width=229, anchor='c')
        self.treev.column('2', width=180, anchor='c')
        self.treev.column('3', width=180, anchor='c')
        self.treev.heading('1', text='License Plate')
        self.treev.heading('2', text='Car ID')
        self.treev.heading('3', text='Driver ID')
        self.treev.bind("<<TreeviewSelect>>", self.treeview_click)
        
        self.load_table()

        # Horizontal Line 
        tk.Frame(self, width=548, height=1, bg='gray').place(x=651, y=210)

        # Details 
        tk.Label(self, text="Car Details", font=(FONT, 18), bg='white').place(x=700, y=220)

        tk.Label(self, text="License Plate:", bg='white', fg='black', font=(FONT, 16)).place(x=700, y=300)
        tk.Label(self, text="Brand:", bg='white', fg='black', font=(FONT, 16)).place(x=700, y=340)
        tk.Label(self, text="Model:", bg='white', fg='black', font=(FONT, 16)).place(x=700, y=380)        
        tk.Label(self, text="Seats:", bg='white', fg='black', font=(FONT, 16)).place(x=700, y=420)    
        tk.Label(self, text="Engine Number:", bg='white', fg='black', font=(FONT, 16)).place(x=700, y=460)
        tk.Label(self, text="Chassis Number:", bg='white', fg='black', font=(FONT, 16)).place(x=700, y=500)
        tk.Label(self, text="Import Day:", bg='white', fg='black', font=(FONT, 16)).place(x=700, y=540)
        tk.Label(self, text="Registration Deadline:", bg='white', fg='black', font=(FONT, 16)).place(x=700, y=580)    
        tk.Label(self, text="Travelled(Km):", bg='white', fg='black', font=(FONT, 16)).place(x=700, y=620)
        tk.Label(self, text="Car ID:", bg='white', fg='black', font=(FONT, 16)).place(x=700, y=660)
        tk.Label(self, text="Driver ID:", bg='white', fg='black', font=(FONT, 16)).place(x=700, y=700)
        tk.Label(self, text="Search:", bg='white', fg='black', font=(FONT, 16)).place(x=700, y=740)

        self.search_entry = tk.Entry(self, highlightthickness=3, border=0, width=25, fg='black', bg='white', font=(FONT, 14))
        self.search_entry.config(highlightbackground='white', highlightcolor='white')
        self.search_entry.place(x=765, y=740)
        tk.Frame(self,width=232, height=1, bg='black').place(x=765, y=765)

        # Search Button
        search_bt = Button(self, width=50, pady=6, text='Search',fg='black', bg="white",font=(FONT, 10), borderless=1, command=self.search_click)
        search_bt.place(x=1025, y=740)

        # Handle Click
        dashboard.bind("<Button-1>", lambda e: controller.show_frame('DashBoard'))
        driver.bind("<Button-1>", lambda e: controller.show_frame('Driver'))
        car.bind("<Button-1>", lambda e: controller.show_frame('Car'))
        income.bind("<Button-1>", lambda e: controller.show_frame('Income'))
        expense.bind("<Button-1>", lambda e: controller.show_frame('Expense'))
        summary.bind("<Button-1>", lambda e: controller.show_frame('Summary'))
    
    def treeview_click(self, *arg):
        cur_item = self.treev.focus()
        car_id = self.treev.item(cur_item)['values'][1]
        data_file = open(CAR_PATH, 'r')
        for car_info in data_file:
            car_json = eval(car_info)
            tmp = {car_json['car_id'] : [car_json['license_plate'], car_json['brand'], car_json['model'], car_json['seats'], car_json['engine_num'], car_json['chassis_num'], car_json['import_day'], car_json['regist_dl'], car_json['travelled'], car_json['driver_id'],]}
            for key, value in tmp.items():
                if key == car_id:
                    self.show_info(value[0], value[1], value[2], value[3], value[4], value[5], value[6], value[7], value[8], car_id, value[9])
                    self.show_in_entry(value[0], value[1], value[2], value[3], value[4], value[5], value[6], value[7], value[8], car_id, value[9])
    
    def show_info(self, license_plate, brand, model, car_id, driver_id, chassis_num, engine_num, travelled, seats, import_day, regist_dl):
        tk.Frame(self, bg='white', width=200, height=30).place(x=820, y=297)
        tk.Frame(self, bg='white', width=200, height=30).place(x=763, y=337)
        tk.Frame(self, bg='white', width=200, height=30).place(x=763, y=377)
        tk.Frame(self, bg='white', width=200, height=30).place(x=758, y=417)
        tk.Frame(self, bg='white', width=200, height=30).place(x=835, y=457)
        tk.Frame(self, bg='white', width=200, height=30).place(x=845, y=497)
        tk.Frame(self, bg='white', width=200, height=30).place(x=805, y=537)
        tk.Frame(self, bg='white', width=200, height=30).place(x=885, y=577)
        tk.Frame(self, bg='white', width=200, height=30).place(x=825, y=617)
        tk.Frame(self, bg='white', width=200, height=30).place(x=765, y=657)
        tk.Frame(self, bg='white', width=200, height=30).place(x=785, y=697)
        tk.Label(self, text=license_plate, bg='white', fg='black', font=(FONT, 16)).place(x=825, y=300)
        tk.Label(self, text=brand, bg='white', fg='black', font=(FONT, 16)).place(x=768, y=340)
        tk.Label(self, text=model, bg='white', fg='black', font=(FONT, 16)).place(x=768, y=380)        
        tk.Label(self, text=seats, bg='white', fg='black', font=(FONT, 16)).place(x=763, y=420)    
        tk.Label(self, text=engine_num, bg='white', fg='black', font=(FONT, 16)).place(x=840, y=460)
        tk.Label(self, text=chassis_num, bg='white', fg='black', font=(FONT, 16)).place(x=850, y=500)
        tk.Label(self, text=import_day, bg='white', fg='black', font=(FONT, 16)).place(x=810, y=540)
        tk.Label(self, text=regist_dl, bg='white', fg='black', font=(FONT, 16)).place(x=890, y=580)    
        tk.Label(self, text=travelled, bg='white', fg='black', font=(FONT, 16)).place(x=830, y=620)
        tk.Label(self, text=car_id, bg='white', fg='black', font=(FONT, 16)).place(x=770, y=660)
        tk.Label(self, text=driver_id, bg='white', fg='black', font=(FONT, 16)).place(x=790, y=700)
    
    def show_in_entry(self, license_plate, brand, model, car_id, driver_id, chassis_num, engine_num, travelled, seats, import_day, regist_dl):
        self.clear_add_entries()
        self.license_plate_entry.insert(0, license_plate)
        self.brand_entry.insert(0, brand)      
        self.model_entry.insert(0, model)      
        self.seats_entry.insert(0, seats)      
        self.engine_num_entry.insert(0, engine_num)
        self.chassis_num_entry.insert(0, chassis_num)
        self.import_entry.insert(0, import_day)   
        self.regist_dl_entry.insert(0, regist_dl)
        self.travelled_entry.insert(0, travelled)
        self.car_id_entry.insert(0, car_id)  
        self.driver_id_entry.insert(0, driver_id)

    def load_table(self):
        data_file = open(CAR_PATH, 'r')
        if data_file is not None:
            for car_info in data_file:
                car_json = eval(car_info)
                self.treev.insert("", 'end', text=f'driver', values=(car_json['license_plate'], car_json['car_id'], car_json['driver_id']))
    
    def clear_add_entries(self):
        self.license_plate_entry.delete(0, tk.END)
        self.brand_entry.delete(0, tk.END)
        self.model_entry.delete(0, tk.END)
        self.seats_entry.delete(0, tk.END)
        self.engine_num_entry.delete(0, tk.END)
        self.chassis_num_entry.delete(0, tk.END)
        self.import_entry.delete(0, tk.END)
        self.regist_dl_entry.delete(0, tk.END)
        self.travelled_entry.delete(0, tk.END)
        self.car_id_entry.delete(0, tk.END)
        self.driver_id_entry.delete(0, tk.END)
    
    def clear_info(self):
        tk.Frame(self, bg='white', width=200, height=30).place(x=820, y=297)
        tk.Frame(self, bg='white', width=200, height=30).place(x=763, y=337)
        tk.Frame(self, bg='white', width=200, height=30).place(x=763, y=377)
        tk.Frame(self, bg='white', width=200, height=30).place(x=758, y=417)
        tk.Frame(self, bg='white', width=200, height=30).place(x=835, y=457)
        tk.Frame(self, bg='white', width=200, height=30).place(x=845, y=497)
        tk.Frame(self, bg='white', width=200, height=30).place(x=805, y=537)
        tk.Frame(self, bg='white', width=200, height=30).place(x=885, y=577)
        tk.Frame(self, bg='white', width=200, height=30).place(x=825, y=617)
        tk.Frame(self, bg='white', width=200, height=30).place(x=765, y=657)
        tk.Frame(self, bg='white', width=200, height=30).place(x=785, y=697)

    def add_click(self):
        license_plate = self.license_plate_entry.get()
        brand = self.brand_entry.get()
        model = self.model_entry.get()
        seats = self.seats_entry.get()
        engine_num = self.engine_num_entry.get()
        chassis_num = self.chassis_num_entry.get()
        import_day = self.import_entry.get()
        regist_dl = self.regist_dl_entry.get()
        travelled = self.travelled_entry.get()
        car_id = self.car_id_entry.get()
        driver_id = self.driver_id_entry.get()

        car = {
            'car_id': car_id,
            'driver_id' : driver_id,
            'license_plate' : license_plate,
            'brand' : brand,
            'model' : model,
            'seats' : seats,
            'engine_num' : engine_num,
            'chassis_num' : chassis_num,
            'import_day' : import_day,
            'regist_dl':regist_dl,
            'travelled':travelled,
        }

        car_json = json.dumps(car)
        car_json_str = str(car_json)
        if Path(CAR_PATH).is_file():
            condition = self.check_existence(driver_id, car_id)
            if condition == 1:
                messagebox.showerror('Invalid','Driver ID already exist')
            elif condition == 2:
                messagebox.showerror('Invalid','Car ID already exist')
            elif condition == 0:
                self.treev.insert("", 'end', text=f'driver', values=(license_plate, car_id, driver_id))
                file = open(CAR_PATH, 'a')
                file.write(f'{car_json_str}\n')
                file.close()
                self.show_info(license_plate, brand, model, car_id, driver_id, chassis_num, engine_num, travelled, seats, import_day, regist_dl)
                self.clear_add_entries()

        else:
            self.treev.insert("", 'end', text=f'driver', values=(license_plate, car_id, driver_id))
            file = open(CAR_PATH, 'w')
            file.write(f'{car_json_str}\n')
            file.close()
            self.show_info(license_plate, brand, model, car_id, driver_id, chassis_num, engine_num, travelled, seats, import_day, regist_dl)
            self.clear_add_entries()

    def remove_click(self):
        selected_item = self.treev.selection()
        self.clear_add_entries()
        self.clear_info()

        car_id = self.treev.item(selected_item)['values'][1]
        cars = []

        with open(CAR_PATH, 'r') as f:
            cars = f.readlines()

        for i, car in enumerate(cars):
            car_json = eval(car)
            if car_json['car_id'] == car_id:
                with open(CAR_PATH, 'w') as f:
                    f.writelines(cars[:i] + cars[i+1:])
        self.treev.delete(selected_item)

    def change_click(self):
        license_plate = self.license_plate_entry.get()
        brand = self.brand_entry.get()
        model = self.model_entry.get()
        seats = self.seats_entry.get()
        engine_num = self.engine_num_entry.get()
        chassis_num = self.chassis_num_entry.get()
        import_day = self.import_entry.get()
        regist_dl = self.regist_dl_entry.get()
        travelled = self.travelled_entry.get()
        car_id = self.car_id_entry.get()
        driver_id = self.driver_id_entry.get()

        selected_item = self.treev.selection()
        car_id = self.treev.item(selected_item)['values'][1]
        cars = []

        with open(CAR_PATH, 'r', encoding='utf-8') as file:
            data = file.readlines()

        with open(CAR_PATH, 'r') as f:
            cars = f.readlines()

        new_data = {
            'car_id': car_id, 
            'driver_id' : driver_id, 
            'license_plate' : license_plate, 
            'brand' : brand, 
            'model' : model, 
            'seats' : seats, 
            'engine_num' : engine_num, 
            'chassis_num' : chassis_num, 
            'import_day' : import_day, 
            'regist_dl':regist_dl, 
            'travelled':travelled,}

        for i, car in enumerate(cars):
            car_json = eval(car)
            if car_json['car_id'] == car_id:
                data[i] = str(new_data) + '\n'
        with open(CAR_PATH, 'w', encoding='utf-8') as file:
            file.writelines(data)
    
    def search_click(self):
        query = self.search_entry.get()
        selections = []
        for child in self.treev.get_children():
            if query.lower() in self.treev.item(child)['values'][0].lower():  
                selections.append(child)
        self.treev.selection_set(selections)

    def check_existence(self, driver_id, car_id):
        existing_driver_id_list = list()
        existing_car_id_list = list()
        data_file = open(CAR_PATH, 'r')
        if os.path.getsize(CAR_PATH) != 0:
            for driver_info in data_file:
                car_json = eval(driver_info)
                existing_driver_id_list.append(car_json['driver_id'])
                existing_car_id_list.append(car_json['car_id'])
            if driver_id in existing_driver_id_list:
                return 1
            elif car_id in existing_car_id_list:
                return 2
            else:
                return 0
        elif os.path.getsize(CAR_PATH) == 0:
            return 0

        


        