import random as rand
import mysql.connector

db = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'libby69',
    database = 'data_sci_dog2')

c = db.cursor()

""" ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### """

def name_colony_leader():

    ranklist = [
        'Fleet Admiral', 'Admiral', 'Vice Admiral', 'Captain', 'Commander', 'Lieutenant', 'Ensign', 'Master Chief Petty Officer', 'Senior Chief Petty Officer',
        'Chief Petty Officer']

    namelist = [
        'Ace', 'Aero', 'Albert', 'Appolo', 'Archie', 'Aspen', 'Autumn', 'Bailey', 'Bandit', 'Barkley', 'Barney', 'Baron', 'Basil', 'Baxter', 'Bean', 'Bear', 'Bingo', 'Birdie',
        'Biscuit', 'Blaze', 'Blossom', 'Bo', 'Boomer', 'Brandy', 'Brownie', 'Brutus', 'Buddy', 'Buffy', 'Butch', 'Candy', 'Carla', 'Carter', 'Casper', 'Champ', 'Chance', 'Charlie',
        'Chase', 'Chester', 'Chewy', 'Chico', 'Chip', 'Chloe', 'Cinnamon', 'Cleo', 'Clifford', 'Coco', 'Cookie', 'Cricket', 'Daisey', 'Dakota', 'Destiny', 'Dexter', 'Diesel', 'Diva',
        'Dixie', 'Dodger', 'Dolly', 'Duchess', 'Eddie', 'Ella', 'Ellie', 'Elsa', 'Emma', 'Eva', 'Faith', 'Fanny', 'Felix', 'Fern', 'Finn', 'Fiona', 'Fisher', 'Flash', 'Foxy', 'Fritz',
        'Georgia', 'Gidget', 'Ginger', 'Gizmo', 'Goldie', 'Griffin', 'Gunner', 'Gus', 'Gypsy', 'Hank', 'Hawkeye', 'Honey', 'Hoss', 'Hunter', 'Iggy', 'Ivan', 'IzzyJade', 'Jack',
        'Jackson', 'Jake', 'Jasmine', 'Jasper', 'Jax', 'Jersey', 'Juno', 'Kallie', 'Kiki', 'King', 'Kira', 'Kobe', 'Koda', 'Kona', 'Lacy', 'Lady', 'Layla', 'Leia', 'Leo', 'Leroy',
        'Levi', 'Lewis', 'Lexi', 'Libby', 'Lily', 'Lizzy', 'Logan', 'Loki', 'London', 'Louie', 'Lucky', 'Luke', 'Lulu', 'Luna', 'Mabel', 'Macy', 'Maggie', 'Marley', 'Marty', 'Matilda',
        'Maverick', 'Max', 'Maximus', 'Maya', 'Mickey', 'Miles', 'Missy', 'Misty', 'Mocha', 'Moe', 'Moose', 'Morris', 'Moxie', 'Muffin', 'Murphy', 'Nala', 'Nelson', 'Nero', 'Norm',
        'Odie', 'Odin', 'Olive', 'Oliver', 'Ollie', 'Oreo', 'Oscar', 'Otis', 'Ozzy', 'Parker', 'Peaches', 'Peanut', 'Pearl', 'Pebbles', 'Penny', 'Piper', 'Pixel', 'Pixie', 'Precious',
        'Prince', 'Princess', 'Quincy', 'Radar', 'Ralph', 'Rambo', 'Ranger', 'Rascal', 'Rebel', 'Reggie', 'Remy', 'Rex', 'Ricky', 'Rider', 'Riley', 'Ringo', 'Rocky', 'Rosco', 'Rosie',
        'Roxy', 'Rudy', 'Rufus', 'Rusty', 'Sage', 'Sam', 'Samson', 'Sarge', 'Sawyer', 'Scoobz', 'Scooter', 'Scraps', 'Shiloh', 'Simba', 'Simon', 'Snoop', 'Sparky', 'Spencer', 'Stanley',
        'Star', 'Snickers', 'Summer', 'Sunny', 'Sweetie', 'Taco', 'Taz', 'Teddy', 'Toby', 'Trapper', 'Trixie', 'Tucker', 'Violet', 'Wally', 'Walter', 'Willy', 'Winnie', 'Winston', 'Wyatt',
        'Xena', 'Yukon', 'Willow', 'Zane', 'Zelda', 'Zeus', 'Ziggy', 'Zoe']

    rank = rand.choice(ranklist)
    name = rand.choice(namelist)
    leader_name = rank + ' ' + name
    return leader_name

def name_planet():

    verbs = [
        'Shining', 'Iron', 'Burning', 'Freezing', 'Shimmering', 'Blinking', 'Drifting', 'Soaring', 'Levitating', 'Spinning', 'Rotating', 'Distant', 'Unacknowledged', 'Rising', 'Astonishing', 'Waking',
        'Blinding', 'Changing', 'Crawling', 'Creeping', 'Crying', 'Dancing', 'Desired', 'Destroyed', 'Dry', 'Engaging', 'Experimental', 'Fallen', 'Flying', 'Forbidden', 'Hanging', 'Looping',
        'Sleeping', 'Lost', 'Beloved', 'Melting', 'Decaying', 'Growing', 'Shattered', 'Broken', 'Overgrown', 'Unobserved', 'Unexplored', 'Overtaken', 'Blissful', 'Swirling', 'Thundering', 'Storming',
        'Temperate', 'Choking', 'Intoxicating', 'Electrified']

    nouns = [
        'Rock', 'Orb', 'Eye', 'Ball', 'Planet', 'Moon', 'Island', 'Constellation', 'Crystal', 'Iceland', 'Fireland', 'Jungle', 'Stranger', 'Alien Land', 'Alien Homeworld', 'Loner', 'Hermit', 'Homeworld',
        'Oceans', 'Oceanworld', 'Seas', 'Waterworld', 'Refuge', 'Retreat', 'Sanctuary', 'Dog Park', 'Kennel', 'Globe', 'Asteroid', 'Heavenly Body', 'Exo-planet', 'Trojan Planet', 'Inner Planet',
        'Coreless Planet', 'Desert', 'Silicate Planet', 'Rogue Planet', 'Pulsar Planet', 'Molten Planet', 'Molten Moon', 'Abyss', 'Void', 'Plane', 'Holy Land', 'Hellscape', 'Dunes', 'Sandworld',
        'Tropics', 'Drift', 'Mountain Planet', 'Steppes']

    alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    number = rand.randint(1,999)
    two_letters = alpha[rand.randint(0,25)] + alpha[rand.randint(0,25)]
    single_letter = alpha[rand.randint(0,25)]
    generic_name = two_letters + '-' + str(number) + single_letter

    adj_choice = rand.choice(verbs)
    noun_choice = rand.choice(nouns)
    planet_suffix = 'The ' + adj_choice + ' ' + noun_choice

    full_planet_name = generic_name + ' ' + planet_suffix
    return full_planet_name

""" ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### """


"""
The create_planets function takes an 1 parameter that is an integer equal to the number of planets you want to
create in the simulation.

The return value is a dictionary containing two notable sections within each key-value pair:
1. A list containing planet_name, age, ESI, and meteor events, visited/not visited
2. Two remaining values, the raw probability of finding a bone and the actual bones found upon visiting the planet

As the variable containing all the planets in the simulation is used through out the data_sci_dog2.py program, the
two sections above will be useful at different points in time.

The formula for bone probability can be reconfigured and any fields that can be changed without disturbing the program
 are noted in the function with a '# *' symbol.
"""


def create_planet(x):
    i = 1
    planets = {}

    while i <= x:

        planet_name = name_planet()

        age = rand.uniform(2, 13)  # * #billions of years
        age2to5 = rand.uniform(0, 0.05)  # *
        age5to9 = rand.uniform(0, 0.1)  # *
        age9to13 = rand.uniform(0.07, 0.25)  # *

        esi = round(rand.uniform(0, 0.99),
                    2)  # ESI is a value between 0 and 1, but could be modified to be more or less likely to be closed to 0 or 1. Right now it is purely random.
        low_esi = rand.uniform(0, 0.05)  # *
        med_esi = rand.uniform(0, 0.1)  # *
        high_esi = rand.uniform(0.07, 0.25)  # *

        meteor = rand.randint(0, 5)
        meteor_prob = [rand.uniform(0.01, 0.02),  # *
                       rand.uniform(0.01, 0.03),  # *
                       rand.uniform(0.01, 0.05),  # *
                       rand.uniform(0.01, 0.07),  # *
                       rand.uniform(0.01, 0.09),  # *
                       rand.uniform(0.01, 0.11)]  # *

        prob_bone = 0.01

        bone_num = 0

        j = 0

        while j <= meteor:
            if j == meteor:
                prob_bone += meteor_prob[j]
                j += 1
                break
            else:
                j += 1
                continue

        if age >= 2 and age < 5:
            prob_bone += age2to5
        if age >= 5 and age < 9:
            prob_bone += age5to9
        if age >= 9 and age <= 13:
            prob_bone += age9to13

        if esi >= 0 and esi < 0.33:
            prob_bone += low_esi
        if esi >= 0.33 and esi < 0.66:
            prob_bone += med_esi
        if esi >= 0.66 and esi <= 1:
            prob_bone += high_esi

        k = 1

        while k <= 100:
            roll = rand.uniform(0, 1)
            if roll > prob_bone:
                k += 1
                continue
            if roll <= prob_bone:
                bone_num += 1
                k += 1

        planets[i] = [[planet_name, round(age, 2), esi, meteor], round(prob_bone, 2),
                      bone_num]  # was a plain tuple before

        i += 1

    return planets


""" 
Here is some commented out print code that you can run to see how to easily parse through the dictionary to retrieve
the values you need at different points in time to fill out the entire data_sci_dog2.sql database
"""


#planets = create_planet(8)
#print(planets)
#print(planets[1])
#print(planets[1][0])
#print(planets[1][1])
#print(planets[1][2])

# def planet_idxs(n):

"""
journey_keys() takes the parametre of how many planets you would like to visit, from a dictionary of planets.

There seems to be a bug with this code where the last planet in the planets dictionary cannot be selected?
"""

def journey_keys(n, planets):
    planet_keys = rand.sample(range(1, len(planets)), n, counts=None)
    return planet_keys

#journey = journey_keys(3, planets)

""" ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### """


def create_puppies(n): #takes an para for how many total puppy colonies you want

    breed = [
        "Affenpinscher", "Afghan Hound", "Airedale Terrier", "Akita", "Alaskan Malamute", "American Bulldog", \
        "American Foxhound", "Appenzeller Sennenhund", "Australian Shepherd", "Basset Hound", "Beagle", "Bearded Collie", \
        "Bedlington Terriers", "Belgian Laekenois", "Bernese Mountain Dog", "Bichon Frise", "Bloodhound", "Bluetick Coonhound", \
        "Cane Corso", "Cardigan Welsh Corgi", "Cavalier King Charles Spaniel", "Cesky Terrier", "Chihuahua", "Chinese Crested", \
        "Chinese Shar-Pei", "Chinook", "Collie", "Dachshund", "Dalmatian", "Doberman Pinscher", "Dogue de Bordeaux", "Drever", \
        "Dutch Shepherd", "English Foxhound", "Entlebucher Mountain Dog", "Estrela Mountain Dog", "Eurasier", "Finnish Lapphund", \
        "Finnish Spitz", "Flat-Coated Retriever", "French Bulldog", "German Shorthaired Pointer", "German Pinscher", \
        "Finnish Spitz", "Flat-Coated Retriever", "French Bulldog", "German Shorthaired Pointer", "German Pinscher", \
        "German Shepherd", "German Spitz", "Giant Schnauzer", "Golden Retriever", "Grand Basset Griffon Vendéen", \
        "Great Dane", "Greyhound", "Harrier", "Havanese", "Hokkaido", "Hovawart", "Ibizan Hound", "Icelandic Sheepdog", \
        "Irish Setter", "Irish Terrier", "Irish Wolfhound", "Italian Greyhound", "Jagdterrier", "Japanese Chin", "Jindo", \
        "Kai Ken", "Karelian Bear Dog", "Kishu Ken", "Komondor", "Kromfohrlander", "Kuvasz", "Labrador Retriever", \
        "Lagotto Romagnolo", "Lancashire Heeler", "Leonberger", "Lhasa Apso", "Löwchen", "Maltese", "Mastiff", \
        "Miniature Bull Terrier", "Mountain Cur", "Mudi", "Mutt", "Newfoundland", "Norwegian Elkhound", "Norwich Terriers", \
        "Nova Scotia Duck Tolling Retriever", "Old English Sheepdog", "Otterhound", "Papillon", "Pekingese", \
        "Pembroke Welsh Corgi", "Pharaoh Hound", "Pointer", "Pomeranian", "Pug", "Puli", "Rat Terrier", "Rhodesian Ridgeback", \
        "Rottweiler", "Russell Terrier", "Russian Toy", "Russkaya Tsvetnaya Bolonka", "Saint Bernard", "Saluki", "Samoyed", \
        "Schipperke", "Scottish Deerhound", "Segugio Italiano", "Shiba Inu", "Shih Tzu", "Sloughi", "Swedish Vallhund", \
        "Teddy Roosevelt Terrier", "Tibetan Mastiff", "Tornjak", "Toy Fox Terrier", "Vizsla", "West Highland White Terrier", \
        "Whippet", "Xoloitzcuintli", "Yakutian Laikas", "Yorkshire Terrier"
    ]
    fav_toy = [
        "tennis ball", "peanut butter filled KONG", "tug o' war rope", "squeaky toy", "stuffed animal", "frisbee", "chew bone",
        "snuffle mat", "dog bed", "trash bin", "socks", "shoes", "digging holes", "chasing space bunnies"
    ]
    i = 1
    pup_dict = {}
    while i <= n:
        colony_leader_name = name_colony_leader()
        pup_breed = rand.choice(breed)
        num_of_puppies = rand.randint(12,101)
        pup_fav_toy = rand.choice(fav_toy)
        pup_dict[i] = [colony_leader_name, pup_breed, num_of_puppies, pup_fav_toy]
        i += 1
    return pup_dict

#puppies = create_puppies(10)
#print(puppies)

def puppy_keys(n, puppies):
    puppy_keys = rand.sample(range(1, len(puppies)), n, counts=None)
    return puppy_keys

#puppy_keys = puppy_keys(5, puppies)
#print(puppy_keys)

""" ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### """

def dig_for_bones(journey_len, journey, planets):

    bones_dict = {}
    bone_type_list = ['alien humanoid', 'mammalian', 'chitinous', 'metallic alloy', 'avian', 'megafauna', \
             'gargantuan piscine', 'cyborg synthetics', 'ancient reptilian', 'unknown materials']
    bone_number = [] # planets[1][2]
    bone_age = 0
    bone_depth = 0
    i = 1

    while i <= journey_len:

        bone_type = rand.choice(bone_type_list)
        journey_idx = journey[i - 1]
        num_of_bones = planets[journey_idx][2]
        age_millions = rand.randint(1,999)
        depth_meters = rand.randint(1,250)
        planet_id = journey_idx

        bones_dict[i] = [bone_type, num_of_bones, age_millions, depth_meters, planet_id]

        i += 1

    return bones_dict

#bones_found = dig_for_bones(3, journey, planets)
#print('idxs:', journey)
#print(bones_found)

""" ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### """

def journey_data(journey_len, planets, journey, bones, colony_keys):

    journey_dict = {}
    i = 1

    while i <= journey_len:

        planet_idx = journey[i - 1] #[0]
        est_arch_succ = planets[planet_idx][1]
        planet_id = planet_idx
        bone_id = i
        colony_id = colony_keys[i - 1] #[0]

        journey_dict[i] = [est_arch_succ, planet_id, bone_id, colony_id]

        i += 1

    return journey_dict

def update_puppies_planet_id(puppies, colony_keys, journey):
    query_str_list = []
    len_of_puppies = len(puppies)
    puppies_keys = [i for i in range(1, len_of_puppies + 1)]

    i = 1

    while i <= len(journey):
        for x in colony_keys:
            for b in puppies_keys:
                if x == b:
                    str1 = 'UPDATE puppies SET planet_id = '
                    str2 = str(journey[i - 1])
                    str3 = ' WHERE puppy_id = '
                    str4 = str(puppies_keys[b - 1])
                    query = ''
                    query += str1 + str2 + str3 + str4
                    i += 1
                    c.execute(query)
                    db.commit()



