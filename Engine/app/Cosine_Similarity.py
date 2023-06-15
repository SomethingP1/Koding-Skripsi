from Pembobotan import Datareader
from Pemrosesan_kata import *
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np
##from InputOutput import *

class Cosine_Similarity:
    
    ##def datainputan(text):
    ##    datainput = Pemrosesan.lowercase(text)
        
    ##    return datainput
    
    
    ##def datapembobotan (dp):
    ##    hasilpembobotan = Datareader.Tf_IDF(dp)

    ##    return hasilpembobotan

    def perhitungan(inputan, df):
        inputan = Pemrosesan.lowercase(inputan) #pemanggilan data hasil lowercase (belum selesai)
        df = Datareader.Tf_IDF(df) # pemanggilan data hasil pembobotan (belum selesai)
        vectorizer = TfidfVectorizer

        output_vec = vectorizer.transform(inputan).toarray().reshape(df.shape[0])
        sim = {}

        for i in range (705):
            sim[i] = np.dot(df.loc[:, i].values, output_vec) / np.linalg.norm(df.loc[:,i]) * np.linalg.norm (output_vec)

        sim_sort = sorted(sim.items(), key=lambda x: x[0], reverse = True)

        return sim_sort

                    