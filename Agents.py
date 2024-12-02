from game import Agent
from game import Directions
import random

class BetterRandomAgent(Agent):
    def getAction(self, state):
        random_numbers = [random.randint(1, 4) for _ in range(1)]
        randomKey = {1: 'WEST', 2: 'EAST', 3: 'SOUTH', 4: 'NORTH'}
        print(randomKey[random.randint(1, 4)])
        if randomKey[random.randint(1, 4)] == 'WEST' and Directions.WEST in state.getLegalPacmanActions():
            if Directions.STOP in state.getLegalPacmanActions():
                if randomKey[random.randint(1, 4)] == 'SOUTH' and Directions.SOUTH in state.getLegalPacmanActions():
                    return Directions.SOUTH
            return Directions.WEST
        else:
            print("Stopping.")
            return Directions.STOP


class RandomAgent(Agent):
    def getAction(self, state):
        random_numbers = [random.randint(1, 4) for _ in range(1)]
        randomKey = {1: 'WEST', 2: 'EAST', 3: 'SOUTH', 4: 'NORTH'}
        print(randomKey[random.randint(1, 4)])
        if randomKey[random.randint(1, 4)] == 'WEST' and Directions.WEST in state.getLegalPacmanActions():
            return Directions.WEST
        elif randomKey[random.randint(1, 4)] == 'SOUTH' and Directions.SOUTH in state.getLegalPacmanActions():
            return Directions.SOUTH
        elif randomKey[random.randint(1, 4)] == 'EAST' and Directions.EAST in state.getLegalPacmanActions():
            return Directions.EAST
        else:
            print("Stopping.")
            return Directions.STOP


class DumbAgent(Agent):
    "an agent that goes west until it can't"
    def getAction(self, state):
        "The agent receives a GameState (defined in pacman.py)."
        print("Location: ", state.getPacmanPosition())
        print("Actions available: ", state.getLegalPacmanActions())
        if Directions.SOUTH in state.getLegalPacmanActions():
            print("Going West.")
            return Directions.SOUTH
        else:
            print("Stopping.")
            return Directions.STOP

