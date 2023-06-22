#from Pemrosesan_kata import *
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np
import pandas as pd
import pickle
#from InputOutput import *

class myCosine:
    
    #def ambilhasilinputan (inputan):
    #    inputanx = (inputan)
        
    #    print("nilai ",inputanx)

    #def ambildatamodeling (dataframe):
    #    dataframex = (dataframe)
        
    #    return dataframex
    
    #def pengumpulandata (z,df):
    #    a = myCosine.ambilhasilinputan(z)
    #    b = myCosine.ambildatamodeling(df)

    #    return a, b
    
    #def kirimdata (c,v):
    #    q = myCosine.pengumpulandata(c)
    #    t = myCosine.pengumpulandata(v)

    #    hasil = myCosine.perhitungankemiripan (q,t)
        
    #    return hasil
    
    ##def datainputan(text):
    ##    datainput = Pemrosesan.lowercase(text)
        
    ##    return datainput
    
    
    ##def datapembobotan (dp):
    ##    hasilpembobotan = Datareader.Tf_IDF(dp)

    ##    return hasilpembobotan

    def load_tf_idf_model(path):
        with open(path, "rb") as fopen:
            model = pickle.load(fopen)
        
        return model
    
    def perhitungankemiripan(inputan, model):
        vectorizer = TfidfVectorizer()
        # model = myCosine.load_tf_idf_model("Model TF-IDF.pickle")
        # #print(model)
        # #print (inputan)
        # output_vec = model.fit_transform([inputan])
        # #print (output_vec)
        # sim = {}

        # for i in range(704):
        #     sim[i] = np.dot(model[i], output_vec.T) / (np.linalg.norm(model[i]) * np.linalg.norm(output_vec))

        #     sim_sort = sorted(sim.items(), key=lambda x: x[1], reverse=True)

        #     print("nilai : ", sim_sort)

        #     return

        
        output_vec = vectorizer.fit_transform([inputan]).toarray().reshape(model.shape[0])
        print (output_vec)
        sim = {}

        # for i in range(705):
        #     sim[i] = np.dot(model[i].toarray().flatten(), output_vec.toarray().flatten()) / (np.linalg.norm(model[i].toarray()) * np.linalg.norm(output_vec.toarray()))

        #     sim_sort = sorted(sim.items(), key=lambda x: x[1], reverse=True)

        #     print("nilai : ", sim_sort)

        #     return
        for i in range (705):
            sim[i] = np.dot(model.iloc[:,i], output_vec) / np.linalg.norm(model.iloc[:,i]) * np.linalg.norm (output_vec)

        sim_sort = sorted(sim.items(), key=lambda x: x[0], reverse = True)

        print("nilai : ",sim_sort)

        
        return

                    