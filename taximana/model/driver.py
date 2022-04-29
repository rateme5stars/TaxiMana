class Driver:
    def __init__(self, name, sex, DoB, phone, driver_id, car_id, recruitment_day, days_off, km_run):
        self.name = name
        self.sex = sex 
        self.DoB = DoB
        self.phone = phone
        self.driver_id = driver_id
        self.car_id = car_id
        self.recruitment_day = recruitment_day
        self.days_off = days_off
        self.salary = km_run * 7000