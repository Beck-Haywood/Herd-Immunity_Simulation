import random
import sys
from person import Person
from logger import Logger
from virus import Virus
random.seed(42)


class Simulation(object):
    """Main class that will run the herd immunity simulation program.
    Expects initialization parameters passed as command line arguments when
    file is run.
    Simulates the spread of a virus through a given population.  The percentage
    of the
    population that are vaccinated, the size of the population, and the amount
    of initially
    infected people in a population are all variables that can be set when the
    program is run.
    """

    def __init__(self, pop_size, vacc_percentage, virus, initial_infected=1):
        """
        Logger object logger records all events during the simulation.
        Population represents all Persons in the population.
        The next_person_id is the next available id for all created Persons,
        and should have a unique _id value.
        The vaccination percentage represents the total percentage of
        population vaccinated at the start of the simulation.
        You will need to keep track of the number of people currently infected
        with the disease.
        The total infected people is the running total that have been infected
        since the
        simulation began, including the currently infected people who died.
        You will also need to keep track of the number of people that have die
        as a result
        of the infection.
        All arguments will be passed as command-line arguments when the file is
        run.
        HINT: Look in the if __name__ == "__main__" function at the bottom.
        """
        # √: Create a Logger object and bind it to self.logger.
        # Remember to call the appropriate logger method in the corresponding
        # parts of the simulation.
        # √: Call self._create_population() and pass in the correct
        # parameters.
        # Store the array that this method will return in the self.population
        # attribute.
        # √: Store each newly infected person's ID in newly_infected
        # attribute.
        # At the end of each time step, call self._infect_newly_infected()
        # and then reset .newly_infected back to an empty list.
        self.logger = Logger('logs.txt')
        self.population = [None] # List of Person objects, initialized to the length of our population size
        self.pop_size = pop_size  # Int
        self.next_person_id = 0  # Int
        self.virus = virus  # Virus object
        self.initial_infected = initial_infected  # Int
        self.total_infected = 0  # Int
        self.current_infected = 0  # Int
        self.vacc_percentage = vacc_percentage  # float between 0 and 1
        self.total_dead = 0  # Int
        self.file_name = "{}_simulation_pop_{}_vp_{}_infected_{}.txt".format( 
            virus.name, pop_size, vacc_percentage, initial_infected)
        self.newly_infected = []
        self.current_dead = 0
        self.total_dead = 0
        self.current_alive = self.pop_size
        self.vaccinated = int(vacc_percentage*pop_size) 

        #Gengi this is why we had nothing logging, I never added it to sim haha.
        #self.logger.write_metadata(pop_size, vacc_percentage, virus.name, virus.mortality_rate)
        #self.BobRossSaved = 0
       
    def _create_population(self, initial_infected, pop_size, vacc_percentage):
        """
        This method will create the initial population.
            Args:
                initial_infected (int): The number of infected people that the
                simulation
                will begin with.
            Returns:
                list: A list of Person objects.
        """
        # √: Finish this method!  This method should be called when the
        # simulation
        # begins, to create the population that will be used. This method
        # should return
        # an array filled with Person objects that matches the specifications
        # of the
        # simulation (correct number of people in the population, correct
        # percentage of
        # people vaccinated, correct number of initially infected people).

        # Use the attributes created in the init method to create a population
        # that has
        # the correct intial vaccination percentage and initial infected.

        #create new population list and fill with people who may or may not have been vaccinated
        population = []
        for index in range(pop_size):
            #By default assume they are not vaccinated
            vaccinated = False
            #roll a random number from 0 to our population size
            vaccinated_rng = random.random()
            #if our random number is less then the population size times the vaccinated percentage, then set variable True
            #print(f' vaccinated rng = :{vaccinated_rng} vacc % = :{vacc_percentage} person vacc? :{(vaccinated_rng<= vacc_percentage)}')
            if (vacc_percentage > 0 and vaccinated_rng <= vacc_percentage):
                vaccinated = True
            one_people = Person(index,vaccinated)
            #print(f' making person index:{index} is vaccinated? chance{vaccinated_rng} of {pop_size * vacc_percentage} resulted in :{vaccinated}')a

            population.append(one_people)

        #counter of people we have successfully infected
        population_infected = 0
        #infect random people until we satisfy starting requirements
        #print (f' pop_infected: {population_infected} initial_infected: {initial_infected}')

        while initial_infected > 0 and population_infected < initial_infected:
            random_infected = random.randint(0,pop_size-1) if pop_size > 1 else 0
            #random_infected = random.randint(0,pop_size-1)
            #print (f' Checking person {random_infected} vaccinated? :{population[random_infected].is_vaccinated} infected? {population[random_infected].infection}')
            #find a person who has neither virus, or vaccination
            if (population[random_infected].is_vaccinated == False and population[random_infected].infection is None):
                population[random_infected].infection = self.virus
                population_infected += 1
                self.total_infected += 1  # Int
                self.current_infected += 1  # Int     

        return population #don't use self.population, so as to satisfy this functions requirements.

    def _simulation_should_continue(self):
        """
        The simulation should only end if the entire population is dead
        or everyone is vaccinated.
            Returns:
                bool: True for simulation should continue, False if it should end.
        """ 
        # √: Complete this helper method.  Returns a Boolean.

        continue_simulation = False #Set the default behavior to end the game
        #If one person is alive, and hasn't been vaccinated, then the simulation needs to continue
        infected = 0
        for person in self.population:
            if person.infection != None:
                infected = 0
            if person.is_alive == True and person.is_vaccinated == False:
                continue_simulation = True
                break #We've determined the simulation will continue, no need to continue checking
        if continue_simulation == True and infected == 0:
            continue_simulation = False
        return continue_simulation

    def run(self):
        """
        This method should run the simulation until all requirements for ending
        the simulation are met.
        """
        # √: Finish this method.  To simplify the logic here, use the helper method
        # _simulation_should_continue() to tell us whether or not we should continue
        # the simulation and run at least 1 more time_step.

        # √: Keep track of the number of time steps that have passed.
        # HINT: You may want to call the logger's log_time_step() method at the end of each time step.
        # √: Set this variable using a helper

        #Gengi this is why we had nothing logging, I never added it to sim haha.
        self.logger.write_metadata(pop_size, vacc_percentage, virus.name, virus.mortality_rate)

        #Initialize this counter to zero
        time_step_counter = 0
        #By default, we want the simulation to begin. We don't check, and just assume True
        should_continue = True
        #instantiate population
        self.population = self._create_population(self.initial_infected, self.pop_size, self.vacc_percentage)

        while should_continue:
            # √: for every iteration of this loop, call self.time_step() to compute another
            # round of this simulation.
            time_step_counter +=1
            #The purpose of the run()Function is to loop, not to do the work inside the loop, the work is in time_step()
            self.time_step()
            #Check if the entire population is dead or vaccinated
            should_continue = self._simulation_should_continue()
            self.logger.log_time_step(time_step_counter, self.current_infected, self.total_infected, self.total_dead)
        #This is called when the while loop is finished
        print(f'The simulation has ended after {time_step_counter} turns.')
        survived = 0
        perished = 0
        for person in self.population:
            if person.is_alive:
                survived +=1
            else:
                perished +=1
        print (f'#survived {survived} % {survived/10} ')
        print (f'#perished {perished} % {perished/10} ')
        #print (f'Bob ross saved : {self.BobRossSaved}')

    def time_step(self):
        """
        This method should contain all the logic for computing one time step
        in the simulation.
        This includes:
            1. 100 total interactions with a randon person for each infected
            person in the population
            2. If the person is dead, grab another random person from the
            population.
                Since we don't interact with dead people, this does not count
                as an interaction.
            3. Otherwise call simulation.interaction(person, random_person) and
                increment interaction counter by 1.
        """
        #go through everyone in our population list
        for infected in self.population:
            #print(f'person # {infected._id}')
            #check if they are infected
            if infected.infection != None and infected.is_alive == True:
                #print(f'infection found in person# {infected._id}')
                #start counting interactions
                interactions = 0
                #up to 100
                while interactions <100:
                    #interact with a random person
                    rng = random.randint(0,self.pop_size-1)
                    #print(f'person # {infected._id} interactions left {100-interactions} rng# {rng}')
                    #dead people don't count
                    if self.population[rng].is_alive == True:
                        interactions +=1
                        #give the random person a chance to become infected
                        self.interaction(infected, self.population[rng])
        #We've determined newly infected, update status of current infected
        self._infect_newly_infected()
        # √: Finish this method.

    def interaction(self, person, random_person):
        """
        This method should be called any time two living people are selected
        for an
        interaction. It assumes that only living people are passed in as
        parameters.
        Args:
            person1 (person): The initial infected person
            random_person (person): The person that person1 interacts with.
        """
        # Assert statements are included to make sure that only living people
        # are passed
        # in as params
        assert person.is_alive is True
        assert random_person.is_alive is True

        # √: Finish this method.
        #  The possible cases you'll need to cover are listed below:
        # random_person is vaccinated:
        #     nothing happens to random person.
        # random_person is already infected:
        #     nothing happens to random person.
        # random_person is healthy, but unvaccinated:
        #     generate a random number between 0 and 1.  If that number is
        # smaller
        #     than repro_rate, random_person's ID should be appended to
        #     Simulation object's newly_infected array, so that their .infected
        #     attribute can be changed to True at the end of the time step.
        # ??? TODO: Call slogger ??? method during this method.

        #assume the worst
        #Note to TA, that this replaces the 'person.did_survive_invection()' method
        infected = True 
        #check if vaccinated, already infected, and just lucky to not catch the virus.
        if random_person.is_vaccinated == True:
            #self.BobRossSaved +=1
            infected = False
        elif random_person.infection != None:
            infected = False
        else:
            infection_rng = random.random()
            if infection_rng > self.virus.repro_rate:
                infected = False

        #storing only the persons _id to send them off to be later infected.
        if (infected):
            self.newly_infected.append(random_person._id)

    def _infect_newly_infected(self):
        """
        This method should iterate through the list of ._id stored in
        self.newly_infected
        and update each Person object with the disease.
        """

        # √: Call this method at the end of every time step and infect each
        # Person.
        # √: Once you have iterated through the entire list of
        # self.newly_infected, remember
        # to reset self.newly_infected back to an empty list.

        #currently infected individuals will live or die
        for person in self.population:
            if (person.is_alive):
                survived = person.did_survive_infection()
                if (survived == False):
                    self.current_dead -= 1
                    self.total_dead += 1
                    self.current_alive -= 1
                else :
                    self.vaccinated += 1
                #print (f'infected person #{person._id} survied?:{survived}')
            # TODO: Put a check if False here to be able to count how many died this round

        #This infects people so they can infect others on the next cycle
        for _id in self.newly_infected:
            self.population[_id].infection = self.virus
        self.newly_infected = []

if __name__ == "__main__":
    params = sys.argv[1:]
    virus_name = str(params[0])
    repro_num = float(params[1])
    mortality_rate = float(params[2])

    pop_size = int(params[3])
    vacc_percentage = float(params[4])

    if len(params) == 6:
        initial_infected = int(params[5])
    else:
        initial_infected = 1

    virus = Virus(virus_name, repro_num, mortality_rate)
    #print (f'Virus {virus.name} with a reproduction rate of %{virus.repro_rate*100} and mortality rate of %{virus.mortality_rate*100}')
    sim = Simulation(pop_size, vacc_percentage, virus, initial_infected)

    #virus.set_virus_cooties()

    sim.run()