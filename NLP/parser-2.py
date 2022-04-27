import nltk
import time 
start = time.time()
gram_rules = nltk.CFG.fromstring(
    """
S -> NP VP
NP -> Det N | Det N PP
VP -> V NP | V NP PP
PP -> P NP
NP -> 'I'
N -> 'man' | 'park' | 'telescope' | 'dog'
Det -> 'the' | 'a'
P -> 'in' | 'with'
V -> 'saw'
"""
)
sentence = ['I', 'saw', 'a', 'man', 'in', 'the', 'park']
parser = nltk.ChartParser(gram_rules)
print("top down parsing")
print("")
for tree in parser.parse(sentence): 
    print(tree)
print(tree.draw())
print("--- %s seconds ---" % (time.time() - start))
print("")
print("bottom up parsing")
print("")
parser = nltk.ShiftReduceParser(gram_rules, trace=2)
for tree in parser.parse(sentence):
    print(tree)
print(tree.draw())
print("--- %s seconds ---" % (time.time() - start))

