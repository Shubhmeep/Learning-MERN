doc_a="Rajasthan, The land of Kings is the largest state of India located in north western India. The Land of Royalty was ruled by Rajputs for a long time even today they are regarded in very high esteem. The Royal Rajputs of Rajasthan were the descendants of the Kshatriyas or warriors of vedic India. One of the world’s first and oldest civilizations, The Indus Valley Civilization was located in Rajasthan. Prime attractions of Rajasthan are its unique culture,Thar desert, great forts, palaces, temples and big fair & festivals."
doc_b="Rajasthan has had a glorious history. It is known for many brave kings, their deeds; and their interest in art and architecture. Its name means “the land of the rajas”. It was also called Rajputana (the country of the Rajputs), whose codes of chivalry shaped social mores just as their often bitter and protracted feuding dominated their politics. From this same sandy tract the world heard the bangs of India’s nuclear test program—first during the regime of Mrs. Indira Gandhi and, quite recently, when Mr. Atal Behari Vajpayee joined as Prime Minister. The nuclear blast that caused a world-hauling polarisation of leading nations, was made in an insipid belt of Rajasthan known as Pokhran. Also famous for its painted mud Potteries, Pokhran has become the recent sanatorium of India associated with the pride of its people. Such is Rajasthan, the land of Rajput warriors—bold and beauteous, simple and yet difficult, welcoming and yet self-conscious, full of valour and full of romance. In its diversity lie around the Great Indian Desert, mountain ranges, lakes, dense forests, lush green valleys, barren fields and attractive oases. Spread in  a vast stretch of 342,214 sq. km Rajasthan is the largest state of India with a population over 45 million."
doc_c="The land of Rajas and Maharajas, Rajasthan is a priceless jewel in the crown of India. The state takes you on an unforgettable ride on the sands of time where you explore some unheard stories about rich Indian history when India was called the Golden Sparrow. From its royalty oozing cities to vibrant festivals underlining its lively cultures – Rajasthan is a dream destination of every human soul seeking a luxurious experience. The state has been blessed with some of the most skilfully made monuments showcasing the elaborate lifestyles of the rulers of India in the past. Numerous legendary battles of history were fought here; however, the state still stands strong with pride till date."
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd

data = [doc_a,doc_b,doc_c]

#w stopwords

count_vectorizer = CountVectorizer()
sparse_matrix_1= count_vectorizer.fit_transform(data)
doc_term_matrix = sparse_matrix_1.todense()
df1 = pd.DataFrame(doc_term_matrix,
                   columns=count_vectorizer.get_feature_names (), 
                   index=['doc_a', 'doc_b', 'doc_c'])
print ("cosine similarity with stop words:")
#print(df1)
print ("")
print (cosine_similarity(df1, df1))

#w/o stopwords

count_vectorizer = CountVectorizer(stop_words='english')
sparse_matrix = count_vectorizer.fit_transform(data)
doc_term_matrix = sparse_matrix.todense() 

df = pd.DataFrame(doc_term_matrix, 
                  columns=count_vectorizer.get_feature_names(), 
                  index=["doc_a", "doc_b", "doc_c"]) 
print ("cosine similarity without stop words:")
print ("")
#print(df)
print (cosine_similarity(df, df))
print ("")


#porter stemmer w stopwords

from nltk.tokenize import sent_tokenize, word_tokenize 
from nltk.stem import PorterStemmer

porter=PorterStemmer()
def stemSentence (sentence):
    token_words=word_tokenize(sentence)
    stem_sentence = list()
    for word in token_words:
        stem_sentence.append(porter.stem(word))
        stem_sentence.append(" ")
    return "".join(stem_sentence)

stemmed_a=stemSentence (doc_a)
stemmed_b = stemSentence(doc_b)
stemmed_c= stemSentence (doc_c)
print(stemmed_a)
#print ("")
#print(stemmed_b)
#print ("")
#print(stemmed_c)
stemmed_data = [stemmed_a, stemmed_b, stemmed_c]

count_vectorizer = CountVectorizer()
sparse_matrix_3= count_vectorizer.fit_transform(stemmed_data) 
doc_term_matrix = sparse_matrix_3.todense()
df3= pd.DataFrame (doc_term_matrix,
                   columns=count_vectorizer.get_feature_names (), 
                   index=['stemmed_a', 'stemmed_b', 'stemmed_c']) 
print ("")
print ("porter stemmer : cosine similarity with stop words:")
print ("")
print (cosine_similarity(df3, df3))

#porter stemmer w/o stopwords

count_vectorizer =CountVectorizer(stop_words='english') 
sparse_matrix_4= count_vectorizer.fit_transform(stemmed_data)

doc_term_matrix =sparse_matrix_4.todense()

df4=pd.DataFrame (doc_term_matrix, 
                  columns=count_vectorizer.get_feature_names (), 
                  index= ['stemmed_a', 'stemmed_b', 'stemmed_c'])
print ("")
print ("porter stemmer : cosine similarity without stop words:")
print ("")
print (cosine_similarity(df4, df4))

