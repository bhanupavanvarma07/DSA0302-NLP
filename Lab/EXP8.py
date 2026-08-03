from collections import defaultdict

training_data = [
    ("The", "DT"),
    ("dog", "NN"),
    ("barks", "VBZ"),
    ("loudly", "RB"),
    ("A", "DT"),
    ("cat", "NN"),
    ("meows", "VBZ"),
    ("softly", "RB"),
    ("The", "DT"),
    ("bird", "NN"),
    ("sings", "VBZ"),
    ("sweetly", "RB")
]

word_tag_count = defaultdict(lambda: defaultdict(int))

for word, tag in training_data:
    word_tag_count[word.lower()][tag] += 1

word_tag = {}

for word in word_tag_count:
    word_tag[word] = max(word_tag_count[word],
                         key=word_tag_count[word].get)

sentence = "The dog barks loudly"

words = sentence.split()

print("Stochastic POS Tagging:\n")

for word in words:
    tag = word_tag.get(word.lower(), "NN")
    print(f"{word:10} -> {tag}")