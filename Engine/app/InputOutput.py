import pandas as pd
import string
import re
import nltk
import numpy as np
from Pemrosesan_kata import Pemrosesan




class InputOutput:
    def datainput():
        hasilinputan = input("Masukan Judul Kerja Praktik : ")
        
        return hasilinputan
    
    t = datainput()

    def ambil_data():

        excel_data = pd.read_excel("F:/Skripsi/source/dataset.xlsx")
        judul = excel_data ["JUDUL_LAPORAN"]
        print ("judul raw : ",judul)
        
        

        return judul
    
    datajudul = ambil_data()


    def textprosessing (t, datajudul):
        Pemrosesan.eksekusiinputan(t, datajudul)

        
    textprosessing(t, datajudul)

