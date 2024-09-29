from rich import print as pprint

from agent import Agent
from configs import settings
from map import draw_map

draw_map()

agent = Agent()

while True:
    if settings.enable_steps:
        response = input("Press Enter to move one iteration or `Q` to quit... ")
        if response.lower() == "q":
            pprint("[blue] Quitting...")
            break
    if agent.reached_goal():
        pprint("[green]Goal reached!")
        agent.stop()
        break

    # Write your code here. Use the `agent` object to move the around the map
