text = "Ravi is a good boy. He studies well."

sentences = text.split(".")

name = "Ravi"

for sentence in sentences:
    sentence = sentence.strip()
    if sentence.startswith("He"):
        sentence = sentence.replace("He", name)
    print(sentence)
