import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from Cosine_Similarity import myCosine
import numpy as np
import pickle

class ModelTF_IDF:

    
    def createmodel(text, corpus):
        vectorizer = TfidfVectorizer()
        
        #vectorizer.fit_transform(corpus)

        X = vectorizer.fit_transform(corpus)

        df = pd.DataFrame(X.T.toarray(), index=vectorizer.get_feature_names_out())

        myCosine.perhitungankemiripan(text, df)

        return df

    #     with open("Model TF-IDF.pickle", "wb") as fsave:
    #         pickle.dump(vectorizer, fsave)
    #     # df = pd.DataFrame(model.T.toarray(), index=vectorizer.get_feature_names_out())
    #     return vectorizer
    
    # def load_tf_idf_model(path):
    #     with open(path, "rb") as fopen:
    #         model = pickle.load(fopen)
        
    #     return model
    
    
        # myCosine.perhitungankemiripan(df)

        
        
        # output_vec = vectorizer.transform(inputan).toarray().reshape(df.shape[0])
        # sim = {}

        # for i in range (df.shape[0]):
        #     sim[i] = np.dot(df[:, i], output_vec) / np.linalg.norm(df[:,i]) * np.linalg.norm (output_vec)

        # sim_sort = sorted(sim.items(), key=lambda x: x[0], reverse = True)

        # print("nilai : ",sim_sort)

        
        # return sim_sort
        

    #def perhitungankemiripan(inputan, df):
        #inputan = Pemrosesan.lowercase(inputan) #pemanggilan data hasil lowercase (belum selesai)
        #df = Datareader.Tf_IDF(df) # pemanggilan data hasil pembobotan (belum selesai)
        
        #vectorizer = TfidfVectorizer

        #output_vec = vectorizer.transform(inputan).toarray().reshape(df.shape[0])
        #sim = {}

        #for i in range (705):
        #    sim[i] = np.dot(df.loc[:, i].values, output_vec) / np.linalg.norm(df.loc[:,i]) * np.linalg.norm (output_vec)

        #sim_sort = sorted(sim.items(), key=lambda x: x[0], reverse = True)

        #return sim_sort