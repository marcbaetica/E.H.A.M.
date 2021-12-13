from time import sleep
from random import choice


class HabitatSim:
    def __init__(self):
        self.oxygen = 0
        self.nitrogen = 0
        self.other_gases = 0
        self.carbon_dioxide = 0
        self.humidity = 0
        self.barometric_pressure = 0
        self.exterior_temperature = 0
        self.interior_temperature = 0
        self.radiation_indoor = 0
        self.electricity_demand = 0
        self.electricity_supply = 0
        self.electricity_stored = 0

    def increase_temperature(self):
        self.interior_temperature = self.interior_temperature + 1

    def decrease_temperature(self):
        self.interior_temperature = self.interior_temperature - 1

    def start_simulation(self):
        while True:
            modify_temperature = choice([self.increase_temperature, self.decrease_temperature])
            modify_temperature()
            sleep(1)
