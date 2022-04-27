import operator

from nltk.corpus import words
import time

start = time.time()

def candidate_words(word,n=2,number_words=20):
    ngram_dict={}
    n_total = 26**n
    for i in range(n_total):
        c =''
        k=i
        for j in range (n):
            c=chr(97+(k%26))+c
            k=k//26
            ngram_dict[c]=set()
    lexicon=words.words()
    lexicon=[i.lower() for i in lexicon if i.isalnum()]
    for w in range(len(lexicon)):
        for c in range (0,len(lexicon[w])-n+1):
            ngram_dict[lexicon[w][c:c+n]].add(w)
    freq_dict={}
    for c in range(0,len(word)-n+1):
        for w in ngram_dict[word[c:c+n]]:
            if lexicon[w]not in freq_dict.keys():
                freq_dict[lexicon[w]]=1
            else:
                freq_dict[lexicon[w]]+=1
    top_freq=dict(sorted(freq_dict.items(),key =operator.itemgetter(1), reverse =True)[:number_words])
    return top_freq
    
if __name__=='__main__':
    word=input('Enter the word:').lower()
    top_freq=candidate_words(word)
    print(top_freq)
    print("--- %s seconds ---" % (time.time() - start))
