from random import randint
from numpy import random #I imported this because random.seed was giving error, this could be wrong import
random.seed(42)
from virus import Virus


class Person(object):
    ''' Person objects will populate the simulation. '''

    def __init__(self, _id, is_vaccinated, infection=None):
        ''' We start out with is_alive = True, because we don't make vampires or zombies.
        All other values will be set by the simulation when it makes each Person object.

        If person is chosen to be infected when the population is created, the simulation
        should instantiate a Virus object and set it as the value
        self.infection. Otherwise, self.infection should be set to None.
        '''
        self._id = None  # int
        self.is_alive = True  # boolean
        self.is_vaccinated = None  # boolean
        self.infection = None  # Virus object or None
        self.virus = Virus('name', 0, 0)
    def did_survive_infection(self):
        ''' Generate a random number and compare to virus's mortality_rate.
        If random number is smaller, person dies from the disease.
        If Person survives, they become vaccinated and they have no infection.
        Return a boolean value indicating whether they survived the infection.
        '''
        mortality_rate_roll = randint(0, 100)
        if not self.infection == None:
            if mortality_rate_roll > self.virus.mortality_rate:
                self.is_alive = False
            else:
                self.is_vaccinated = True
                self.infection = None
        return self.is_vaccinated and self.is_alive and self.infection
        # Only called if infection attribute is not None.
        # TODO:  Finish this method. Should return a Boolean

