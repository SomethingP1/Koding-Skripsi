import pandas as pd
import string
import re
import nltk
import numpy as np
from Pemrosesan_kata import Pemrosesan
from Pembobotan import *
from Cosine_Similarity import *




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

    # def corpuscontoh ():
    #     corpus = ['Ikhsan kayang di mall', 
    #               'Nanda nginep dirumah ikhsan',
    #               'Agung Maen kostan nanda']
        
    #     print (corpus)
    #     return corpus
    # contohcorpus = corpuscontoh()


    def textprosessing (t, datajudul):
        hasilpreprosessinginputan = Pemrosesan.eksekusiinputan(t, datajudul)
        print ("Hasil Preprosessing Inputan : ", hasilpreprosessinginputan)

        #hasispreprossesingjudul = pem
    textprosessing(t, datajudul)

    #def textprosessingjudul (datajudul):
    #    hasilpreprosessing = Pemrosesan.eksekusijudul(datajudul)
    #    print ("Hasil Preprosessing Judul : ", hasilpreprosessing)
        #sim_sort = myCosine.perhitungankemiripan(datajudul, hasillowercase)
     #   return hasilpreprosessing
    
    #textprosessingjudul(datajudul)

    # def ambil_judul():

    #     excel_data = pd.read_excel("F:/Skripsi/source/dataset.xlsx")
    #     judul = excel_data ["JUDUL_LAPORAN"]
    #     listjudul = InputOutput.outputfinal(judul)

    #     return listjudul

    # def hasilcosine(hasil):
    #     hasilc = (hasil)

    #     return hasilc
    
    # def listjudul():
    #     listjudulx = InputOutput.datajudul()
    #     return listjudulx
    
    
    #def outputfinal (output):
        #hasiloutput = myCosine.kirimdata(output = 0)
        #listjudul = InputOutput.listjudul(datajudul)
        #print (hasiloutput)

        #for k, v in hasiloutput:
        #    if v != 0.0:
        #        print ("Hasil Similaritas : ", v)
        #        print (listjudul[k])
        #        print ()

    
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

