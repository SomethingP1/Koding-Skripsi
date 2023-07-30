from nltk.tokenize import word_tokenize
import string, re
from nltk.corpus import stopwords
from MainEngine import *
import pandas as pd


class Pemrosesan:

    def eksekusiinputan(teks, judul):
    
        hasillowercaseteks = Pemrosesan.casefolding(teks)
        hasilstopwordteks = Pemrosesan.stopword_removal(hasillowercaseteks)
        
        
        
        tampung = []
        for i in judul:
            judulx = str(i)
            hasillowercase = Pemrosesan.casefolding(judulx)
            hasilstopword = Pemrosesan.stopword_removal(hasillowercase)
            tampung.append(hasilstopword)
        
        pd.DataFrame(tampung).to_csv('Hasil-Preprocessing.csv')

        nilaireturn = MyEngine.TFIDF_Cosine(hasilstopwordteks)
        return nilaireturn
        

    
    def casefolding(text):    
        text = str.lower(text)
        text = re.sub('[%s]' % re.escape(string.punctuation.replace('?', '')), '', text)
        text = re.sub("[^a-zA-Z0-9\s:\n\\n]+@]", '', text)
        text = re.sub('www\S+', '', text)
        text = re.sub('\w*\d\w*', '', text)
        text = re.sub('[‘’“”…]', '', text)
        text = re.sub('\n', '', text)
        text = re.sub('\r', '', text)
        text = text.replace('?', ' ?')
        text = text.replace('\d+', '')
        text = re.sub('[.;:!\'?,\"()\[\]*~]', '', text)
        text = re.sub('(<br\s*/><br\s*/>)|(\-)|(\/)', '', text)
        text = re.sub('\n2', '', text)
        

        return text

    
    def stopword_removal (text):
        text = str(text)
        liststopword = set(stopwords.words('indonesian'))
        wordx = [word for word in text.split() if word not in liststopword]
        hasil = ' '.join(wordx)


        return hasil
    
    


        
