# tests.py

import unittest
from simulation import Simulation 
from virus import Virus
from person import Person

class TestStringMethods(unittest.TestCase):
    def test__create_population(self):
        """create population length, and number of initial infected/vacc"""
        virus = Virus()
        virus.set_virus_cooties()
        simulation = Simulation(1000,.1,virus)
        simulation.virus = virus
        population = simulation._create_population(10, 1000, .1)
        infected = 0
        vaccinated = 0
        for person in population:
            if person.infection != None:
                infected +=1
            if person.is_vaccinated != False:
                vaccinated +=1
        assert (len(population) == 1000), "length of population is not 1000"
        assert infected == 10, "there is not only 1 person infected"
        #we cannot test the actual number of people vaccinated because it is a percentage, and dependant on random       
    
    def test__simulation_should_continue(self):
        virus = Virus('harmless',0,0)
        simulation = Simulation(1,0,virus)
        simulation.virus = virus
        #npc = Person(0,True)
        population = simulation._create_population(0, 1, 0)
        simulation.population = population
        assert len(simulation.population) == 1
        assert simulation.population[0].is_alive == True
        assert simulation.population[0].is_vaccinated == False
        assert simulation._simulation_should_continue() == True, "Created an individual who is neither infected nor vaccinated. resulted in False"
        #simulation.virus = virus
        simulation.population[0].is_alive = False
        assert simulation._simulation_should_continue() == False, "Created an individual who died to the virus resulted in True"

    def test_interaction(self):
        virus = Virus('deadly',1,.5)
        simulation = Simulation(2,0,virus,0)
        #simulation.virus = virus
        #__init__(2,0,virus,0)
        population = simulation._create_population(0,2,0)
        Zombie = Person(0,False,virus)
        npc = Person(1,False)
        simulation.population = population
        simulation.population[0] = Zombie
        simulation.population[1] = npc
        simulation.interaction(simulation.population[0],simulation.population[1])
        assert len(simulation.newly_infected) == 1, "Our zombie hasn't passed infection on to the NPC via interaction"

    def test__infect_newly_infected(self):
        virus = Virus('deadly',1,.5)
        simulation = Simulation(2,0,virus,0)
        population = simulation._create_population(0,2,0)
        Zombie = Person(0,False,virus)
        npc = Person(1,False)
        simulation.population=population
        simulation.population[0] = Zombie
        simulation.population[1] = npc
        simulation.interaction(simulation.population[0],simulation.population[1])
        simulation._infect_newly_infected()
        assert simulation.population[1].infection != None, "Our newly infected NPC survived his deadly disease"

if __name__ == '__main__':
    unittest.main()