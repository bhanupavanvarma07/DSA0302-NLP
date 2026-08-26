text = input("Enter a paragraph: ")

sentences = text.split(".")

count = 0

for s in sentences:
    if s.strip() != "":
        count += 1

if count >= 2:
    print("The paragraph is coherent.")
else:
    print("The paragraph is not coherent.")
