import json

with open("knowledge_base.json") as f:
    kb = json.load(f)

def finn(query: str) -> str:
    q = query.lower()
    if "water" in q or "drink" in q:
        return kb["hydration"]
    elif "sleep" in q:
        return kb["sleep"]
    elif "stress" in q:
        return kb["stress"]
    elif "tired" in q:
        return kb["tired"]
    elif "eat" in q:
        return kb["eat"]
    elif "exercise" in q:
        return kb["exercise"]
    else:
        return "I don’t have that information yet, but I can point you to resources!"

if __name__ == "__main__":
    while True:
        query = input("Ask Finn a question (or type 'quit'): ")
        if query.lower() == "quit":
            break
        print("Finn:", finn(query))
