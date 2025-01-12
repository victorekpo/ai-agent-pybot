import json
from datetime import datetime

import boto3
import spacy
from sentence_transformers import SentenceTransformer

from src.classes.agent.check_intent import check_intent, route_intent
from src.classes.agent.check_similarity import check_similarity
from src.classes.agent.processor import process_information
from src.classes.agent.web_parser import parse_web_url
from src.classes.machine.Machine import Machine
from src.utils.clean_text import clean_web_text


class Agent(Machine):
    def __init__(self, name):
        super().__init__(name)
        self.name = name
        self.brain = []
        self.brain_extended = []
        self.residence = None
        self.bank_balance = {category: 0 for category in ["income", "expenses", "savings", "misc"]}
        self.bank_budget = {category: 0 for category in ["income", "expenses", "savings", "misc"]}
        self.nlp = spacy.load("en_core_web_sm")
        self.sentence_model = SentenceTransformer("all-MiniLM-L6-v2")
        self.sqs = None
        self.queue_url = None
        print(f"ConversationalAgent {self.name} initialized.")

    def similar_question(self, question):
        return check_similarity(self, question)

    def ask(self, question):
        print("\nAsking question:", question)
        internal_source = None
        matched_entries = []

        intent_result = check_intent(question)
        if intent_result is not None:
            print("Intent detected:", intent_result)
            result = route_intent(intent_result)
            print("Intent result:", result)
            matched_entries.append(result)
            internal_source = "intent-found"

        similar_matches = self.similar_question(question)
        if similar_matches is not None:
            print("Similar matches found:", similar_matches)
            matched_entries.extend(similar_matches)
            internal_source = "similar-questions"

        if matched_entries:
            answer = matched_entries
            source = "local knowledge base from " + str(internal_source)
        else:
            answer = "I don't know the answer to that question yet."
            source = "unknown"
        print(f"Answer ({source}): {answer}")
        return answer

    def add_to_brain(self, _type, key, raw_value, limit=-1, cache=True):
        process_information(self, _type, key, raw_value, limit, cache)

    def add_to_brain_extended(self, url, text):
        cleaned_text = clean_web_text(text)
        doc = self.nlp(cleaned_text)
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
            json.dump({self.name: self.brain}, f)
        print("Brain saved!")

    def save_brain_extended(self, filename="brain_extended.json"):
        with open(filename, "w") as f:
            json.dump({self.name: self.brain_extended}, f)
        print("Knowledge base saved!")

    def load_brain(self, filename="brain.json"):
        try:
            with open(filename, "r") as f:
                data = json.load(f)
                if self.name in data:
                    self.brain = data[self.name]
                    print("Brain loaded!")
                else:
                    print(f"No brain data found for {self.name}. Starting fresh.")
        except FileNotFoundError:
            print("No saved brain found. Starting fresh.")

    def load_brain_extended(self, filename="brain_extended.json"):
        try:
            with open(filename, "r") as f:
                data = json.load(f)
                if self.name in data:
                    self.brain_extended = data[self.name]
                    print("Knowledge base loaded!")
                else:
                    print(f"No extended brain data found for {self.name}. Starting fresh.")
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
        print("Item learned successfully.")
        return True

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

    def connect_sqs(self):
        print("Connecting to SQS")
        self.sqs = boto3.client('sqs', endpoint_url='http://localhost:4566', region_name='us-east-1')

        # Get the queue URL
        self.queue_url = self.sqs.get_queue_url(QueueName='my-queue')['QueueUrl']
        print("Connected to SQS with queue URL:", self.queue_url)
        return self.sqs

    def send_sqs_message(self, message_body):
        print("Sending Message from", self.name)
        response = self.sqs.send_message(
            QueueUrl=self.queue_url,
            MessageBody=message_body
        )
        print(f"Message sent: {response['MessageId']}")
        return response['MessageId']

    def receive_sqs_messages(self):
        print("Receiving Message from", self.name)
        response = self.sqs.receive_message(
            QueueUrl=self.queue_url,
            MaxNumberOfMessages=10,
            WaitTimeSeconds=10
        )
        messages = response.get('Messages', [])
        for message in messages:
            print(f"Received message: {message['Body']}")
            # Process the message
            print("Processing message with agent:", self.name + "...")
            self.ask(message['Body'])
            print("Message processed. Removing from queue.")
            # Delete the message after processing
            self.sqs.delete_message(
                QueueUrl=self.queue_url,
                ReceiptHandle=message['ReceiptHandle']
            )

    # Add a to_dict method to the Agent class to convert to JSON serializable format
    def to_dict(self):
        return {
            "chronId": self.chronId,
            "id": self.id,
            "name": self.name,
            "dob": self.dob,
            "bank_budget": self.bank_budget,
            "bank_balance": self.bank_balance,
            "residence": self.residence,
            "brain": self.brain,
            "brain_extended": self.brain_extended,
            "nlp": "en_core_web_sm",
            "sentence_model": "all-MiniLM-L6-v2",
            "sqs": self.sqs,
            "queue_url": self.queue_url
        }
