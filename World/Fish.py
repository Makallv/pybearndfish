class Fish:
    """A class to represent a fish"""

    FISH_COUNT = 0  # class variable to keep track of total number of fish in the world

    FISH_LIST: list = []

    def __init__(self, species: str, size: int, count=10000):
        """
        Initialize a new fish object.

        Parameters:
        species (str): the species of the fish
        size (int): the size of the fish
        count (int): the number of fish in the world
        """
        self.species = species
        self.size = size
        self.FISH_COUNT += count  # set the count of fish in the world
        self.FISH_LIST.append(self)
