
from nltk.tokenize import word_tokenize
import string, re
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
from nltk.corpus import stopwords

class Pemrosesan:

    def penggabunganjudul(teks):
        text = Pemrosesan.lowercase(teks)
        text2 = Pemrosesan.stopword_removal(text)
        text3 = Pemrosesan.stemming(text2)

        return text3
    
    def lowercase(text):
        text = str(text)
        text = text.encode('utf-8').decode('ascii', 'ignore')
        text = text.lower()
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
    
    def stemming (text):
        factory = StemmerFactory()
        stemmer = factory.create_stemmer()
        wordx = [stemmer.stem(word) for word in text.split()]
        hasil = ' '.join(wordx)

        return hasil
    
    
    


        
