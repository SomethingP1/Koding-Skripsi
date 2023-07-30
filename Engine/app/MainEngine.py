import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np


class MyEngine:

    
    def TFIDF_Cosine(text):
        vectorizer = TfidfVectorizer()
        
        panggil = pd.read_csv("C:/xampp/htdocs/Skripsi/Hasil-Preprocessing.csv")
        corpus = panggil ["0"]
        X = vectorizer.fit_transform(corpus)

        df = pd.DataFrame(X.T.toarray(), index=vectorizer.get_feature_names_out())


        inputan_vec = vectorizer.transform([text]).toarray().reshape(df.shape[0])
        cosine = {}

        for i in range (len(corpus)):
            cosine[i] = np.dot(df.loc[:,i].values, inputan_vec) / (np.linalg.norm(df.loc[:,i]) * np.linalg.norm(inputan_vec))
            

        cosine_sort = sorted(cosine.items(), key=lambda x: x[1], reverse = True)


        return cosine_sort
    
   