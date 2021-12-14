from habitat_simulation import HabitatSim
from threading import Thread
from time import sleep


hab = HabitatSim()
hab_simulation = Thread(target=hab.start_simulation)
hab_simulation.start()

while True:
    print(hab.light, hab.heat, hab.electricity_stored, hab.interior_temperature)
    sleep(1)
