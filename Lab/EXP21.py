import nltk
from nltk import word_tokenize, pos_tag
from nltk.chunk import RegexpParser

sentence = "The intelligent student solved the difficult problem."

words = word_tokenize(sentence)

tags = pos_tag(words)

grammar = "NP: {<DT>?<JJ>*<NN>+}"

cp = RegexpParser(grammar)

result = cp.parse(tags)

print(result)

result.draw()
