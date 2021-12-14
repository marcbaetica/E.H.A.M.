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
        self.electricity_stored = 100
        self.light = 'ON'
        self.heat = 'ON'

    def increase_temperature(self):
        self.interior_temperature = self.interior_temperature + 1

    def decrease_temperature(self):
        self.interior_temperature = self.interior_temperature - 1

    def consume_electricity(self):
        if self.light == 'ON' and self.electricity_stored > 0:
            self.electricity_stored = self.electricity_stored - 1
        if self.heat == 'ON' and self.electricity_stored > 0:
            self.electricity_stored = self.electricity_stored - 1
        if self.electricity_stored == 0:
            self.light = 'OFF'
            self.heat = 'OFF'

    def start_simulation(self):
        while True:
            modify_temperature = choice([self.increase_temperature, self.decrease_temperature])
            modify_temperature()
            self.consume_electricity()
            sleep(1)
