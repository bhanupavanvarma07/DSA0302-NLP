sentence = "The boy is playing football"

words = sentence.split()

tags = [(word, "NN") for word in words]

print("Initial Tags:")
for word, tag in tags:
    print(f"{word:10} -> {tag}")

transformed_tags = []

for i, (word, tag) in enumerate(tags):
    if word.lower() in ["the", "a", "an"]:
        tag = "DT"

    elif word.lower() in ["is", "am", "are", "was", "were"]:
        tag = "VBZ"

    elif word.endswith("ing"):
        tag = "VBG"

    elif word.endswith("ly"):
        tag = "RB"

    transformed_tags.append((word, tag))

print("\nAfter Applying Transformation Rules:")

for word, tag in transformed_tags:
    print(f"{word:10} -> {tag}")