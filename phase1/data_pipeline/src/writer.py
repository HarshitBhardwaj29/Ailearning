import json

def save_embeddings(results):
    with open("embeddings.json", "w", encoding="utf-8") as file:
        json.dump(results, file, indent=2)