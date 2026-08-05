# Experiment 1: Rule-Based Morphological Processing

words = ["analyzing", "analysis", "analytical"]

for word in words:
    root = ""
    affix = ""
    morph_type = ""

    if word.endswith("ing"):
        root = "analyze"
        affix = "-ing"
        morph_type = "Inflectional"

    elif word.endswith("sis"):
        root = "analyze"
        affix = "-sis"
        morph_type = "Derivational"

    elif word.endswith("ical"):
        root = "analyze"
        affix = "-ical"
        morph_type = "Derivational"

    print("Original Word :", word)
    print("Root          :", root)
    print("Affix         :", affix)
    print("Type          :", morph_type)
    print("Normalized    :", "analyze")
    print("-" * 40)