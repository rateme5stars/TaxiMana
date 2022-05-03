from controller import Root
from taximana.viewcontrollers.generate_data import (DriverData, CarData)


def run_application():
    driver = DriverData()
    car = CarData()
    driver.save_data()
    car.save_data()
    app = Root()
    sc_width = app.winfo_screenwidth()
    sc_height = app.winfo_screenheight()
    app_width = 1200
    app_height = 800
    x = int((sc_width/2) - (app_width/2))
    y = int((sc_height/2) - (app_height/2))
    app.geometry(f'{app_width}x{app_height}+{x}+{y}')
    app.resizable(False, False)
    app.mainloop()

if __name__ == "__main__":
    run_application()