class Logger(object):
    ''' Utility class responsible for logging all interactions during the simulation. '''
    # TODO: Write a test suite for this class to make sure each method is working
    # as expected.

    # PROTIP: Write your tests before you solve each function, that way you can
    # test them one by one as you write your class.

    def __init__(self, file_name):
        # √:  Finish this initialization method. The file_name passed should be the
        # full file name of the file that the logs will be written to.
        self.file_name = file_name

    def write_metadata(self, pop_size, vacc_percentage, virus_name, mortality_rate): #had basic_repro_num
        '''
        The simulation class should use this method immediately to log the specific
        parameters of the simulation as the first line of the file.
        '''
        # √: Finish this method. This line of metadata should be tab-delimited
        # it should create the text file that we will store all logs in.
        # TIP: Use 'w' mode when you open the file. For all other methods, use
        # the 'a' mode to append a new log to the end, since 'w' overwrites the file.
        # NOTE: Make sure to end every line with a '/n' character to ensure that each
        # event logged ends up on a separate line!
        file = open(self.file_name, 'w+')
        file.write(f"Population size: {pop_size}\n" +
        f"Vaccination percentage: {vacc_percentage}\n" +
        f"Virus name: {virus_name}\n" +
        f"Mortality rate: {mortality_rate}\n")
        #f"Basic reproduction number: {basic_repro_num}\n")
        file.close()

    def log_interaction(self, person, random_person, random_person_sick=None,
                        random_person_vacc=None, did_infect=None):
        '''
        The Simulation object should use this method to log every interaction
        a sick person has during each time step.

        The format of the log should be: "{person.ID} infects {random_person.ID} \n"

        or the other edge cases:
            "{person.ID} didn't infect {random_person.ID} because {'vaccinated' or 'already sick'} \n"
        '''
        # √ Finish this method. Think about how the booleans passed (or not passed)
        # represent all the possible edge cases. Use the values passed along with each person,
        # along with whether they are sick or vaccinated when they interact to determine
        # exactly what happened in the interaction and create a String, and write to your logfile.
        file = open(self.file_name, 'a')
        if did_infect and not random_person_vacc and not random_person_sick:
            file.write(f"{random_person._id} was infected by {person._id}\n")
        elif not did_infect:
            if random_person_sick:
                file.write(f"{random_person._id} and {person._id} are both sick, and cannot infect eachother\n")
            elif random_person_vacc:
                file.write(f"{random_person._id} through the power of vaccination dodged getting infected by {person._id}\n")
        file.close()

    def log_infection_survival(self, person):
        ''' The Simulation object uses this method to log the results of every
        call of a Person object's .resolve_infection() method.

        The format of the log should be:
            "{person.ID} died from infection\n" or "{person.ID} survived infection.\n"
        '''
        # √: Finish this method. If the person survives, did_die_from_infection
        # should be False.  Otherwise, did_die_from_infection should be True.
        # Append the results of the infection to the logfile
        living = person.did_survive_infection()
        file = open(self.file_name, 'a')
        if living:
            file.write(f"{person._id} survived the infection and is now vaccinated\n")
            file.close()
            return True          
        else:
            file.write(f"{person._id} died from the infection\n")
            file.close()
            return False

    def log_time_step(self, time_step_number, infected_this_step, died_this_step, death_count):
        ''' STRETCH CHALLENGE DETAILS:

        If you choose to extend this method, the format of the summary statistics logged
        are up to you.

        At minimum, it should contain:
            The number of people that were infected during this specific time step.
            The number of people that died on this specific time step.
            The total number of people infected in the population, including the newly infected
            The total number of dead, including those that died during this time step.

        The format of this log should be:
            "Time step {time_step_number} ended, beginning {time_step_number + 1}\n"
        '''
        # √: Finish this method. This method should log when a time step ends, and a
        # new one begins.
        # NOTE: Here is an opportunity for a stretch challenge!
        #I tried making it neat, I also am assuming these variables will be easily passed in from the simulation code. :)
        file = open(self.file_name, "a")
        file.write(" * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *\n" +
        f"Number of people infected during time step {time_step_number}, {infected_this_step}\n" +
        f"Number of people that died during time step {time_step_number}, {died_this_step}\n" +
        f"World death count: {death_count}\n" +
        f"Time step {time_step_number} ended, beginning {time_step_number + 1}\n" +
        f" * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *")
        file.close()