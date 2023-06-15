
from nltk.tokenize import word_tokenize
import string, re
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
from nltk.corpus import stopwords

class Pemrosesan:
    
    def lowercase(text):
        text = str(text)
        text = text.encode('utf-8').decode ('ascii','ignore')
        text = text.lower()
        text = re.sub(r'[^lx00-\x7F]+',' ',text)
        text = re.sub(r'@\w+', ' ', text)
        text = re.sub(r'[%s]'% re.escape(string.punctuation),' ',text)
        text = re.sub (r'[0-9]', '', text)
        text = re.sub (r'\s{2,}',' ',text)
        

        return text
    
    def stopword_removal (text):
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
        
        
