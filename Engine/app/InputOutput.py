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

        ##hasil = str(judul)

        return judul
    
    datajudul = ambil_data()


    def textprosessing (t):
        hasillowercase = Pemrosesan.penggabunganjudul(t)
        print ("Hasil Preprosessing Inputan : ", hasillowercase)
    textprosessing(t)

    #def textprosessingjudul (datajudul):
    #    hasillowercase = Pemrosesan.penggabunganjudul(datajudul)
    #    print ("Hasil Preprosessing Judul : ")
    #    print (hasillowercase)
    #textprosessingjudul(datajudul)

    
    #def outputstemming (t):
    #    hasilstemming = Pemrosesan.stemming(t)
    #    print ("Hasil Stemming : ", hasilstemming)

    #outputstemming(t)

    #def outputstemmingjudul (datajudul):
    #    hasilstemming = Pemrosesan.stemming(datajudul)
    #    print ("Hasil Stemming : ")
    #    print (hasilstemming)

    #outputstemmingjudul(datajudul)
        
    
    #def outputstopword_removal(t):
    #    hasilstop_removal = Pemrosesan.stopword_removal(t)
    #    print ("Hasil Stopword Removal : ", hasilstop_removal)
    
    #outputstopword_removal(t)

    #def outputstopword_removaljudul(datajudul):
    #    hasilstop_removal = Pemrosesan.stopword_removal(datajudul)
    #    print ("Hasil Stopword Removal : ")
    #    print (hasilstop_removal)
    
    #outputstopword_removaljudul(datajudul)
    
    #def hasilpembobotanjudul(datajudul):
    #    hasilTF_IDF = Datareader.Tf_IDF(datajudul)
    #    print (hasilTF_IDF)
        
    #    return hasilTF_IDF
    
    #hasilpembobotanjudul(datajudul)

    ##datapembobotan = hasilpembobotanjudul(datajudul)

    ##def hasilperhitungan(t, datapembobotan):
    ##    hasilcosine = Cosine_Similarity.perhitungan(t, datapembobotan)
    ##    print ("Nilai Kemiripan : ")
    ##    print (hasilcosine)

    ##hasilperhitungan(t, datapembobotan)

