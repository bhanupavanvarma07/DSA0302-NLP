data = {
    "Apple accessories": {
        "senses": ["Fruit", "Technology Brand"],
        "result": "iPhone Charger",
        "correct": "Technology Brand"
    },
    "Mouse wireless": {
        "senses": ["Animal", "Computer Device"],
        "result": "Bluetooth Mouse",
        "correct": "Computer Device"
    },
    "Java tutorial": {
        "senses": ["Island", "Programming Language"],
        "result": "Coding Lessons",
        "correct": "Programming Language"
    },
    "Python course": {
        "senses": ["Snake", "Programming Language"],
        "result": "Software Development Training",
        "correct": "Programming Language"
    }
}

for query, info in data.items():

    print("Query:", query)
    print("Possible Senses:", ", ".join(info["senses"]))
    print("Clicked Result:", info["result"])
    print("Selected Sense:", info["correct"])
    print()