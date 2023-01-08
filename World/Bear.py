from typing import Tuple, Any
import time
from World.Fish import Fish
from World.Planet import Planet
import random


class Bear:
    """A class to represent a bear"""

    ALIVE_BEARS = []  # list to keep track of alive bears

    DEAD_BEARS = []  # list of keeping track of dead bears

    def __init__(self, name: str, energy: float, starvation: float, gender: str):
        """
        Initialize a new bear object.

        Parameters:
        name (str): the name of the bear
        energy (float): the energy level of the bear
        starvation (float): the starvation level of the bear
        gender (str): the gender of the bear
        """
        self.name = name
        self.energy = energy
        self.starvation = starvation
        self.gender = gender
        Bear.ALIVE_BEARS.append(self)  # add the bear to the list of alive bears when it is created
        # self.x = x  # X coordinate for the bear
        # self.y = y  # Y coordinate for the bear

    def move(self):
        """Cause the bear to lose energy when it moves"""
        self.energy -= 10  # bear loses energy when it moves
        self.check_energy()  # check if the bear's energy has dropped below 0

    def breed(self):
        """Cause the bear to lose energy when it breeds"""
        self.energy -= 20  # bear loses energy when it breeds
        self.check_energy()  # check if the bear's energy has dropped below 0

    def eat(self, fish: Fish):
        """Cause the bear to gain starvation when it eats a fish"""
        self.starvation += fish.size
        Fish.FISH_COUNT -= 1
        self.energy -= 5

    @staticmethod
    def gain_energy(bear):
        bear.starvation = bear.starvation - (bear.starvation * 0.1)
        bear.energy = bear.energy + (bear.starvation * 0.1)

    @staticmethod
    def random_action(bear, action: int):
        if action == 1:
            bear.move()
        elif action == 2:
            bear.breed()

    def check_energy(self) -> float:
        """Check if the bear's energy has dropped below 0 and cause it to die if necessary"""
        if self.starvation == 0:
            self.energy -= 5  # bear's energy drops by 5 each second if its starvation level is 0
            time.sleep(3)
            if self.starvation > 0:
                Bear.gain_energy(self)
        return self.energy

    def die(self):
        """Cause the bear to die and be removed from the list of alive bears"""
        Bear.ALIVE_BEARS.remove(self)  # remove the bear from the list of alive bears when it dies
        Bear.DEAD_BEARS.append(self)  # add to dead bears if bear energy reaches 0
