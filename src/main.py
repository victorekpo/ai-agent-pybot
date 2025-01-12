import time

from src.agents.vic_bot import vic_bot_1
from src.classes.agent.train_intent_model import train_intent_model
from src.server.server import run_server


def main():
    start_time = time.time()

    TRAINING_DATA = [
        ("What is my account balance?", {"cats": {"get_account_balance": 1.0}}),
        ("Set my monthly budget to 500", {"cats": {"set_monthly_budget": 1.0}}),
        ("What is Typescript?", {"cats": {"typescript": 1.0}}),
        ("typescript", {"cats": {"typescript": 1.0}}),
        # Add more training examples here
    ]
    train_intent_model(TRAINING_DATA)

    # Collect information from a web url about typescript
    parse_web_start = time.time()
    vic_bot_1.parse_web("https://www.telerik.com/blogs/mastering-typescript-benefits-best-practices")
    parse_web_end = time.time()
    print(f"Parsing web information took {parse_web_end - parse_web_start:.2f} seconds")

    # Ask a question
    ask_start = time.time()
    vic_bot_1.ask("What is typescript?")
    ask_end = time.time()
    print(f"Asking question took {ask_end - ask_start:.2f} seconds")

    # Learn some new things
    learn_start = time.time()
    vic_bot_1.learn("coding", "Typescript", "TypeScript is a strongly typed superset of JavaScript")
    vic_bot_1.learn("coding", "Java-Completeable-Futures",
                    "Completeable-Futures are awesome, they allow you to run asynchronous code in java")
    vic_bot_1.learn("coding", "Java-Completeable-Futures",
                    "Completeable-Futures are awesome, they allow you to run asynchronous code in java")
    vic_bot_1.learn("coding", "Java-Completeable-Futures",
                    "You can create Completeable Futures by...CompletableFuture.supplyAsync(() -> {return 42;})")
    learn_end = time.time()
    print(f"Learning took {learn_end - learn_start:.2f} seconds")

    # End tests
    end_time = time.time()
    print(f"Total elapsed time: {end_time - start_time:.2f} seconds")

    # Start the server, last action
    run_server()

    # # Sleep for 15 minutes (900 seconds)
    # time.sleep(900)


if __name__ == "__main__":
    main()
