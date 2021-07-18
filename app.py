from tkinter import *
import sqlite3


root = Tk()
root.title("Programma")
root.geometry("400x500")

url_var = StringVar()

def verifica():
    
    url=url_var.get()

    print("l'url indicata è: " + url)

    url_var.set("")

#creiamo label e input 
url_label = Label(root, text ='url', font=('calibre', 10, 'bold'))
url_entry = Entry(root, textvariable= url_var, font=('calibre', 10, 'normal'))


####### Buttons #############
btn_verifica = Button(root, text="Aggiungi", command=verifica)
btn_chiudi = Button(root, text="Chiudi", command=root.destroy)

#posizionare elementi nella finestra

url_label.grid(row=0, column=0)
url_entry.grid(row=0, column=1)
btn_verifica.grid(row=2, column=1)
btn_chiudi.grid(row=2, column=2)


root.mainloop()
