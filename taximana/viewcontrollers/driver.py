import tkinter as tk
import os
from taximana.constant import *
from tkmacosx import Button
from datetime import date
import tkinter.ttk as ttk
from pathlib import Path
import json
from tkinter import messagebox

'''
#TODO:
- ID regex 
- Change unique value 
'''

class Driver(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='white')
        self.controller = controller
        self.controller.title("Driver")

        # Navigation Bar ======================================
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

        # Statistic Bar ===========================================
        stat_frame = tk.Frame(self, width=400, height=850, bg='#FFF5D2')
        stat_frame.place(x=250, y=0)

        # Stat Label 
        tk.Label(stat_frame, text='Statistic', bg='#FFF5D2', fg='black', font=(FONT, 22)).place(x=20, y=8)

        # Date
        tk.Label(stat_frame, text=f'Date: {date.today().strftime("%B %d, %Y")}', bg='#FFF5D2', fg='black', font=(FONT, 15)).place(x=20, y=55)

        # Income Label 
        tk.Label(stat_frame, text='Employee', bg='#FFF5D2', fg='black', font=(FONT, 17)).place(x=60, y=100)
        tk.Label(stat_frame, text='123/150', bg='#FFF5D2', fg='black', font=(FONT, 14)).place(x=60, y=135)

        tk.Label(stat_frame, text='Late', bg='#FFF5D2', fg='black', font=(FONT, 17)).place(x=270, y=100)
        tk.Label(stat_frame, text='123', bg='#FFF5D2', fg='black', font=(FONT, 14)).place(x=270, y=135)

        tk.Label(stat_frame, text='Co-Worker', bg='#FFF5D2', fg='black', font=(FONT, 17)).place(x=60, y=180)
        tk.Label(stat_frame, text='30/100', bg='#FFF5D2', fg='black', font=(FONT, 14)).place(x=60, y=215)

        tk.Label(stat_frame, text='Report', bg='#FFF5D2', fg='black', font=(FONT, 17)).place(x=270, y=180)
        tk.Label(stat_frame, text='123', bg='#FFF5D2', fg='black', font=(FONT, 14)).place(x=270, y=215)

        # TreeView
        self.treev = ttk.Treeview(stat_frame, select='browse')
        self.treev.place(x=0, y=251)
        verscrlbar = tk.Scrollbar(stat_frame, orient='vertical', command=self.treev.yview)
        self.treev.configure(xscrollcommand=verscrlbar.set)
        self.treev['columns'] = ('1', '2', '3')
        self.treev['show'] = 'headings'
        self.treev.column('1', width=240, anchor='c')
        self.treev.column('2', width=80, anchor='c')
        self.treev.column('3', width=80, anchor='c')
        self.treev.heading('1', text='Name')
        self.treev.heading('2', text='ID')
        self.treev.heading('3', text='Car ID')
        self.treev.bind("<<TreeviewSelect>>", self.treeview_click)
        self.load_table()

        tk.Label(stat_frame,text='Name:', bg='#FFF5D2', fg='black', font=(FONT, 12)).place(x=10, y=480)
        self.name_entry = tk.Entry(stat_frame, highlightthickness=3, border=0, width=25, fg='black', bg='#FFF5D2', font=(FONT, 12))
        self.name_entry.config(highlightbackground='#FFF5D2', highlightcolor='#FFF5D2')
        self.name_entry.place(x=50, y=480)
        tk.Frame(stat_frame,width=252, height=1, bg='black').place(x=53, y=505)

        tk.Label(stat_frame,text='ID:', bg='#FFF5D2', fg='black', font=(FONT, 12)).place(x=10, y=520)
        self.id_entry = tk.Entry(stat_frame, highlightthickness=3, border=0, width=25, fg='black', bg='#FFF5D2', font=(FONT, 12))
        self.id_entry.config(highlightbackground='#FFF5D2', highlightcolor='#FFF5D2')
        self.id_entry.place(x=50, y=520)
        tk.Frame(stat_frame,width=252, height=1, bg='black').place(x=53, y=545)

        tk.Label(stat_frame,text='DoB:', bg='#FFF5D2', fg='black', font=(FONT, 12)).place(x=10, y=560)
        self.dob_entry = tk.Entry(stat_frame, highlightthickness=3, border=0, width=25, fg='black', bg='#FFF5D2', font=(FONT, 12))
        self.dob_entry.config(highlightbackground='#FFF5D2', highlightcolor='#FFF5D2')
        self.dob_entry.place(x=50, y=560)
        tk.Frame(stat_frame,width=252, height=1, bg='black').place(x=53, y=585)
        
        tk.Label(stat_frame,text='Edu Level:', bg='#FFF5D2', fg='black', font=(FONT, 12)).place(x=10, y=600)
        self.edu_entry = tk.Entry(stat_frame, highlightthickness=3, border=0, width=25, fg='black', bg='#FFF5D2', font=(FONT, 12))
        self.edu_entry.config(highlightbackground='#FFF5D2', highlightcolor='#FFF5D2')
        self.edu_entry.place(x=80, y=600)
        tk.Frame(stat_frame,width=223, height=1, bg='black').place(x=83, y=625)

        tk.Label(stat_frame,text='Phone:', bg='#FFF5D2', fg='black', font=(FONT, 12)).place(x=10, y=640)
        self.phone_entry = tk.Entry(stat_frame, highlightthickness=3, border=0, width=25, fg='black', bg='#FFF5D2', font=(FONT, 12))
        self.phone_entry.config(highlightbackground='#FFF5D2', highlightcolor='#FFF5D2')
        self.phone_entry.place(x=55, y=640)
        tk.Frame(stat_frame,width=248, height=1, bg='black').place(x=58, y=665)
        
        tk.Label(stat_frame,text='CarID:', bg='#FFF5D2', fg='black', font=(FONT, 12)).place(x=10, y=680)
        self.car_id_entry = tk.Entry(stat_frame, highlightthickness=3, border=0, width=25, fg='black', bg='#FFF5D2', font=(FONT, 12))
        self.car_id_entry.config(highlightbackground='#FFF5D2', highlightcolor='#FFF5D2')
        self.car_id_entry.place(x=50, y=680)
        tk.Frame(stat_frame,width=252, height=1, bg='black').place(x=53, y=705)

        tk.Label(stat_frame,text='Type:', bg='#FFF5D2', fg='black', font=(FONT, 12)).place(x=10, y=720)
        self.type_entry = tk.Entry(stat_frame, highlightthickness=3, border=0, width=25, fg='black', bg='#FFF5D2', font=(FONT, 12))
        self.type_entry.config(highlightbackground='#FFF5D2', highlightcolor='#FFF5D2')
        self.type_entry.place(x=50, y=720)
        tk.Frame(stat_frame,width=252, height=1, bg='black').place(x=53, y=745)

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

        # Vertical Line 
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

        tk.Label(self, text='Driver Details', bg='white', fg='black', font=(FONT, 22)).place(x=700, y=230)
        img = tk.PhotoImage(file='taximana/asset/driver.png')
        logo = tk.Label(self, image=img, bg='white', width=160, height=110)
        logo.place(x=670, y=280)
        logo.image = img

        # Label
        tk.Label(self, text="Name:", bg='white', fg='black', font=(FONT, 16)).place(x=700, y=400)
        tk.Label(self, text="ID:", bg='white', fg='black', font=(FONT, 16)).place(x=700, y=450)
        tk.Label(self, text="DoB:", bg='white', fg='black', font=(FONT, 16)).place(x=700, y=500)        
        tk.Label(self, text="Education Level:", bg='white', fg='black', font=(FONT, 16)).place(x=700, y=550)    
        tk.Label(self, text="Phone:", bg='white', fg='black', font=(FONT, 16)).place(x=700, y=600)
        tk.Label(self, text="Car ID:", bg='white', fg='black', font=(FONT, 16)).place(x=700, y=650)
        tk.Label(self, text="Type:", bg='white', fg='black', font=(FONT, 16)).place(x=700, y=700)

        # Search 
        tk.Label(self,text='Search:', bg='white', fg='black', font=(FONT, 16)).place(x=700, y=750)
        self.search_entry = tk.Entry(self, highlightthickness=3, border=0, width=25, fg='black', bg='white', font=(FONT, 14))
        self.search_entry.config(highlightbackground='white', highlightcolor='white')
        self.search_entry.place(x=765, y=750)
        tk.Frame(self,width=232, height=1, bg='black').place(x=765, y=775)

        # Search Button
        search_bt = Button(self, width=50, pady=6, text='Search',fg='black', bg="white",font=(FONT, 10), borderless=1, command=self.search_click)
        search_bt.place(x=1025, y=750)

        clear_search_bt = Button(self, width=50, pady=6, text='Clear',fg='black', bg="white",font=(FONT, 10), borderless=1, command=lambda:self.search_entry.delete(0, tk.END))
        clear_search_bt.place(x=1100, y=750)

        # Handle Click
        dashboard.bind("<Button-1>", lambda e: controller.show_frame('DashBoard'))
        driver.bind("<Button-1>", lambda e: controller.show_frame('Driver'))
        car.bind("<Button-1>", lambda e: controller.show_frame('Car'))
        income.bind("<Button-1>", lambda e: controller.show_frame('Income'))
        expense.bind("<Button-1>", lambda e: controller.show_frame('Expense'))
        summary.bind("<Button-1>", lambda e: controller.show_frame('Summary'))
    
    def entry(self, parent_frame, entry_x, entry_y, line_x, line_y, line_w):
        self.my_entry = tk.Entry(parent_frame, highlightthickness=3, border=0, width=25, fg='black', bg='#FFF5D2', font=(FONT, 12))
        self.my_entry.config(highlightbackground='#FFF5D2', highlightcolor='#FFF5D2')
        self.value = self.my_entry.get()
        self.my_entry.place(x=entry_x, y=entry_y)
        tk.Frame(parent_frame,width=line_w, height=1, bg='black').place(x=line_x, y=line_y)

    def load_table(self):
        data_file = open(DRIVER_PATH, 'r')
        if data_file is not None:
            for driver_info in data_file:
                driver_json = eval(driver_info)
                self.treev.insert("", 'end', text=f'driver', values=(driver_json['name'], driver_json['id'], driver_json['car_id']))
            
    def treeview_click(self, *arg):
        cur_item = self.treev.focus()
        driver_id = self.treev.item(cur_item)['values'][1]
        data_file = open(DRIVER_PATH, 'r')
        for driver_info in data_file:
            driver_json = eval(driver_info)
            tmp = {driver_json['id'] : [driver_json['name'], driver_json['dob'], driver_json['car_id'], 
            driver_json['edu_lv'], driver_json['phone'], driver_json['type'],]}
            for key, value in tmp.items():
                if key == driver_id:
                    self.show_info(value[0], driver_id, value[1], value[2], value[3], value[4], value[5])
                    self.show_in_entry(value[0], driver_id, value[1], value[2], value[3], value[4], value[5])
                    
    def add_click(self):
        name = self.name_entry.get()
        driver_id = self.id_entry.get()
        dob = self.dob_entry.get()
        car_id = self.car_id_entry.get()
        edu = self.edu_entry.get()
        phone = self.phone_entry.get()
        driver_type = self.type_entry.get()

        driver = {
            'id': driver_id,
            'name' : name,
            'dob': dob,
            'car_id': car_id,
            'edu_lv': edu,
            'phone': phone,
            'type': driver_type
        }

        driver_json = json.dumps(driver)
        driver_json_str = str(driver_json)
        if Path(DRIVER_PATH).is_file():
            condition = self.check_existence(driver_id, car_id, phone)
            if condition == 1:
                messagebox.showerror('Invalid','Driver ID already exist')
            elif condition == 2:
                messagebox.showerror('Invalid','Car ID already exist')
            elif condition == 3:
                messagebox.showerror('Invalid','Phone number already exist')
            elif condition == 0:
                self.treev.insert("", 'end', text=f'driver', values=(name, driver_id, car_id))
                file = open(DRIVER_PATH, 'a')
                file.write(f'{driver_json_str}\n')
                file.close()
                self.show_info(name, driver_id, dob, edu, phone, car_id, driver_type)
                self.clear_add_entries()
            
        else:
            self.treev.insert("", 'end', text=f'driver', values=(name, driver_id, car_id))
            file = open(DRIVER_PATH, 'w')
            file.write(f'{driver_json_str}\n')
            file.close()
            self.show_info()
            self.clear_add_entries()
            
    def clear_add_entries(self):
        self.name_entry.delete(0, tk.END)
        self.id_entry.delete(0, tk.END)
        self.dob_entry.delete(0, tk.END)
        self.car_id_entry.delete(0, tk.END)
        self.edu_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.type_entry.delete(0, tk.END)

    def show_in_entry(self, name, driver_id, dob, edu, phone, car_id, driver_type):
        self.clear_add_entries()
        self.name_entry.insert(0, name)
        self.id_entry.insert(0, driver_id)
        self.dob_entry.insert(0, dob)
        self.car_id_entry.insert(0, edu)
        self.edu_entry.insert(0, phone)
        self.phone_entry.insert(0, car_id)
        self.type_entry.insert(0, driver_type)
        
    def show_info(self, name, driver_id, dob, edu, phone, car_id, driver_type):
        tk.Frame(self, bg='white', width=380, height=30).place(x=755, y=397)
        tk.Frame(self, bg='white', width=380, height=30).place(x=735, y=447)
        tk.Frame(self, bg='white', width=380, height=30).place(x=745, y=497)
        tk.Frame(self, bg='white', width=350, height=30).place(x=830, y=547)
        tk.Frame(self, bg='white', width=380, height=30).place(x=760, y=597)
        tk.Frame(self, bg='white', width=380, height=30).place(x=760, y=647)
        tk.Frame(self, bg='white', width=380, height=30).place(x=755, y=697)
        tk.Label(self, text=name, bg='white', fg='black', font=(FONT, 16)).place(x=760, y=400)
        tk.Label(self, text=driver_id, bg='white', fg='black', font=(FONT, 16)).place(x=740, y=450)
        tk.Label(self, text=dob, bg='white', fg='black', font=(FONT, 16)).place(x=750, y=500)        
        tk.Label(self, text=edu, bg='white', fg='black', font=(FONT, 16)).place(x=835, y=550)    
        tk.Label(self, text=phone, bg='white', fg='black', font=(FONT, 16)).place(x=765, y=600)
        tk.Label(self, text=car_id, bg='white', fg='black', font=(FONT, 16)).place(x=765, y=650)
        tk.Label(self, text=driver_type, bg='white', fg='black', font=(FONT, 16)).place(x=760, y=700)

    def check_existence(self, driver_id, car_id, phone_num):
        existing_driver_id_list = list()
        existing_car_id_list = list()
        existing_phone_list = list()
        data_file = open(DRIVER_PATH, 'r')
        if os.path.getsize(DRIVER_PATH) != 0:
            for driver_info in data_file:
                driver_json = eval(driver_info)
                existing_driver_id_list.append(driver_json['id'])
                existing_car_id_list.append(driver_json['car_id'])
                existing_phone_list.append(driver_json['phone'])
            if driver_id in existing_driver_id_list:
                return 1
            elif car_id in existing_car_id_list:
                return 2
            elif phone_num in existing_phone_list:
                return 3
            else:
                return 0
        elif os.path.getsize(DRIVER_PATH) == 0:
            return 0
        
    def remove_click(self):
        selected_item = self.treev.selection()
        self.clear_add_entries()
        self.clear_info()

        driver_id = self.treev.item(selected_item)['values'][1]
        drivers = []

        with open(DRIVER_PATH, 'r') as f:
            drivers = f.readlines()

        for i, driver in enumerate(drivers):
            driver_json = eval(driver)
            if driver_json['id'] == driver_id:
                with open(DRIVER_PATH, 'w') as f:
                    f.writelines(drivers[:i] + drivers[i+1:])
        self.treev.delete(selected_item)
        
    def clear_info(self):
        tk.Frame(self, bg='white', width=380, height=30).place(x=755, y=397)
        tk.Frame(self, bg='white', width=380, height=30).place(x=735, y=447)
        tk.Frame(self, bg='white', width=380, height=30).place(x=745, y=497)
        tk.Frame(self, bg='white', width=350, height=30).place(x=830, y=547)
        tk.Frame(self, bg='white', width=380, height=30).place(x=760, y=597)
        tk.Frame(self, bg='white', width=380, height=30).place(x=760, y=647)
        tk.Frame(self, bg='white', width=380, height=30).place(x=755, y=697)

    def change_click(self):
        name = self.name_entry.get()
        driver_id = self.id_entry.get()
        dob = self.dob_entry.get()
        car_id = self.car_id_entry.get()
        edu = self.edu_entry.get()
        phone = self.phone_entry.get()
        driver_type = self.type_entry.get()

        selected_item = self.treev.selection()
        driver_id = self.treev.item(selected_item)['values'][1]
        drivers = []

        with open(DRIVER_PATH, 'r', encoding='utf-8') as file:
            data = file.readlines()

        with open(DRIVER_PATH, 'r') as f:
            drivers = f.readlines()

        new_data = {"id": driver_id, "name": name, "dob": dob, "car_id": car_id, "edu_lv": edu, "phone": phone, "type": driver_type}
        for i, driver in enumerate(drivers):
            driver_json = eval(driver)
            if driver_json['id'] == driver_id:
                data[i] = str(new_data) + '\n'
                
        with open(DRIVER_PATH, 'w', encoding='utf-8') as file:
            file.writelines(data)
    
    def search_click(self):
        query = self.search_entry.get()
        selections = []
        for child in self.treev.get_children():
            if query.lower() in self.treev.item(child)['values'][0].lower():   # compare strings in  lower cases.
                print(self.treev.item(child)['values'])
                selections.append(child)
        print('search completed')
        self.treev.selection_set(selections)