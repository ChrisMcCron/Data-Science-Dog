""" ### ### ### ### ### ### ### DATA_SCIENCE_DOG ### ### ### ### ### ### ### ###  """

from db_functions import create_planet, journey_keys, create_puppies, puppy_keys, \
    dig_for_bones, journey_data, update_puppies_planet_id

import mysql.connector

db = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = '********', # must enter password for your local database
    database = 'data_sci_dog')

c = db.cursor()

""" ### ### ### ### ### ### ### SET SIMULATION PARAMETERS ### ### ### ### ### ### ### ###  """

sim_size = 100 #must be greater than journey_len
puppy_fleet_size = 50 #must be greater than journey_len
journey_len = 25

""" ### ### ### ### ### ### ### GENERATING UNIVERSE ### ### ### ### ### ### ### ###  """

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