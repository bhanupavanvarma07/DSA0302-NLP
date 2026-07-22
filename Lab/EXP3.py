import nltk
from nltk.tokenize import word_tokenize
from nltk import pos_tag

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

sentence = "The boys are playing football happily."

words = word_tokenize(sentence)

tags = pos_tag(words)

print("Word\t\tPart of Speech")

for word, tag in tags:
    print(word, "\t\t", tag)