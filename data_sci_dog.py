""" ### ### ### ### ### ### ### DATA_SCIENCE_DOG ### ### ### ### ### ### ### ###  """

from db_functions import create_planet, journey_keys, create_puppies, puppy_keys, \
    dig_for_bones, journey_data, update_puppies_planet_id

import mysql.connector

db = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'libby69',
    database = 'data_sci_dog')

c = db.cursor()

""" ### ### ### ### ### ### ### SET SIMULATION PARAMETERS ### ### ### ### ### ### ### ###  """

"""

sim_size: how many planets will be generated total
puppy_fleet_size: how many platoons of puppies will be made that could possible be deployed to a planet
journey_len: how many planets data science dog will visit, how many archelogical sites he will dig at, and how many
             puppy colonies will be made (i.e., 1 of each per planet visited).

"""

sim_size = 100 #must be greater than journey_len
puppy_fleet_size = 50 #must be greater than journey_len
journey_len = 25

""" ### ### ### ### ### ### ### GENERATING UNIVERSE ### ### ### ### ### ### ### ###  """

"""

planets: all data for planets, plus the probability of finding a bone and actual bones found when planet is visited.
         The values for probability of finding a bone and actual bones found will be used in the tables bones and
         journeys respectively.

journey: the keys of all planets that Data Science Dog will visit.

puppies: all possible combos of puppies that can be selected for colonies.

colony_keys: all keys selected from puppies for colonies.

bones: all bones found, the complete data set ready to be inserted into the bones table in DB
journey_data: all data that needs to be inserted into the journey table in DB. Contains the chance of finding
              a bone on a given planet as well per roll on a given planet. Essentially, it builds the primary 
              table in the DB.
"""

planets = create_planet(sim_size)

journey = journey_keys(journey_len, planets)

puppies = create_puppies(puppy_fleet_size)

colony_keys = puppy_keys(journey_len, puppies)

bones = dig_for_bones(journey_len, journey, planets)

journey_data = journey_data(journey_len, planets, journey, bones, colony_keys)

""" ### ### ### ### ### ### ### TERMINAL READOUT OF ALL VARIABLES ### ### ### ### ### ### ### ###  """

print('Planets list =\n', planets, '\n')
print('Planets visited by key =\n', journey, '\n')
print('Puppies list =\n', puppies, '\n')
print('Puppy colonies by key from puppies list =\n', colony_keys, '\n')
print('Bones data set =\n', bones, '\n')
print('Journeys table data =\n', journey_data, '\n')

""" ### ### ### ### ### ### ### DATA INSERTION INTO SQL ### ### ### ### ### ### ### ###  """

"""

    At this point in the program, all data has been generated and stored in variables. The only remaining task is to
enter all of the data into the SQL Database. The following series of loops and functions perform the task of filling
out all the SQL tables

    When the program executes correctly:
- The tables journeys and bones tables should have no missing values.
- The planets table should only have NULL values in journey_id (meaning the planet was not visited)
- The puppies table should only have NULL values in planet_id (meaning that the puppies were not used to colonize a
  planet

    In mySQL Workbench, you can use the tab Database > Reverse Engineer to generate a EER (enhanced entity-relationship)
diagram that will show all the relationships among the tables.

"""

q1 = 'INSERT INTO planets (name_of_planet, age_billions, esi, meteor_events) VALUES (%s, %s, %s, %s)'

x = 1

while x <= (len(planets)):
    c.execute(q1, planets[x][0])
    x += 1
    if x == (len(planets)):
        c.execute(q1, planets[x][0])
        db.commit()
        break


q2 = 'INSERT INTO bones (bone_type, num_of_bones, age_millions, depth_meters, planet_id) VALUES (%s, %s, %s, %s, %s)'

x = 1

while x <= (len(bones)):
    c.execute(q2, bones[x])
    x += 1
    if x == (len(bones)):
        c.execute(q2, bones[x])
        db.commit()
        break

q3 = 'INSERT INTO puppies (colony_leader_name, breed, num_of_puppies, fav_toy) VALUES (%s, %s, %s, %s)'

x = 1

while x <= (len(puppies)):
    c.execute(q3, puppies[x])
    x += 1
    if x == (len(puppies)):
        c.execute(q3, puppies[x])
        db.commit()
        break


q4 = 'INSERT INTO journeys (estimated_arch_site_success_rate, planet_id, bone_id, colony_id) VALUES (%s, %s, %s, %s)'

x = 1

while x <= (len(journey_data)):
    c.execute(q4, journey_data[x])
    x += 1
    if x == (len(journey_data)):
        c.execute(q4, journey_data[x])
        db.commit()
        break

update_puppies_planet_id(puppies, colony_keys, journey) # complex function from db_functions.py used to update puppies
                                                        # table with planet_ids matching where the colony was
                                                        # established

x = 1
while x <= 1:
    q5 = 'UPDATE planets INNER JOIN journeys ON journeys.planet_id = planets.planet_id SET planets.journey_id = journeys.journey_id'
    c.execute(q5)
    db.commit()
    x += 1


""" ### ### ### ### ### ### ### GO EXPLORE THE SQL DATABASE! ### ### ### ### ### ### ### ###  """