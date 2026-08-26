sentence = input("Enter a sentence: ")

if sentence.endswith("?"):
    print("Question")

elif sentence.lower().startswith("hello"):
    print("Greeting")

elif sentence.lower().startswith("please"):
    print("Request")

else:
    print("Statement")
