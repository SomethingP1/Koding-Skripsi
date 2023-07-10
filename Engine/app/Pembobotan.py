import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from Cosine_Similarity import myCosine
import numpy as np
import pickle

class ModelTF_IDF:

    
    def createmodel(text):
        vectorizer = TfidfVectorizer()
        
        #vectorizer.fit_transform(corpus)
        panggil = pd.read_csv("C:/xampp/htdocs/Skripsi/Hasil-Preprocessing.csv")
        corpus = panggil ["0"]
        X = vectorizer.fit_transform(corpus)

        df = pd.DataFrame(X.T.toarray(), index=vectorizer.get_feature_names_out())
        print (df)
        #datajudul = pd.read_excel("F:/Skripsi/source/dataset.xlsx")

        print ("text : ",text)
        print (df.shape)

        #######################################################################

        output_vec = vectorizer.transform([text]).toarray().reshape(df.shape[0])
        print("output_vec shape:", output_vec.shape)
        sim = {}

        for i in range (703):
            sim[i] = np.dot(df.loc[:,i].values, output_vec) / np.linalg.norm(df.loc[:,i]) * np.linalg.norm (output_vec)

        sim_sort = sorted(sim.items(), key=lambda x: x[1], reverse = True)

        print("nilai : ",sim_sort)

        g=0
        for k, v in sim_sort:
            if v != 0.0:
                #print (g,".Nilai Similaritas : ", v)
                print (g,corpus[k])
                g += 1
                print ()

        #myCosine.perhitungankemiripan(text, df)

        return df

#    def perhitungankemiripan(inputan, model):
#         vectorizer = TfidfVectorizer()
#         print ("text : ",inputan)
#         print (model.shape)

#         output_vec = vectorizer.transform([inputan]).toarray().reshape(model.shape[0])
#         print("output_vec shape:", output_vec.shape)
#         sim = {}

        # for i in range (703):
        #     sim[i] = np.dot(model.loc[:,i].values, output_vec) / np.linalg.norm(model.loc[:,i]) * np.linalg.norm (output_vec)

        # sim_sort = sorted(sim.items(), key=lambda x: x[0], reverse = True)

        # print("nilai : ",sim_sort)