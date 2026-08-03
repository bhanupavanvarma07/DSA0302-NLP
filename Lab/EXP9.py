import nltk
from nltk import word_tokenize
from nltk.tag import RegexpTagger

patterns = [
    (r'.*ing$', 'VBG'),      
    (r'.*ed$', 'VBD'),       
    (r'.*ly$', 'RB'),        
    (r'.*ness$', 'NN'),      
    (r'.*ment$', 'NN'),      
    (r'.*ous$', 'JJ'),       
    (r'.*able$', 'JJ'),      
    (r'.*s$', 'NNS'),        
    (r'^(The|the|A|a|An|an)$', 'DT'),  
    (r'^(is|am|are|was|were)$', 'VB'), 
    (r'^(to)$', 'TO'),      
    (r'.*', 'NN')   
]       

tagger = RegexpTagger(patterns)

text = "The cats are running quickly to school."

words = word_tokenize(text)

tagged = tagger.tag(words)

print("Rule-Based POS Tagging:\n")

for word, tag in tagged:
    print(f"{word:10} -> {tag}")