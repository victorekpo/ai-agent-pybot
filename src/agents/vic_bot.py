import time

from src.classes.agent.Agent import Agent


def create_vic_bot():
    load_start = time.time()
    vic_bot = Agent("vicBot")
    vic_bot.load_brain_extended()
    vic_bot.load_brain()
    vic_bot.live("Milwaukee, Wisconsin")
    load_end = time.time()

    print(f"Agent Chronological ID: {vic_bot.chronId}")
    print(f"Agent ID: {vic_bot.id}")
    print(f"Agent Name: {vic_bot.name}")
    print(f"Agent Date of Birth: {vic_bot.dob}")
    print(f"Agent Bank Budget: {vic_bot.bank_budget}")
    print(f"Loading agent took {load_end - load_start:.2f} seconds")

    # Set monthly budget
    budget_start = time.time()
    vic_bot.set_monthly_budget({"income": 5000, "expenses": 3000})
    budget_end = time.time()
    print(f"Setting monthly budget took {budget_end - budget_start:.2f} seconds")

    # Get account balance
    balance_start = time.time()
    vic_bot.get_account_balance()
    balance_end = time.time()
    print(f"Getting account balance took {balance_end - balance_start:.2f} seconds")

    # Get monthly budget
    monthly_budget_start = time.time()
    vic_bot.get_monthly_budget()
    monthly_budget_end = time.time()
    print(f"Getting monthly budget took {monthly_budget_end - monthly_budget_start:.2f} seconds")

    return vic_bot
