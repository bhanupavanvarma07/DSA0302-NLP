sentences = [
    {
        "sentence": "Doctor prescribed medicine to patient",
        "subject": "Doctor",
        "verb": "prescribed",
        "object": "Medicine"
    },
    {
        "sentence": "Patient reported severe headache",
        "subject": "Patient",
        "verb": "reported",
        "object": "Headache"
    },
    {
        "sentence": "Nurse monitored patient continuously",
        "subject": "Nurse",
        "verb": "monitored",
        "object": "Patient"
    },
    {
        "sentence": "Medicine reduced blood pressure",
        "subject": "Medicine",
        "verb": "reduced",
        "object": "Blood Pressure"
    }
]

roles = {
    "Doctor": "Agent",
    "Medicine": "Instrument",
    "Patient": "Recipient",
    "Headache": "Symptom"
}

for item in sentences:

    print("Sentence:", item["sentence"])
    print("Subject :", item["subject"])
    print("Verb    :", item["verb"])
    print("Object  :", item["object"])

    subject = item["subject"]
    obj = item["object"]

    if subject in roles:
        print(subject, "->", roles[subject])

    if obj in roles:
        print(obj, "->", roles[obj])

    print("-" * 40)