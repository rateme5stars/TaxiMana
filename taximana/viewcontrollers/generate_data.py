import uuid
import pandas as pd 
import numpy as np 
from datetime import timedelta, date
import random
import string
import json
from pathlib import Path
from taximana.constant import *

def fake_id():
    id_list = list()
    for _ in range(500):
        my_id = str(uuid.uuid1())
        my_id = my_id[:8]
        id_list.append(my_id)
    return id_list

id_list = fake_id()

class DriverData:
    def __init__(self):
        self.dates = self.fake_date()
        self.names = self.fake_name()
        self.dob = self.fake_dob()
        self.edu_lv_list = self.fake_edu()
        self.phone_numbers = self.fake_num()
        self.kind_list = self.fake_kinds()
        self.opcost = self.fake_opcost()

        self.driver_df_list = list()
        for d in self.dates:
            report_list = self.reported()
            km = self.km_run()
            driver_df = pd.DataFrame({
            'date' : [d] * 500,
            'name' : self.names,
            'id' : id_list,
            'dob' : self.dob,
            'edu_lv' : self.edu_lv_list,
            'phone' : self.phone_numbers,
            'kind' : self.kind_list,
            'reported' : report_list,
            'km_run' :km,
            'income' : km * 11000,
            'opcost' : self.opcost,
            'salary' : [20000000] * 500,
            'profit' : km * 11000 ,
            'accept' : np.random.randint(15, 25, 500),
            'cancel' : np.random.randint(0, 3, 500),
            })
            driver_df['salary'] = 0.4 * driver_df['income'].where(driver_df['kind'] == 'Co-Worker')
            driver_df = driver_df.fillna(20000000)
            driver_df['profit'] = driver_df['profit'] - driver_df['opcost'] - driver_df['salary']
            self.driver_df_list.append(driver_df)

    def fake_id(self):
        id_list = list()
        for _ in range(500):
            my_id = str(uuid.uuid1())
            my_id = my_id[:8]
            id_list.append(my_id)
        
        return id_list

    def fake_date(self):
        dates = pd.date_range('2021-02-01','2022-05-01' , freq='1M')-pd.offsets.MonthBegin(1)
        dates = [date.strftime("%d-%m-%Y") for date in dates]
        return dates

    def fake_name(self):
        names = list()
        first_name = ['Ngô', 'Nguyễn', 'Đặng', 'Phạm', 'Bùi', 'Cao', 'Trần', 'Lê', 'Đỗ', 'Hoàng', 'Phan', 'Vũ', 'Dương', 'Võ', 'Lý', 'Phan']

        last_name = ['Tài', 'Dũng', 'Dương', 'Lâm', 'Minh', 'Đức', 'Bách', 'Tuấn', 'Quyết', 'Nam', 'Bắc', 'Trung', 'Giang', 'Quân', 
                    'Linh', 'Huyền', 'Trường', 'Thọ', 'Kiệt', 'Đạt']
        for fn in first_name:
            for ln in last_name:
                n = fn + ' ' + ln
                names.append(n)
        names = names + names[:180]

        return names

    def fake_dob(self):
        dob = list()
        for _ in range(500):
            time_between_dates = date(2001, 1, 1) - date(1970, 1, 1)
            days_between_dates = time_between_dates.days
            random_number_of_days = random.randrange(days_between_dates)
            random_date = date(1970, 1, 1) + timedelta(days=random_number_of_days)

            dob.append(random_date.strftime("%d-%m-%Y"))

        return dob

    def fake_edu(self):
        edu_lv = [f'{i}/12' for i in range(9, 13)] + ['Cao Đẳng', 'Trung Cấp', 'Đại Học']
        random_edu_lv = np.random.randint(0, len(edu_lv), 500)
        edu_lv_list = [edu_lv[i] for i in random_edu_lv]

        return edu_lv_list

    def fake_num(self):
        phone_numbers = ['09' + str(number) for number in random.sample(range(10000000, 99999999), 500)]
        return phone_numbers

    def fake_kinds(self):
        kinds = ['Employee', 'Co-Worker']
        random_kind = np.random.randint(0, len(kinds), 500)
        kind_list = [kinds[i] for i in random_kind]

        return kind_list

    def fake_opcost(self):
        opcost = np.random.randint(5000, 6000, 500)
        opcost = opcost * 1000

        return opcost

    def reported(self):
        reported = ['Negative', 'Positive']
        random_report = np.random.randint(0, len(reported), 500)
        return [reported[i] for i in random_report]

    def km_run(self):
            return np.random.randint(100, 200, 500) * 30

    def save_data(self):
        last_month_df = self.driver_df_list[-1]
        for i in range(len(last_month_df)):
            
            d = {
                'id': str(last_month_df['id'][i]),
                'name' : str(last_month_df['name'][i]),
                'dob': str(last_month_df['dob'][i]),
                'edu_lv': str(last_month_df['edu_lv'][i]),
                'phone': str(last_month_df['phone'][i]),
                'type': str(last_month_df['kind'][i])
            }

            driver_json = json.dumps(d)
            driver_json_str = str(driver_json)
            if Path(DRIVER_PATH).is_file():
                    file = open(DRIVER_PATH, 'a')
                    file.write(f'{driver_json_str}\n')
                    file.close()
            else:
                file = open(DRIVER_PATH, 'w')
                file.write(f'{driver_json_str}\n')
                file.close()

        

class CarData:
    def __init__(self):
        driver = DriverData()
        self.plates = self.fake_plates()
        self.brand = 'Toyota'
        self.model = self.fake_model()
        self.engine_num = random.sample(range(10000000, 99999999), 500)
        self.chassis_num = random.sample(range(100000000, 999999999), 500)
        self.import_day = ['20-12-2018'] * 500
        self.regist_dl = ['10-10-2028'] * 500
        self.travel = 0
        for df in driver.driver_df_list:
            self.travel += df['km_run']
        
        self.car_df = pd.DataFrame({
            'id' : id_list,
            'plates' : self.plates,
            'brand' : self.brand,
            'model' : self.model,
            'engine_num' : self.engine_num,
            'chassis_num' : self.chassis_num,
            'import_day' : self.import_day,
            'regist_dl' : self.regist_dl,
            'travel' : self.travel,
            'seats' : ['4'] * 500
            })
        self.car_df['seats'] = np.where(self.car_df['model'] == 'Innova', '7', '4')
    def fake_plates(self):
        a = ['29', '30']
        alphabet_list = list(string.ascii_uppercase)
        b = np.random.randint(0, 2, 500)
        c = np.random.randint(0, len(alphabet_list), 500)
        d = np.random.randint(1, 10, 500)
        last_num = random.sample(range(10000, 99999), 500)

        first_num = [a[i] for i in b]
        first_cha = [alphabet_list[i] for i in c]
        plates = list()
        for i in range(500):
            license_plate = first_num[i] + first_cha[i] + str(d[i]) + '-' + str(last_num[i])
            plates.append(license_plate)
        return plates
        
    def fake_model(self):
        model = ['Vios', 'Innova']
        random_model = np.random.randint(0, len(model), 500)
        model_list = [model[i] for i in random_model]
        return model_list

    def save_data(self):
        last_month_df = self.car_df
        for i in range(len(last_month_df)):
            
            d = {
                'id': str(last_month_df['id'][i]),
                'license_plate': str(last_month_df['plates'][i]),
                'brand' : str(last_month_df['brand'][i]),
                'model': str(last_month_df['model'][i]),
                'seats': str(last_month_df['seats'][i]),
                'engine_num': str(last_month_df['engine_num'][i]),
                'chassis_num': str(last_month_df['chassis_num'][i]),
                'import_day': str(last_month_df['import_day'][i]),
                'regist_dl': str(last_month_df['regist_dl'][i]),
                'travelled': str(last_month_df['travel'][i])
            }

            driver_json = json.dumps(d)
            driver_json_str = str(driver_json)
            if Path(CAR_PATH).is_file():
                    file = open(CAR_PATH, 'a')
                    file.write(f'{driver_json_str}\n')
                    file.close()
            else:
                file = open(CAR_PATH, 'w')
                file.write(f'{driver_json_str}\n')
                file.close()