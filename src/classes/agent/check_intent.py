import spacy

from src.classes.agent.intent_actions.actions import intent_actions


def check_intent(question):
    # Load the trained spaCy model
    nlp = spacy.load("intent_model")
    INTENT_THRESHOLD = 0.7

    print("Checking intent for question:", question)
    doc = nlp(question)
    print("Document", doc)
    intent = max(doc.cats, key=doc.cats.get)
    similarity = doc.cats[intent]
    print("Document categories:", doc.cats)
    print("Max similarity:", similarity)

    if similarity > INTENT_THRESHOLD:
        print("Intent detected:", intent)
        return intent
    else:
        print("Intent not detected.")
        return None


def route_intent(intent):
    response_function = intent_actions.get(intent, lambda: "I'm not sure how to respond to that.")
    return response_function()
