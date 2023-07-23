import pandas as pd
import string
import re
import nltk
import numpy as np
from Pemrosesan_kata import Pemrosesan
from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askopenfile

app = Tk()
app.title('Pencarian Judul Kerja Praktik')
app.geometry('700x400')

datajudul = None
        
def inputan():
    global judulpencarian
    global datajudul

    tree.delete(*tree.get_children())

    datainputan = judulpencarian.get()

    hasilall = Pemrosesan.eksekusiinputan(datainputan, datajudul)

    g=1
    for k, v in hasilall:
        if v != 0.0:
            
            olah = (g,datajudul[k],v)
            g +=1

            tree.insert('', 'end', values=olah)


def openfile():
    global datajudul
    file_path = askopenfile(mode='r', filetypes=[('Excel File', '*xlsx')])
    namajudul['text'] = file_path.name
    if file_path is not None:
        datajudul = pd.read_excel(file_path.name)["JUDUL_LAPORAN"]

namalabel = Label(app, text = 'Masukan Judul')
namalabel.pack()
judulpencarian = Entry(app, relief=SUNKEN)
judulpencarian.pack(padx=10, pady=5)

datajudul = Button(app, text= 'Masukan File', command=openfile)
datajudul.pack(padx=10, pady=5)
namajudul = Label(app, text="Nama File")
namajudul.pack()

process = Button(app, text= 'Cari', command=inputan)
process.pack(padx=10, pady=5)

tree = ttk.Treeview(app, columns=('Index', 'Judul', 'Tingkat Kemiripan'), show='headings')
tree.column('Index', width=60)
tree.column('Judul', width=400)
tree.column('Tingkat Kemiripan', width=200)

tree.heading('Index', text='Index')
tree.heading('Judul', text='Judul')
tree.heading('Tingkat Kemiripan', text='Tingkat Kemiripan')
tree.pack()


app.mainloop()


# class InputOutput:
    # def datainput():
    #     hasilinputan = input("Masukan Judul Kerja Praktik : ")
        
    #     return hasilinputan
    
    # text = datainput()

    # def ambil_data():

    #     excel_data = pd.read_excel("F:/Skripsi/source/dataset.xlsx")
    #     judul = excel_data ["JUDUL_LAPORAN"]
    #     print ("judul raw : ",judul)
        
        

    #     return judul
    
    # datajudul = ambil_data()


    # def textprosessing (text, datajudul):
    #     hasilsemua = Pemrosesan.eksekusiinputan(text, datajudul)
    #     g=1
    #     for k, v in hasilsemua:
    #         if v != 0.0:
    #             print (g,datajudul[k])
    #             print ("Nilai Similaritas : ", v)
    #             g += 1
    #             print()
                
    #     print ("Jumlah Judul : ",g-1)
    #     print ("Judul yang di input :", text)
    #     print ()

        
    # textprosessing(text, datajudul)
