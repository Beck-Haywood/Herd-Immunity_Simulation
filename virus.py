class Virus(object):
    '''Properties and attributes of the virus used in Simulation.'''

    def __init__(self, name = 'unnamed', repro_rate = 0.0, mortality_rate = 0.0):
        self.name = name
        self.repro_rate = repro_rate
        self.mortality_rate = mortality_rate

    def set_virus_cooties(self):
        self.name ='Cooties'
        self.repro_rate = .9
        self.mortality_rate = .0002

    def set_virus_vamparism(self):
        self.name = 'Vamparism'
        self.repro_rate = .01
        self.mortality_rate= 1

    def set_virus_gameAddiction(self):
        self.name = 'Addiction to Video Games'
        self.repro_rate = .1
        self.mortality_rate = .001

    def set_virus_zombie(self):
        self.name = 'Zombie Plague'
        self.repro_rate = .8
        self.mortality_rate = .99

    def set_virus_loveSickness(self):
        self.name = 'Love Sickness'
        self.repro_rate = .1
        self.mortality_rate = .5

    def set_virus_insomnia(self):
        self.name = 'Insomnia'
        self.repro_rate = .02
        self.mortality_rate = .1

def test_virus_instantiation():
    #TODO: Create your own test that models the virus you are working with
    '''Check to make sure that the virus instantiator is working.'''
    virus = Virus("HIV", 0.8, 0.3)
    assert virus.name == "HIV"
    assert virus.repro_rate == 0.8
    assert virus.mortality_rate == 0.3
    
