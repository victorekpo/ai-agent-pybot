from src.classes.agent.intent_actions.balance import get_balance

intent_actions = {
    "greet": lambda: "Hello! How can I help you today?",
    "goodbye": lambda: "Goodbye! Have a great day!",
    "affirm": lambda: "I'm glad I could help!",
    "deny": lambda: "I'm sorry I couldn't help.",
    "typescript": lambda: "TypeScript is a statically typed superset of JavaScript.",
    "get_account_balance": get_balance,
}
