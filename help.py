from tkinterweb import HtmlFrame #import the HTML browser
import tkinter as tk #python3

root = tk.Tk() #create the tkinter window
frame = HtmlFrame(root) #create HTML browser

html = '''
<!DOCTYPE html>

<html lang="de">
  <head>
    <meta charset="utf-8">
    <title>Meine erste Seite</title>
  </head>
  <body>
    <p align = 'center'><h3 align = 'center'>Zahlsysteme umrechnen!</h3></p>
    <p align = 'center'>&copy; Lutz Herrmann <br> Georgius-Agricola-Gymnasium Glauchau <br> 2022 bis 2023</p>
    <p align = 'center'> Dieses Programm kommt OHNE JEDWEDE GARANTIE. </p>
    <p align = 'center'> <a href='https://www.gnu.org/licenses/gpl-3.0.de.html'>GNU General Public License, Version 3 oder neuer</a> </p>
    <p align = 'center'>Projektseite: </p>
  </body>
</html>
'''

frame.load_html(html) #load a file
root.geometry('400x300')
frame.pack(fill="both", expand=True) #attach the HtmlFrame widget to the parent window
root.mainloop()