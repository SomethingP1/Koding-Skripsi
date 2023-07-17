import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np
import pickle

class MyEngine:

    
    def TFIDF_Cosine(text):
        vectorizer = TfidfVectorizer()
        
        panggil = pd.read_csv("C:/xampp/htdocs/Skripsi/Hasil-Preprocessing.csv")
        corpus = panggil ["0"]
        #print("Dataset : ",corpus)
        X = vectorizer.fit_transform(corpus)

        df = pd.DataFrame(X.T.toarray(), index=vectorizer.get_feature_names_out())
        #print (df)

        #print ("text : ",text)
        #print (df.shape)

        #######################################################################

        output_vec = vectorizer.transform([text]).toarray().reshape(df.shape[0])
        #print("output_vec shape:", output_vec.shape)
        #print()
        sim = {}

        for i in range (len(corpus)):
            sim[i] = np.dot(df.loc[:,i].values, output_vec) / np.linalg.norm(df.loc[:,i]) * np.linalg.norm (output_vec)

        sim_sort = sorted(sim.items(), key=lambda x: x[1], reverse = True)

        #print("nilai : ",sim_sort)

        g=1
        for k, v in sim_sort:
            if v != 0.0:
                print (g,corpus[k])
                print ("Nilai Similaritas : ", v)
                g += 1
                print ()
        print ("Judul yang di input :", text)
        print ()


        return sim_sort