import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer


class Datareader:
    def Tf_IDF(datajudul):
    
        vectorizer = TfidfVectorizer()
        X = vectorizer.fit_transform(datajudul)

        df = pd.DataFrame(X.T.toarray(), index=vectorizer.get_feature_names_out())
        data_judul = df.astype(str)
        return data_judul