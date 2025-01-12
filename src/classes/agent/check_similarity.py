from sentence_transformers import util

from src.utils.clean_text import clean_text_remove_newlines


def check_similarity(self, question):
    question_embedding = self.sentence_model.encode(question, convert_to_tensor=True)
    best_matches = []
    highest_similarity = 0
    similarity_threshold = 0.7

    # 1. Check brain keys
    print("Checking brain keys.")
    for entry in self.brain:
        key_embedding = self.sentence_model.encode(entry["key"], convert_to_tensor=True)
        similarity = util.pytorch_cos_sim(question_embedding, key_embedding).item()

        if similarity > highest_similarity:
            highest_similarity = similarity

        if similarity > similarity_threshold:
            best_matches.append(entry["value"])

    # 2. Check brain values
    print("Checking brain values.", highest_similarity)
    seen_values = set(best_matches)  # Avoid duplicate values from the brain
    for entry in self.brain:
        value_embedding = self.sentence_model.encode(entry["value"], convert_to_tensor=True)
        similarity = util.pytorch_cos_sim(question_embedding, value_embedding).item()

        if similarity > highest_similarity:
            highest_similarity = similarity

        if similarity > similarity_threshold and entry["value"] not in seen_values:
            best_matches.append(entry["value"])
            seen_values.add(entry["value"])

    # 3. Check brain_extended for information from the web
    print("Checking brain extended.", highest_similarity)
    for information in self.brain_extended:
        for detail in information["details"]:
            saved_question_embedding = self.sentence_model.encode(detail, convert_to_tensor=True)
            similarity = util.pytorch_cos_sim(question_embedding, saved_question_embedding).item()
            # print("Detailed information", detail, similarity)

            if similarity > highest_similarity:
                highest_similarity = similarity

            if similarity > similarity_threshold:
                print("Information similarity found in brain extended", information["url"])
                # print("Similarity", similarity, "Highest Similarity", highest_similarity, "Detail", detail)
                best_matches.append(clean_text_remove_newlines(detail))

    print("Highest similarity found:", highest_similarity)
    return best_matches if highest_similarity > similarity_threshold else None
