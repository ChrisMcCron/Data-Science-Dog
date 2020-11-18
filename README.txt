                 --- DATA SCIENCE DOG ---

			  *BORK!*
			  __      _
			o'')}____//
			 `_/      )
 			 (_(_/-(_/
o               .        ___---___                    .                   
       .              .--\        --.     .     .         .
                    ./.;_.\     __/~ \.     
                   /;  / `-'  __\    . \                            
 .        .       / ,--'     / .   .;   \        |
                 | .|       /       __   |      -O-       .
                |__/    __ |  . ;   \ | . |      |
                |      /  \\_    . ;| \___|    
   .    o       |      \  .~\\___,--'     |           .
                 |     | . ; ~~~~\_    __|
    |             \    \   .  .  ; \  /_/   .
   -O-        .    \   /         . |  ~/                  .
    |    .          ~\ \   .      /  /~          o
  .                   ~--___ ; ___--~       
                 .          ---         .              

              --- AN SQL DATABASE GENERATOR ---

	          .-.               .-.
	         (   `-._________.-'   )
	          >=     _______     =<
	         (   ,-'`       `'-,   )
	          `-'               `-'

		WHAT IS DATA SCIENCE DOG?

Data science dog is an educational tool that is currently in development.

		DATA_SCI_DOG.SQL DOCUMENTATION

This .sql script must be opened in mySQL WorkBench and run first to generate the database (named data_sci_dog), the tables, and primary/
foreign key relationships among the tables.

Commented out at the bottom of the script as some SELECT, DELETE, and JOIN statements that are being kept their during the development
process. They can be utilized by you or ignored.

		DATA_SCI_DOG.PY DOCUMENTATION

This file is the main file that must be run in order to populate your database with
the data that will be generated.

Here is an explanation of the key variables and what they store. Look for the titles that are commented out with triple quotation marks
to more easily identify these variables in the script.


### ### ### ### ### ### ### SET SIMULATION PARAMETERS ### ### ### ### ### ### ### ###

sim_size: how many planets will be generated total or the size of the simulated universe. This value must be greater than journey_len.

puppy_fleet_size: how many platoons of puppies will be made that could possible be deployed to a planet as colony later in script. This value must be
greater than journey_len.

journey_len: This is the length of the journey. This value represents how many planets data science dog will visit, how many sites he will dig for bones at,
and how many puppy colonies he will make (i.e., 1 bone site, 1 puppy colony, per 1 planet visited).


### ### ### ### ### ### ### GENERATING UNIVERSE ### ### ### ### ### ### ### ###

planets: All data for planets. This includes a name, age (in billions of years, e.g., 2 = 2 billion), Earth-Similarity Index, and the number of major
	 meteor events that occured on that planet.

	 Additionally, the probability of finding a bone and actual bones found when planet is visited.
         The values for probability of finding a bone and actual bones found will be used in the tables bones and
         journeys respectively. However, since planet age, ESI, and # of meteor events are correlated with the chance
	 of finding a bone and # of bones found, they are generated at the same time as all planets.

	 To clearly see how this all is generated, go to the db_functions.py file and look at the create_planet() function.

	 To learn about the Earth-Similarity Index outside of this program, go to https://en.wikipedia.org/wiki/Earth_Similarity_Index

journey: The keys of all planets that Data Science Dog will visit. These are randomly selected from the planets variable.
	 He visits these planets in the order of which they were selected.

	 Go to db_functions.py and look at the journey_keys() function to learn more.

puppies: All possible combos of puppies that are generated that can later be randomly selected for colonies stored within a dictionary.
	 The number of puppies selected will always be the same as the journey_len variable, because Data Science Dog cannot establish a colony without
	 first visiting the planet.

	 Each puppy key-value pair in the puppy dictionary has a colony leader name, breed of all the puppies in the colony, number of puppies in colony,
	 and that colony's favourite toy.	 

	 Go to db_functions.py and look at the create_puppies() function to learn more. To see how naming of the puppy colony leader
	 works, study at the name_colony_leader() function.

colony_keys: All keys that were randomly selected from puppies for colonies. These keys selected from the puppies list can be viewed
	     as "deployed colonies" that are now active and living on planets.

bones: All bones found, the complete data set ready to be inserted into the bones table in DB stored within a dictionary.
       Each key-value pair in bones contains a type of bone, number of bones found, age of the bones (in millions, e.g., 5 = 5 million),
       and the depth the bones were found at (in meters, e.g., 100 = 100 meters).

       Go to db_functions.py and look at the dig_for_bones() function to learn more.

journey_data: all data that needs to be inserted into the journey table in DB. Contains the chance of finding
              a bone on a given planet as well per roll on a given planet. Essentially, it builds the primary 
              table in the DB.

	      You can read this dictionary as the "narrative" of what Data Science Dog did. The key-value pair
	      '1' in the dictionary will show the estimated success chance of finding a bone on the planet_id visited,
	      the unique bone_id for what was found there, and the colony_id for the puppy colony that was established on
	      that leg of the journey.

	      Go to db_functions.py to study how this is made through the journey_data() function to learn more.

### ### ### ### ### ### ### DATA INSERTION INTO SQL ### ### ### ### ### ### ### ###

    At this point in the program, all data has been generated and stored in variables. The only remaining task is to
enter all of the data into the SQL Database. The following series of loops and functions perform the task of filling
out all the SQL tables.

    When the program executes correctly, this is what you should see in mySQL:
- The tables journeys and bones tables should have no missing values.
- The planets table should only have some NULL values in journey_id (meaning the planet was not visited)
- The puppies table should only have some NULL values in planet_id (meaning that the puppies were not used to colonize a
  planet

    In mySQL Workbench, you can use the tab Database > Reverse Engineer to generate a EER (enhanced entity-relationship)
diagram that will show all the relationships among the tables. This will make everything that the program does much easier
to visualize.

    The series of loops that use the mySQL.connector cursor object to .execute() q1, q2, q3, and q4 simply are assembling
all the tables in the SQL database (i.e., journeys, planets, puppies, bones).

    The final loop that executes q5 should be made into a function at some point. It is an SQL JOIN statement that fills in
the planets table with the associated journey ID as the last step in the database creation.

### ### ### ### ### ### ### GO EXPLORE THE SQL DATABASE! ### ### ### ### ### ### ### ###

Everything should have completed without error. You may now go to mySQL workbench to explore the database created by
Data_sci_Dog.py!