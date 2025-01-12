import time

from src.classes.agent.Agent import Agent

agents = {}


def create_agent(name, dob=None, residence=None, bank_budget=None, bank_balance=None):
    load_start = time.time()

    # Check if the agent already exists
    if name in agents:
        print("Agent with name already exists; name=", name)
        return agents[name]

    agent = Agent(name)
    agent.load_brain_extended()
    agent.load_brain()
    load_end = time.time()

    print(f"Agent Chronological ID: {agent.chronId}")
    print(f"Agent ID: {agent.id}")
    print(f"Agent Name: {agent.name}")
    print(f"Loading agent took {load_end - load_start:.2f} seconds")

    if residence:
        live_start = time.time()
        agent.live(residence)
        live_end = time.time()
        print(f"Setting residence took {live_end - live_start:.2f} seconds")

    if bank_budget:
        budget_start = time.time()
        agent.set_monthly_budget(bank_budget)
        budget_end = time.time()
        print(f"Setting monthly budget took {budget_end - budget_start:.2f} seconds")

    if bank_balance:
        balance_start = time.time()
        agent.bank_balance = bank_balance
        balance_end = time.time()
        print(f"Setting bank balance took {balance_end - balance_start:.2f} seconds")

    # Add the agent to the global dictionary
    agents[agent.name] = agent

    # Set default agent
    if not agents.get("default"):
        print("Setting default agent", agent.name)
        agents["default"] = agent

    return agent
