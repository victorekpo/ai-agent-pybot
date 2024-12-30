import time

from src.agents.classes.agent.Agent import Agent


def main():
    start_time = time.time()

    load_start = time.time()
    agent = Agent("vicBot")
    agent.load_brain_extended()
    agent.load_brain()
    agent.live("Milwaukee, Wisconsin")
    load_end = time.time()
    print(f"Agent Chronological ID: {agent.chronId}")
    print(f"Agent ID: {agent.id}")
    print(f"Agent Name: {agent.name}")
    print(f"Agent Date of Birth: {agent.dob}")
    print(f"Agent Bank Budget: {agent.bank_budget}")
    print(f"Loading agent took {load_end - load_start:.2f} seconds")

    scrape_start = time.time()
    agent.parse_web("https://www.telerik.com/blogs/mastering-typescript-benefits-best-practices")
    scrape_end = time.time()
    print(f"Scraping and adding took {scrape_end - scrape_start:.2f} seconds")

    ask_start = time.time()
    agent.ask("What is typescript?")
    ask_end = time.time()
    print(f"Asking question took {ask_end - ask_start:.2f} seconds")

    budget_start = time.time()
    agent.set_monthly_budget({"income": 5000, "expenses": 3000})
    budget_end = time.time()
    print(f"Setting monthly budget took {budget_end - budget_start:.2f} seconds")

    balance_start = time.time()
    agent.get_account_balance()
    balance_end = time.time()
    print(f"Getting account balance took {balance_end - balance_start:.2f} seconds")

    monthly_budget_start = time.time()
    agent.get_monthly_budget()
    monthly_budget_end = time.time()
    print(f"Getting monthly budget took {monthly_budget_end - monthly_budget_start:.2f} seconds")

    learn_start = time.time()
    agent.learn("coding", "Typescript", "TypeScript is a strongly typed superset of JavaScript")
    agent.learn("coding", "Java-Completeable-Futures",
                "Completeable-Futures are awesome, they allow you to run asynchronous code in java")
    agent.learn("coding", "Java-Completeable-Futures",
                "Completeable-Futures are awesome, they allow you to run asynchronous code in java")
    agent.learn("coding", "Java-Completeable-Futures",
                "You can create Completeable Futures by...CompletableFuture.supplyAsync(() -> {return 42;})")
    learn_end = time.time()
    print(f"Learning took {learn_end - learn_start:.2f} seconds")

    save_start = time.time()
    agent.save_brain_extended()
    agent.save_brain()
    save_end = time.time()
    print(f"Saving brain took {save_end - save_start:.2f} seconds")

    end_time = time.time()
    print(f"Total elapsed time: {end_time - start_time:.2f} seconds")


if __name__ == "__main__":
    main()
