queries = {
    "Q1": {
        "actual": ("ACTIVATE", "Roaming"),
        "predicted": ("ACTIVATE", "Roaming")
    },
    "Q2": {
        "actual": ("DEACTIVATE", "CallerTune"),
        "predicted": ("ACTIVATE", "CallerTune")
    },
    "Q3": {
        "actual": ("QUERY", "DataBalance"),
        "predicted": ("QUERY", "DataBalance")
    },
    "Q4": {
        "actual": ("ACTIVATE", "5GService"),
        "predicted": ("ACTIVATE", "5GService")
    }
}

correct = 0

for q, data in queries.items():
    actual = f"{data['actual'][0]}({data['actual'][1]}, Customer)"
    predicted = f"{data['predicted'][0]}({data['predicted'][1]}, Customer)"

    print(q)
    print("Actual   :", actual)
    print("Predicted:", predicted)

    if data["actual"] == data["predicted"]:
        print("Result   : Correct")
        correct += 1
    else:
        print("Result   : Semantic Error")

    print()

accuracy = correct / len(queries) * 100

print("Accuracy:", accuracy, "%")