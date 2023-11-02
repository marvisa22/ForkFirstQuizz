import pets_db

################################################################################
#     ____                          __     _                          __ __
#    / __ \  __  __  ___    _____  / /_   (_)  ____    ____          / // /
#   / / / / / / / / / _ \  / ___/ / __/  / /  / __ \  / __ \        / // /_
#  / /_/ / / /_/ / /  __/ (__  ) / /_   / /  / /_/ / / / / /       /__  __/
#  \___\_\ \__,_/  \___/ /____/  \__/  /_/   \____/ /_/ /_/          /_/   
#                                                                          
#  Question 4
################################################################################
#
# Instructions:
# Question 4 and Question 5 are about writing SQL. THey use the database that is 
# created in the file `pets_db.py`. 
# These questions use a database called SQLite. You do not need to install anything.
# In the file `pets_db.py` three tables are created. Data is then added to each 
# of the tables. The questions below are about how the data in each of the tables
# is related.

# Part 4.A:
# Write SQL to select the pets that are owned by nobody.
# The output should be a list of tuples in the format: (<pet name>, <species>, <age>)

sql_pets_owned_by_nobody = """

select a.name, a.species, a.age
	from animals a
	where a.animal_id not in (
	select a.animal_id
	from animals a
	inner join people_animals b on b.pet_id = a.animal_id
	inner join people c on c.person_id = b.owner_id)

"""

# Part 4.B:
# Write SQL to select how the number of pets are older than their owners. 
# The output should be an integer.

sql_pets_older_than_owner = """

select count(1)
	from animals a
	inner join people_animals b on b.pet_id = a.animal_id
	inner join people c on c.person_id = b.owner_id
	where a.age > c.age

"""

# Part 4.C: BONUS CHALLENGE! 
# Write SQL to select the pets that are owned by Bessie and nobody else.
# The output should be a list of tuples in the format: (<person name>, <pet name>, <species>)
sql_only_owned_by_bessie = """ 

	select c.name, a.name, a.species
	from animals a
	inner join people_animals b on b.pet_id = a.animal_id
	inner join people c on c.person_id = b.owner_id
	where c.name = 'bessie'
	order by c.person_id, a.animal_id

"""