from sentence_transformers import util


def check_similarity(self, question):
    question_embedding = self.sentence_model.encode(question, convert_to_tensor=True)
    best_match = None
    highest_similarity = 0

    # 1. Check brain keys
    for entry in self.brain:
        key_embedding = self.sentence_model.encode(entry["key"], convert_to_tensor=True)
        similarity = util.pytorch_cos_sim(question_embedding, key_embedding).item()
        if similarity > highest_similarity:
            highest_similarity = similarity
            best_match = entry["value"]

    # 2. Check brain values if no high similarity found in keys
    if highest_similarity < 0.7:
        print("No high similarity found in brain keys. Checking brain values.", highest_similarity)
        for entry in self.brain:
            value_embedding = self.sentence_model.encode(entry["value"], convert_to_tensor=True)
            similarity = util.pytorch_cos_sim(question_embedding, value_embedding).item()
            if similarity > highest_similarity:
                highest_similarity = similarity
                best_match = entry["value"]

    # 3. Check brain_extended for information from the web
    if highest_similarity < 0.7:
        print("No high similarity found in brain values. Checking brain extended.", highest_similarity)
        for information in self.brain_extended:
            print("Information in brain extended", information["url"])
            for detail in information["details"]:
                #  print("Detailed information", detail)
                saved_question_embedding = self.sentence_model.encode(detail, convert_to_tensor=True)
                similarity = util.pytorch_cos_sim(question_embedding, saved_question_embedding).item()
                #   print("Similarity", similarity, "Highest Similarity", highest_similarity)
                if similarity > highest_similarity:
                    highest_similarity = similarity
                    best_match = detail

    print("Highest similarity found:", highest_similarity)
    return best_match if highest_similarity > 0.7 else None
