import json
from datetime import datetime

import spacy
from sentence_transformers import SentenceTransformer

from src.classes.agent.check_similarity import check_similarity
from src.classes.agent.processor import process_information
from src.classes.agent.web_parser import parse_web_url
from src.classes.machine.Machine import Machine


class Agent(Machine):
    def __init__(self, name):
        super().__init__(name)
        self.brain = []
        self.brain_extended = []
        self.residence = None
        self.bank_balance = {category: 0 for category in ["income", "expenses", "savings", "misc"]}
        self.bank_budget = {category: 0 for category in ["income", "expenses", "savings", "misc"]}
        self.nlp = spacy.load("en_core_web_sm")
        self.sentence_model = SentenceTransformer("all-MiniLM-L6-v2")
        print(f"ConversationalAgent {self.name} initialized.")

    def similar_question(self, question):
        return check_similarity(self, question)

    def ask(self, question):
        matched_entry = self.similar_question(question)
        if matched_entry:
            answer = matched_entry
            source = "local knowledge base"
        else:
            answer = "I don't know the answer to that question yet."
            source = "unknown"
        print(f"Answer ({source}): {answer}")

    def add_to_brain(self, _type, key, raw_value, limit=-1, cache=True):
        process_information(self, _type, key, raw_value, limit, cache)

    def add_to_brain_extended(self, url, text):
        doc = self.nlp(text)
        details = [sent.text for sent in doc.sents]
        entry = {
            "url": url,
            "timestamp": datetime.now().isoformat(),
            "details": details
        }
        self.brain_extended.append(entry)
        print("Information added to knowledge base.")
        self.save_brain_extended()

    def parse_web(self, url):
        parse_web_url(self, url)

    def save_brain(self, filename="brain.json"):
        with open(filename, "w") as f:
            json.dump(self.brain, f)
        print("Brain saved!")

    def save_brain_extended(self, filename="brain_extended.json"):
        with open(filename, "w") as f:
            json.dump(self.brain_extended, f)
        print("Knowledge base saved!")

    def load_brain(self, filename="brain.json"):
        try:
            with open(filename, "r") as f:
                self.brain = json.load(f)
            print("Brain loaded!")
        except FileNotFoundError:
            print("No saved brain found. Starting fresh.")

    def load_brain_extended(self, filename="brain_extended.json"):
        try:
            with open(filename, "r") as f:
                self.brain_extended = json.load(f)
            print("Knowledge base loaded!")
        except FileNotFoundError:
            print("No saved knowledge base found. Starting fresh.")

    def get_age(self):
        dob = datetime.strptime(self.dob, "%Y-%m-%d %H:%M:%S")
        age = datetime.now() - dob
        return f"My name is {self.name}, my age is {age}. I was born {self.dob}"

    def live(self, neighborhood):
        self.residence = neighborhood
        print(f"{self.name} just moved into {neighborhood} on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        return str(neighborhood)

    def learn(self, _type, item, value, limit=-1):
        self.add_to_brain(_type, item, value, limit)
        return "Item processed."

    def set_monthly_budget(self, budget):
        self.bank_budget.update(budget)
        self.bank_budget["savings"] = self.bank_budget["income"] - self.bank_budget["expenses"]
        print("Updated Monthly Budget:", self.bank_budget)
        return self.bank_budget

    def get_account_balance(self):
        print("Current Account Balance:", self.bank_balance)
        return self.bank_balance

    def get_monthly_budget(self):
        print("Monthly Budget:", self.bank_budget)
        return self.bank_budget
