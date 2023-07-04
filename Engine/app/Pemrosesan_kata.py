
from nltk.tokenize import word_tokenize
import string, re
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
from nltk.corpus import stopwords
from Pembobotan import *
import pandas as pd
import numpy as np


class Pemrosesan:

    def eksekusiinputan(teks, judul):
        #tampungteks = []
        hasillowercaseteks = Pemrosesan.casefolding(teks)
        hasilstopwordteks = Pemrosesan.stemming(hasillowercaseteks)
        hasilstemmingteks = Pemrosesan.stemming(hasilstopwordteks)
        
        #tampungteks.append(hasilstemmingteks)

        #myCosine.perhitungankemiripan(hasillowercaseteks)
    
        
        tampung = []
        for i in judul:
            judulx = str(i)
            hasillowercase = Pemrosesan.casefolding(judulx)
            #hasilstopword = Pemrosesan.stopword_removal(hasillowercase)
            #hasilstemming = Pemrosesan.stemming(hasilstopword)
            #hasil = pd.Series(hasilstemming)
            tampung.append(hasillowercase)
        
        #print (tampung)
        #print("list Judul : ",tampung)
        # #ModelTF_IDF.createmodel(hasilstemmingteks,tampung)
        ModelTF_IDF.createmodel(hasillowercaseteks,tampung)
        # #myCosine.perhitungankemiripan(hasilstemmingteks)
        
        
            


        
        # judul2 = Pemrosesan.stopword_removal(judul1)
        # text2 = Pemrosesan.stopword_removal(text)
        
        # text3 = Pemrosesan.stemming(text2)
        # judul3 = Pemrosesan.stemming(judul2)

        #tes = judul1.split('\n')
        #hasil = pd.Series(judul1)
        #print (judul1)
        #ModelTF_IDF.createmodel(text, hasil)
        #model = ModelTF_IDF.createmodel(hasil)

        #hasil = myCosine.perhitungankemiripan(text3, judul3)

        return
    
    # def eksekusijudul(teks):
    #     text = Pemrosesan.lowercase(teks)
    #     text2 = Pemrosesan.stopword_removal(text)
    #     text3 = Pemrosesan.stemming(text2)

    #     ##hasil = pd.Series(text3)
    #     hasil_TF_IDF = Datareader.ambildatapreprosessing(text3)

    #     hasilsimilarity = myCosine.perhitungankemiripan(text3, hasil_TF_IDF)

    #     return hasilsimilarity
    
    # def casefolding (textawal):
    #     text = textawal.str.lower()
    
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
    
    #def tokenize (text):
     #   text = word_tokenize(text)

    
    def stopword_removal (text):
        # if isinstance (text, list):
        #     text = ' '.join(text)
        text = str(text)
        liststopword = set(stopwords.words('indonesian'))
        wordx = [word for word in text.split() if word not in liststopword]
        hasil = ' '.join(wordx)


        return hasil
    
    def stemming (text):
        factory = StemmerFactory()
        stemmer = factory.create_stemmer()
        wordx = [stemmer.stem(word) for word in text.split()]
        hasil = ' '.join(wordx)

        return hasil
    
    
    


        
