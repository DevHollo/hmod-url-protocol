from hollosmodule import hexdecimals, Exceptions
import webbrowser as web
from tkinter import ttk
import requests as rq
import tkinter as tk
import sys
import os

e = Exceptions()

class App:
    def __init__(self, *, master: tk.Tk, geometry: list[int, int]):
        self.root = master
        self.WINDOW_W = geometry[0]
        self.WINDOW_H = geometry[1]
        self.get_icon()
    
    def init(self):
        self.root.title("hmod help")
        self.root.geometry(f"{self.WINDOW_W}x{self.WINDOW_H}")
        self.root.protocol('WM_DELETE_WINDOW', self.on_close)

        tk.Label(self.root, text="About hmod://", font=('Arial 20 bold')).pack()

        ttk.Button(self.root, text="Code Source", command=self.code_source).pack(pady=20)

        ttk.Button(self.root, text="All Protocols", command=self.all_protocols).pack(pady=20)

    def compile_app(self, n: int = 0):
        self.root.mainloop(n)

    @staticmethod
    def gethex():
        print(hexdecimals('list', 500))

    def get_icon(self):
        res = rq.get('https://devhollo.github.io/!assets/urls/main/img/hmod_icon.ico')
        if res.status_code == 200:
            with open("icon.temp.ico", "wb") as f:
                f.write(res.content)
            self.root.iconbitmap("icon.temp.ico")
            os.remove('./icon.temp.ico')
        else:
            raise e.ConnectionError("Failed to fetch icon")
    
    def on_close(self):
        root.destroy()
        sys.exit()
    
    @staticmethod
    def code_source():
        web.open_new_tab('https://github.com/DevHollo/hmod-url-protocol/tree/main/src')
    
    @staticmethod
    def all_protocols():
        web.open_new_tab("https://raw.githubusercontent.com/DevHollo/hmod-url-protocol/main/protocols.txt")


if __name__ == "__main__":
    root = tk.Tk()
    app = App(
        master=root,
        geometry=[500, 500]
    )
    app.init()
    app.compile_app()