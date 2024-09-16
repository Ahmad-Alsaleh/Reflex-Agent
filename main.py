from agent import Agent
from map import draw_map

draw_map()

agent = Agent()

while True:
    if agent.reached_goal():
        print("Goal reached!")
        agent.stop()
        break

    if not agent.is_in_front_of_wall():
        agent.move_forward()

    # if agent

    # Write your code here. Use the `agent` object to move the around the map
