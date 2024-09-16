from rich import print as pprint

from agent import Agent
from map import draw_map

draw_map()

agent = Agent()

while True:
    if agent.reached_goal():
        pprint("[green]Goal reached!")
        agent.stop()
        break

    # Write your code here. Use the `agent` object to move the around the map
