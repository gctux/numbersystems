from tkinter import *
from tkinter.scrolledtext import *
from tkinter import ttk
from tkinter import font
from tkinter import messagebox
from tkinter import filedialog
from pathlib import Path
from tkhtmlview import HTMLScrolledText
import hashlib
import sys, random, time



class AboutWindow(Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.html = '''
            <h3 style=" text-align: center">Zahlsysteme umrechnen!</h3>
            <p style=" text-align: center">Version 0.1</p>
            <p style=" text-align: center">&copy; Lutz Herrmann <br> Georgius-Agricola-Gymnasium Glauchau <br> 2022 bis 2023</p>
            <p style=" text-align: center"> Dieses Programm kommt OHNE JEDWEDE GARANTIE. </p>
            <p style=" text-align: center"> <a href='https://www.gnu.org/licenses/gpl-3.0.de.html'>GNU General Public License, Version 3 oder neuer</a> </p>
            <p style=" text-align: center">Projektseite: <a href = 'https://github.com/gctux/numbersystems'>https://github.com/gctux/numbersystems</a></p>
            
        '''
        self.geometry('600x400')
        self.title('About')
        self.html_label = HTMLScrolledText(self, html=self.html)
        self.html_label.pack(fill="both", expand=True)
        

class HelpWindow(Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.html = '''
            <h3 style=" text-align: center">Programmhilfe</h3>
            <p>Zahlsysteme ist ein kleines Pythonprogramm, mit dem man das Umrechnen von Zahlen zwischen dem Dezimalsystem, dem Dualsystem und dem Hexadezimalsystem trinieren kann. Insgesamt</p>
            <p style=" text-align: center"><img width='600' height='300' src='https://raw.githubusercontent.com/gctux/numbersystems/main/images/picture01.png'></p>
        '''
        self.geometry('800x400')
        self.title('Programmhilfe')
        self.html_label = HTMLScrolledText(self, html=self.html)
        self.html_label.pack(fill="both", expand=True)



class Application(Tk):

    def __init__(self):
        super().__init__()
        self.numbers = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.actual = 0
        self.t1=time.time()
        self.t2=time.time()

        self.title("Zahlsysteme")
        self.geometry("800x400")
        self.minsize(400, 300)
        self.menubar = Menu(self)
        self.mDatei = Menu(self.menubar)
        self.mDatei.add_command(label="Speichern unter", command=self.saveResult)
        self.mDatei.add_command(label="Datei testen", command=self.testResult)
        self.mDatei.add_command(label="Ende", command=self.quitApp)
        self.menubar.add_cascade(label = "Datei", menu = self.mDatei)
        self.mHilfe = Menu(self.menubar)
#        self.mHilfe.add_command(label="Hilfe", command=self.open_help)
        self.mHilfe.add_command(label="Über", command=self.open_about)
        self.menubar.add_cascade(label = "Hilfemenü", menu = self.mHilfe)
        self["menu"] = self.menubar

        #self.createStyles()

        #self.grid_rowconfigure(0, weight=1)
        #self.grid_columnconfigure((0, 1, 2, 3), weight=1)

        self.droOptions1 = ("Bitte Aufgabentyp auswählen!","Dual → Dezimal", "Dezimal → Dual", 
        "Hexadezimal → Dezimal", "Dezimal → Hexadezimal", "Dual → Hexadezimal", "Hexadezimal → Dual")
        self.v = StringVar()
        self.v.set(self.droOptions1[0])
        self.drop1 = ttk.OptionMenu(self, self.v, *self.droOptions1)
        self.drop1.grid(row=0,column=0, padx=5, pady=5, sticky="ew")


        self.buAe = ttk.Button(self, text="Aufgaben erstellen", width=20, command=self.createCalculatien)
        self.buAe.grid(row=0, column=1, padx=5, pady=5, sticky="ew")
        self.buAu = ttk.Button(self, text="Auswerten", width=15, command=self.evaluate)
        self.buAu.grid(row=0,column=2, padx=5, pady=5, sticky="ew")

        #self.buLe = ttk.Button(self, text="Alles leeren", width=12, command=self.deleteAll)
        #self.buLe['style'] = 'Emergency.TButton'
        #self.buLe.grid(row=0, column=3, padx=5, pady=5, sticky="ew")
        
        self.droOptions2 = ("Zeitnahme","Ohne Zeitnahme!", "Mit Zeitnahme!")
        self.w = StringVar()
        self.w.set(self.droOptions2[0])
        self.drop2 = ttk.OptionMenu(self, self.w, *self.droOptions2)
        self.drop2.grid(row=0,column=3, padx=5, pady=5, sticky="ew")

        self.f1 = ttk.Frame(self)
        self.f1.grid(row=1, column=0, padx=5, pady=5, sticky="nsew")
        self.calculations = []
        self.results = []
        for i in range(10):
            self.calculations.append(ttk.Label(self.f1, text="Aufgabe "+str(i+1)+" ", width=15, anchor=E))
            self.calculations[i].grid(row=i, column=0, padx=5, pady=5, sticky="ew")
            self.results.append(ttk.Entry(self.f1, width=20))
            self.results[i].grid(row=i, column=1, padx=5, pady=5, sticky="ew")

        self.t = Text(self, width=50, height=15, state='disabled')
        self.t.grid(row=1, column=1, columnspan=3, padx=5, pady=5, sticky="nsew")

        self.bind('<Return>',self.evaluate)

    #def createStyles(self):
    #    self.f = font.nametofont('TkTextFont')
    #    self.buttonstyle1 = ttk.Style()
    #    self.buttonstyle1.configure('Emergency.TButton', foreground='darkred', \
    #        font = (self.f.actual()["family"], self.f.actual()["size"],'bold'))


    def quitApp(self):
        self.quit()
        self.destroy()
        sys.exit(0)

    def createCalculatien(self):
        if self.w.get() == "Mit Zeitnahme!":
            self.t1=time.time()
        if self.v.get() == "Bitte Aufgabentyp auswählen!":
            messagebox.showinfo('information', 'Bitte Aufgabentyp auswählen!')
        elif self.v.get() == "Dual → Dezimal":
            self.deleteAll()
            for i in range(10):
                self.numbers[i]=random.randint(0,255)
                self.calculations[i]["text"] = str(bin(self.numbers[i]))[2:]+" = "
                self.actual = 1
        elif self.v.get() == "Dezimal → Dual":
            self.deleteAll()
            for i in range(10):
                self.numbers[i]=random.randint(0,255)
                self.calculations[i]["text"] = str(self.numbers[i]) + " = "
                self.actual = 2
        elif self.v.get() == "Hexadezimal → Dezimal":
            self.deleteAll()
            for i in range(10):
                self.numbers[i]=random.randint(0,255)
                self.calculations[i]["text"] = str(hex(self.numbers[i]))[2:].upper()+" = "
                self.actual = 3
        elif self.v.get() == "Dezimal → Hexadezimal":
            self.deleteAll()
            for i in range(10):
                self.numbers[i]=random.randint(0,255)
                self.calculations[i]["text"] = str(self.numbers[i]) + " = "
                self.actual = 4
        elif self.v.get() == "Dual → Hexadezimal":
            self.deleteAll()
            for i in range(10):
                self.numbers[i]=random.randint(0,4095)
                self.z = ''
                for j in range(len(str(bin(self.numbers[i]))[2:])):
                    if ((len(str(bin(self.numbers[i]))[2:]))-j) % 4 == 0:
                        self.z += " "
                    self.z += str(bin(self.numbers[i]))[2:][j]
                self.calculations[i]["text"] = self.z + " = "
                self.actual = 5
        elif self.v.get() == "Hexadezimal → Dual":
            self.deleteAll()
            for i in range(10):
                self.numbers[i]=random.randint(0,4095)
                self.calculations[i]["text"] = str(hex(self.numbers[i]))[2:].upper()+" = "
                self.actual = 6     

    def evaluate(self, event=None):
        if self.w.get() == "Mit Zeitnahme!":
            self.t2=time.time()
        if self.actual == 0:
            messagebox.showinfo('information', 'Bitte einen Aufgabentyp auswählen und die Aufgaben neu erzeugen!')
        elif self.actual == 1:
            self.t.configure(state='normal')
            self.t.delete(0.0,"end")
            self.t.insert("end","Umwandlung von Dualzahlen in Dezimalzahlen\n")
            self.t.insert("end","Auswertung um " + time.strftime("%d.%m.%Y %H:%M:%S") +"\n")
            for i in range(10):
                try:
                    if self.numbers[i]==int(self.results[i].get()):
                        self.t.insert("end","Deine Eingabe: "+self.results[i].get()+" Richtig!\n")
                    else:
                        self.t.insert("end","Deine Eingabe: "+self.results[i].get()+" Falsch! Richtige Lösung: "+str(self.numbers[i])+"\n")
                except:
                    self.t.insert("end","Deine Eingabe war keine Zahl! \n")
            self.t.insert("end","\n\n")
            self.t.configure(state='disabled')
            self.actual = 0
        elif self.actual == 2:
            self.t.configure(state='normal')
            self.t.delete(0.0,"end")
            self.t.insert("end","Umwandlung von Dezimalzahlen in Dualzahlen\n")
            self.t.insert("end","Auswertung um " + time.strftime("%d.%m.%Y %H:%M:%S") +"\n")
            for i in range(10):
                try:
                    if self.numbers[i]==int(self.results[i].get(),2):
                        self.t.insert("end","Deine Eingabe: "+self.results[i].get()+" Richtig!\n")
                    else:
                        self.t.insert("end","Deine Eingabe: "+self.results[i].get()+" Falsch! Richtige Lösung: "+str(bin(self.numbers[i]))[2:]+"\n")
                except:
                    self.t.insert("end","Deine Eingabe war keine Zahl! \n")
            self.t.insert("end","\n\n")
            self.t.configure(state='disabled')
            self.actual = 0
        elif self.actual == 3:
            self.t.configure(state='normal')
            self.t.delete(0.0,"end")
            self.t.insert("end","Umwandlung von Hexadezimalzahlen in Dezimalzahlen\n")
            self.t.insert("end","Auswertung um " + time.strftime("%d.%m.%Y %H:%M:%S") +"\n")
            for i in range(10):
                try:
                    if self.numbers[i]==int(self.results[i].get()):
                        self.t.insert("end","Deine Eingabe: "+self.results[i].get()+" Richtig!\n")
                    else:
                        self.t.insert("end","Deine Eingabe: "+self.results[i].get()+" Falsch! Richtige Lösung: "+str(self.numbers[i])+"\n")
                except:
                    self.t.insert("end","Deine Eingabe war keine Zahl! \n")
            self.t.insert("end","\n\n")
            self.t.configure(state='disabled')
            self.actual = 0
        elif self.actual == 4:
            self.t.configure(state='normal')
            self.t.delete(0.0,"end")
            self.t.insert("end","Umwandlung von Dezimalzahlen in Hexadezimalzahlen\n")
            self.t.insert("end","Auswertung um " + time.strftime("%d.%m.%Y %H:%M:%S") +"\n")
            for i in range(10):
                try:
                    if self.numbers[i]==int(self.results[i].get(),16):
                        self.t.insert("end","Deine Eingabe: "+self.results[i].get().upper()+" Richtig!\n")
                    else:
                        self.t.insert("end","Deine Eingabe: "+self.results[i].get()+" Falsch! Richtige Lösung: "+str(hex(self.numbers[i]))[2:].upper()+"\n")
                except:
                    self.t.insert("end","Deine Eingabe war keine Zahl! \n")
            self.t.insert("end","\n\n")
            self.t.configure(state='disabled')
            self.actual = 0
        elif self.actual == 5:
            self.t.configure(state='normal')
            self.t.delete(0.0,"end")
            self.t.insert("end","Umwandlung von Dualzahlen in Hexadezimalzahlen\n")
            self.t.insert("end","Auswertung um " + time.strftime("%d.%m.%Y %H:%M:%S") +"\n")
            for i in range(10):
                try:
                    if self.numbers[i]==int(self.results[i].get(),16):
                        self.t.insert("end","Deine Eingabe: "+self.results[i].get().upper()+" Richtig!\n")
                    else:
                        self.t.insert("end","Deine Eingabe: "+self.results[i].get()+" Falsch! Richtige Lösung: "+str(hex(self.numbers[i]))[2:].upper()+"\n")
                except:
                    self.t.insert("end","Deine Eingabe war keine Zahl! \n")
            self.t.insert("end","\n\n")
            self.t.configure(state='disabled')
            self.actual = 0
        elif self.actual == 6:
            self.t.configure(state='normal')
            self.t.delete(0.0,"end")
            self.t.insert("end","Umwandlung von Hexadezimalzahlen in Dualzahlen\n")
            self.t.insert("end","Auswertung um " + time.strftime("%d.%m.%Y %H:%M:%S") +"\n")
            for i in range(10):
                try:
                    if self.numbers[i]==int(self.results[i].get(),2):
                        self.t.insert("end","Deine Eingabe: "+self.results[i].get()+" Richtig!\n")
                    else:
                        self.t.insert("end","Deine Eingabe: "+self.results[i].get()+" Falsch! Richtige Lösung: "+str(bin(self.numbers[i]))[2:]+"\n")
                except:
                    self.t.insert("end","Deine Eingabe war keine Zahl! \n")
            self.t.insert("end","\n")
            self.t.configure(state='disabled')
            self.actual = 0
        if self.w.get() == "Mit Zeitnahme!":
            self.t2=time.time()
            self.zeit = self.t2 - self.t1
            self.zeit = int(round(self.zeit))
            self.minuten = self.zeit // 60
            self.sekunden = self.zeit % 60
            self.zeit = str(self.minuten)+":"+str(self.sekunden)
            self.t.configure(state='normal')
            self.t.insert("end","Zeit: "+self.zeit+" Minuten \n")  
            self.t.configure(state='disabled')
        

    def deleteAll(self):
        for i in range(10):
            self.results[i].delete(0,"end")
        self.t.configure(state='normal')
        self.t.delete(0.0,"end")
        self.t.configure(state='disabled')

    def focusEntry(self,r):
        k = (r.index()+1)%10
        self.results[k].focus()

    def saveResult(self):
        self.resultFile = filedialog.asksaveasfilename(initialfile="ergebnis_" + \
            time.strftime("%Y_%m_%d_%H_%M_%S") + ".txt", initialdir = Path.home(),\
            filetypes = (("text files","*.txt"),("all files","*.*")))
        with open(self.resultFile, 'w') as f:
            f.write(self.t.get(0.0,"end"))
            f.write(hashlib.md5(self.t.get(0.0,"end").encode()).hexdigest())
            f.close()

    def testResult(self):
        self.testFile = filedialog.askopenfilename( initialdir = Path.home(),\
            filetypes = (("text files","*.txt"),("all files","*.*")))
        try: 
            f = open(self.testFile)
            inhalt = f.readlines()
            f.close()
        except:
            messagebox.showerror('showerror', 'Fehler beim Öffnen der Datei!')
        s = ""
        for i in range(len(inhalt)-1):
            s += inhalt[i] 
        if str(hashlib.md5(s.encode()).hexdigest()) == inhalt[len(inhalt)-1]:
            messagebox.showinfo('information', 'Die Datei ist valide!')
        else:
            messagebox.showinfo('information', 'Die Datei wurde verändert!')
        
    def open_about(self):
        window = AboutWindow(self)
        window.grab_set()

    def open_help(self):
        window = HelpWindow(self)
        window.grab_set()



if __name__ == "__main__":
    app = Application()
    app.mainloop()