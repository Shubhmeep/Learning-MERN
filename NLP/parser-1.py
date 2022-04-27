import nltk
import time 
start = time.time()
gram_rules = nltk.CFG.fromstring(""" 
S ->NP NP
NP -> DT ADJ N | DT N | NP VP
DT ->'The' | 'the'
N ->'can' | 'water'
ADJ ->'large'
VP -> V VP | V NP | V
V ->'hold'| 'can'
""")
sentence = ['The', 'large', 'can', 'can', 'hold', 'the', 'water']
parser = nltk.ChartParser(gram_rules)
for tree in parser.parse(sentence): 
    print(tree)
print(tree.draw())
print("--- %s seconds ---" % (time.time() - start))
gram_rules = nltk.CFG.fromstring(""" 
S ->NP VP
NP -> DT ADJ N | DT N | NP VP
DT ->'The' | 'the'
N ->'can' | 'water'
ADJ ->'large'
VP -> V VP | V NP | V
V ->'hold'| 'can'
""")
sentence = ['The', 'large', 'can', 'can', 'hold', 'the', 'water']
parser = nltk.ChartParser(gram_rules)
for tree in parser.parse(sentence): 
    print(tree)
print(tree.draw())
print("--- %s seconds ---" % (time.time() - start))

