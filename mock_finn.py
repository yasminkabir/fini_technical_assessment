import json

with open("knowledge_base.json") as f:
    kb = json.load(f)

def finn(query: str) -> str:
    q = query.lower()
    for entry in kb:
        if any(keyword in q for keyword in entry ["keywords"]):
            return entry["answer"]
    else:
        return "I don’t have that information yet."
if __name__ == "__main__":
    while True:
        query = input("Ask Finn a question (or type 'quit'): ")
        if query.lower() == "quit":
            break
        print("Finn:", finn(query))
