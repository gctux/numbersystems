from tkinter import *
from tkhtmlview import HTMLLabel
from tkinter import ttk



# root = Tk()
# html_label = HTMLLabel(root, html='<h1 style="color: red; text-align: center"> Hello World </H1>')
# html_label.pack(fill="both", expand=True)
# html_label.fit_height()
# root.mainloop()



class Window(Toplevel):
    def __init__(self, parent):
        super().__init__(parent)

        self.geometry('300x100')
        self.title('Hilfe')
        html_label = HTMLLabel(self, html='<h1 style="color: red; text-align: center"> Hello World </H1>')
        html_label.pack(fill="both", expand=True)
        html_label.fit_height()
        ttk.Button(self,text='Close',command=self.destroy).pack()


class App(Tk):
    def __init__(self):
        super().__init__()

        self.geometry('300x200')
        self.title('Main Window')

        # place a button on the root window
        ttk.Button(self,
                text='Open a window',
                command=self.open_window).pack(expand=True)

    def open_window(self):
        window = Window(self)
        window.grab_set()


if __name__ == "__main__":
    app = App()
    app.mainloop()