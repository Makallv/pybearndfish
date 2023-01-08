class Planet:
    def __init__(self, name: str, dry_land_area: float, water_area: float):
        """
        Initialize a new planet object.

        Parameters:
        name (str): the name of the planet
        dry_land_area (float): the area of dry land on the planet
        water_area (float): the area of water on the planet
        """
        self.name = name
        self.dry_land_area = dry_land_area
        self.water_area = water_area

    def total_area(self):
        """Calculate the total area of the planet"""
        return self.dry_land_area + self.water_area
