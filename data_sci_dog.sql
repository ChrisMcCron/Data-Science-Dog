CREATE DATABASE data_sci_dog;

USE data_sci_dog;

CREATE TABLE journeys (
    journey_id SMALLINT AUTO_INCREMENT,
    estimated_arch_site_success_rate FLOAT, /* this is the old probability of bone */
	planet_id INT,
    bone_id SMALLINT,
    colony_id SMALLINT, /* rename this colony ID but have it point to puppy_id */
    PRIMARY KEY (journey_id)
    /* FOREIGN KEY COLONY_ID POINTS TO PUPPY_ID */
);
	
CREATE TABLE planets (
    planet_id INT AUTO_INCREMENT,
    name_of_planet VARCHAR(255),
    age_billions FLOAT,
    esi FLOAT,
    meteor_events TINYINT,
	journey_id SMALLINT,
    PRIMARY KEY (planet_id)
);
    
CREATE TABLE bones (
    bone_id SMALLINT AUTO_INCREMENT,
    bone_type VARCHAR(255),
    num_of_bones SMALLINT,
    age_millions SMALLINT,
    depth_meters SMALLINT,
    planet_id INT,
    PRIMARY KEY (bone_id)
);
    
CREATE TABLE puppies (
    puppy_id SMALLINT AUTO_INCREMENT,
    colony_leader_name VARCHAR(255),
    breed VARCHAR(255),
    num_of_puppies TINYINT,
    fav_toy VARCHAR(255),
    planet_id INT,
    PRIMARY KEY (puppy_id)
);
    
/*	Hook up all foreign keys	*/

ALTER TABLE journeys
ADD FOREIGN KEY (planet_id) REFERENCES planets(planet_id) ON DELETE CASCADE,
ADD FOREIGN KEY (bone_id) REFERENCES bones(bone_id) ON DELETE CASCADE,
ADD FOREIGN KEY (colony_id) REFERENCES puppies(puppy_id) ON DELETE CASCADE;

ALTER TABLE planets
ADD FOREIGN KEY (journey_id) REFERENCES journeys(journey_id) ON DELETE CASCADE;

ALTER TABLE bones
ADD FOREIGN KEY (planet_id) REFERENCES planets(planet_id) ON DELETE CASCADE;

ALTER TABLE puppies
ADD FOREIGN KEY (planet_id) REFERENCES planets(planet_id) ON DELETE CASCADE;

/*	The database is complete!	*/

SELECT * FROM journeys;
SELECT * FROM planets;
SELECT * FROM bones;
SELECT * FROM puppies;

/*DELETE FROM planets;
DELETE FROM journeys;
DELETE FROM puppies;
DELETE FROM bones;

ALTER TABLE planets
AUTO_INCREMENT = 1;
ALTER TABLE journeys
AUTO_INCREMENT = 1;
ALTER TABLE puppies
AUTO_INCREMENT = 1;
ALTER TABLE bones
AUTO_INCREMENT = 1;*/

/*UPDATE planets
INNER
  JOIN journeys
    ON journeys.planet_id = planets.planet_id 
   SET planets.journey_id = journeys.journey_id;*/

/* DROP DATABASE data_sci_dog2; */
