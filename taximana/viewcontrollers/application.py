from rootcontroller.root_controller import Root

def run_application():
    app = Root()
    sc_width = app.winfo_screenwidth()
    sc_height = app.winfo_screenheight()
    app_width = 1100
    app_height = 600
    x = int((sc_width/2) - (app_width/2))
    y = int((sc_height/2) - (app_height/2))
    app.geometry(f'{app_width}x{app_height}+{x}+{y}')
    app.resizable(False, False)
    app.mainloop()

if __name__ == "__main__":
    run_application()