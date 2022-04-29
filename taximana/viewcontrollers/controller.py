import tkinter as tk
from taximana.constant import *
from taximana.viewcontrollers.signin import SignInController
from taximana.viewcontrollers.signup import SignUpController
from taximana.viewcontrollers.dashboard import DashBoard
from taximana.viewcontrollers.car import Car
from taximana.viewcontrollers.income import Income
from taximana.viewcontrollers.driver import Driver
from taximana.viewcontrollers.expense import Expense
from taximana.viewcontrollers.summary import Summary

class Root(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (SignInController, SignUpController, DashBoard, Car, Driver, Income, Expense, Summary):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("SignInController")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()

