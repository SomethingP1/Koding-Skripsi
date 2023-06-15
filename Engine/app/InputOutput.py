import pandas as pd
import string
import re
import nltk
import numpy as np
from Pemrosesan_kata import *
from Cosine_Similarity import *
from Pembobotan import *




class InputOutput:
    def datainput():
        hasilinputan = input("Masukan Judul Kerja Praktik : ")
        
        return hasilinputan
    
    t = datainput()

    def ambil_data():

        excel_data = pd.read_excel("F:/Skripsi/source/dataset.xlsx")
        judul = excel_data ["JUDUL_LAPORAN"]

        return judul
    
    datajudul = ambil_data()


    def textprosessing (t, datajudul):
        hasillowercase = Pemrosesan.lowercase(t, datajudul)
        print ("Hasil Lower Case : ")
        print (hasillowercase)


    textprosessing(t,datajudul)

    
    def outputstemming (t, datajudul):
        hasilstemming = Pemrosesan.stemming(t, datajudul)
        print ("Hasil Stemming : ")
        print (hasilstemming)

    outputstemming(t, datajudul)
        
    
    def outputstopword_removal(t, datajudul):
        hasilstop_removal = Pemrosesan.stopword_removal(t, datajudul)
        print ("Hasil Stopword Removal : ")
        print (hasilstop_removal)

    outputstopword_removal(t, datajudul)
    
    ##def hasilpembobotanjudul(datajudul):
    ##    hasilTF_IDF = Datareader.Tf_IDF(datajudul)
    ##    print (hasilTF_IDF)
        
    ##    return hasilTF_IDF
    
    ##hasilpembobotanjudul(datajudul)

    ##datapembobotan = hasilpembobotanjudul(datajudul)

    ##def hasilperhitungan(t, datapembobotan):
    ##    hasilcosine = Cosine_Similarity.perhitungan(t, datapembobotan)
    ##    print ("Nilai Kemiripan : ")
    ##    print (hasilcosine)

    ##hasilperhitungan(t, datapembobotan)

