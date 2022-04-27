import nltk
from nltk import word_tokenize
from nltk.util import ngrams
from nltk.lm.models import Laplace
from collections import Counter
from nltk.corpus import brown
import pprint
import re
from nltk.corpus import stopwords
nltk.download ('stopwords')
import string

text=brown.words(categories='news')

unigrams=ngrams(text,1)
bigrams=ngrams(text,2)

punctuation=['"','#','$','%',"'",'(',')',',','*','+','-','/',':',';','<','>','=','@','[','\\',']','^','_','~','{','}','|','``']
pun_stop= punctuation + stopwords.words('english')
filter_words=[x for x in text if x not in pun_stop]
final=filter_words[:50]
final

fdist1= nltk.FreqDist (text)
totaltokens = fdist1.N()
unigrams = ngrams (text,1)
bigrams = ngrams (text, 2)
a = Counter (unigrams) 
b= Counter (bigrams)
print("Probability of Unigram")
for key in a: 
    print (key,"       ",a[key],"        " ,a[key]/totaltokens) 
print("")

print("Probability Bigram") 
unigram_no={}
bigram_no={}
count_matrix=[] 
count_probabilitymatrix=[]
tokens=final
unigram = list (ngrams (tokens, 1))
bigram = list (ngrams (tokens, 2)) 
for word in unigram:
    if word not in unigram_no:
        unigram_no[word]=unigram.count(word)

vocabulary=len(unigram_no)
print('total vocabulary:',vocabulary)
print("")        
for word in bigram:
    if word not in bigram_no: 
        bigram_no[word]=bigram.count(word)
        
for word1 in unigram:
    count=[] 
    count_probability=[]
    for word2 in unigram:
        element=(word1[0], word2[0])
        if element in bigram:
            count.append(bigram_no[element])
            count_probability.append(bigram_no[element]/unigram_no[word1])
            print("{:<15} {:<8} {:<10}".format(word1[0]+','+word2[0], bigram_no[element], bigram_no[element]/unigram_no[word1]))
        else:
            print("{:<15} {:<8} {:<10}".format(word1[0]+','+word2[0],0,0))
            count.append(0)
    count_probabilitymatrix.append(count_probability)
    count_matrix.append(count)

print ("Add 1")
print(" ")
tokens=final
for word in bigram:
    if word not in bigram_no: 
        bigram_no[word]=bigram.count(word)
        
for word1 in unigram:
    count=[] 
    count_probability=[]
    for word2 in unigram:
        element=(word1[0], word2[0])
        if element in bigram:
            count.append(bigram_no[element])
            count_probability.append(bigram_no[element]/unigram_no[word1])
            print("{:<15} {:<8} {:<10}".format(word1[0]+','+word2[0], bigram_no[element]+1, (bigram_no[element]+1)/(unigram_no[word1]+vocabulary)))
        else:
            print("{:<15} {:<8} {:<10}".format(word1[0]+','+word2[0],1,1/(unigram_no[word1]+vocabulary)))
            count.append(0)
    count_probabilitymatrix.append(count_probability)
    count_matrix.append(count)

for words2 in bigram:
    wods=[]
    for i in range():
        element=(word1[2],word[3])
        if element in bigram:
            count.append(bigram_no(1))
            count.append(bigram_no(0))
            count.append(unigram_no(1))
            count.append(unigram_no(0))
        else:
            print("this function is nt useful")
            print("{:<15} {:<8} {:<10}".format(word1[0]+','+word2[0],1,1/(unigram_no[word1]+vocabulary)))
            count.append(0)
    count_probabilitymatrix.append(count_probability)
    count_matrix.append(count)
for word in range():
    words=[]
    for i in range(i,10):
        element =(words2[1])
        if words in unigram:
            print("this is a unigram id i=for the given input")
            count.append(unigram_no(0))
        else:
            print("this function is useful for the particular input given")
        count_matrix.append(count)
        














