words = ["unhappy", "happiness", "happily"]

print("-" * 90)
print("{:<15}{:<12}{:<12}{:<12}{:<15}{:<12}".format(
    "Word","Prefix","Root","Suffix","Type","Normalized"))
print("-" * 90)

for word in words:

    prefix = "-"
    suffix = "-"
    root = ""

    if word.startswith("un"):
        prefix = "un"
        root = "happy"
        suffix = "-"
        t = "Derivational"

    elif word.endswith("ness"):
        root = "happy"
        suffix = "ness"
        t = "Derivational"

    elif word.endswith("ly"):
        root = "happy"
        suffix = "ly"
        t = "Derivational"

    print("{:<15}{:<12}{:<12}{:<12}{:<15}{:<12}".format(
        word,prefix,root,suffix,t,root))