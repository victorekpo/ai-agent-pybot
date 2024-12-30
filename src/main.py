import time

from src.agents.vic_bot import create_vic_bot


def main():
    # Start some tests
    start_time = time.time()

    vic_bot = create_vic_bot()

    # Collect information from a web url about typescript
    parse_web_start = time.time()
    vic_bot.parse_web("https://www.telerik.com/blogs/mastering-typescript-benefits-best-practices")
    parse_web_end = time.time()
    print(f"Parsing web information took {parse_web_end - parse_web_start:.2f} seconds")

    # Ask a question
    ask_start = time.time()
    vic_bot.ask("What is typescript?")
    ask_end = time.time()
    print(f"Asking question took {ask_end - ask_start:.2f} seconds")

    # Learn some new things
    learn_start = time.time()
    vic_bot.learn("coding", "Typescript", "TypeScript is a strongly typed superset of JavaScript")
    vic_bot.learn("coding", "Java-Completeable-Futures",
                  "Completeable-Futures are awesome, they allow you to run asynchronous code in java")
    vic_bot.learn("coding", "Java-Completeable-Futures",
                  "Completeable-Futures are awesome, they allow you to run asynchronous code in java")
    vic_bot.learn("coding", "Java-Completeable-Futures",
                  "You can create Completeable Futures by...CompletableFuture.supplyAsync(() -> {return 42;})")
    learn_end = time.time()
    print(f"Learning took {learn_end - learn_start:.2f} seconds")

    # End tests
    end_time = time.time()
    print(f"Total elapsed time: {end_time - start_time:.2f} seconds")


if __name__ == "__main__":
    main()
