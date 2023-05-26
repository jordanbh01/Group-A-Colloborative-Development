"""
CMP 304
"""
# Imports
import tkinter as tk
from tkinter import ttk
from class_config import GUI


class App(GUI):
    app_gui = tk.Tk()
    title = 'CPS Property Management'
    app_size = ''
    app_frame = ttk.Frame(app_gui)
    style = 'AccentButton'

    def app(self):
        self.app_gui.geometry(self.app_size)
        self.app_gui.title(self.title)
        self.app_gui.iconbitmap()
        style = ttk.Style(self.app_gui)
        self.app_gui.tk.call('source', 'proxttk-dark.tcl')
        style.theme_use(self.theme)
        # Creating frame
        self.app_frame.grid(sticky=self.sticky)
        self.app_frame.columnconfigure(0, weight=1)
        login_btn = ttk.Button(self.app_frame, text="Login", style=self.style, padding=self.padding,
                               command=lambda: my_app.login())
        login_btn.grid(row=2, column=2, sticky=self.sticky)

        self.app_gui.mainloop()

    def login(self):
        login_screen = tk.Toplevel(self.app_gui)
        login_screen.title("Login")
        # username_entry =
        # password_entry =
        authenticate_btn = ttk.Button(self.app_frame, text='Authenticate', style=self.style, padding=self.padding)

    def authenticate(self):




my_app = App()  

if __name__ == '__main__':
    my_app.app()
