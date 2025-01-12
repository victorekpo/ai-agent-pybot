from src.agents.agents import create_agent

residence = "Somewhere, TX"
income = 5000
expenses = 3000

vic_bot_1 = create_agent(
    name="vicBot-001",
    residence=residence,
    bank_budget={"income": income, "expenses": expenses}
)

vic_bot_2 = create_agent(
    name="vicBot-002",
    residence=residence,
    bank_budget={"income": income, "expenses": expenses}
)
