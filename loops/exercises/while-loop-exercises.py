# Define three variables for the LaunchCode shuttle - one for the starting fuel level, another for the number of astronauts aboard, and the third for the altitude the shuttle reaches.

start_fuel = 1000
top_alt = 2000
altitude = 0
num_astro  = 0
testastro = 0
testnumfuel = 0
fuel_question = "What is the starting fuel level?  "
astro_question = "How many astronauts are aboard?  "
extry =1

# Exercise #1: Construct while loops to do the following:
  # a. Query the user for the starting fuel level. Validate that the user enters a positive, integer value greater than 5000 but less than 30000. 
while extry == 1:
  try:
    start_fuel =float(input(fuel_question))
    extry = 0
  except:
    print("Needs to be a number.")
    extry = 1


while testnumfuel == 0:
  if start_fuel <5001:
    print("Fuel level too low! Fuel level must be above 5,000 kg.")
    start_fuel =float(input(fuel_question))
  elif start_fuel > 29_999:
    print("Fuel level too high! Fuel must be under 30,000 kg.")
    start_fuel =float(input(fuel_question))
  else:
    testnumfuel += 1



# b. Use a second loop to query the user for the number of astronauts (up to a maximum of 7). Validate the entry.
num_astro = float(input(astro_question))

while testastro == 0:
  if num_astro%1 != 0:
    print("There are no partial people. Number must be a whole number!")
    num_astro = float(input(astro_question))
  elif num_astro > 7:
     print("Too many Astronauts! Remove someone from the mission. Max Astronauts = 7.")
     num_astro = float(input(astro_question))
  elif num_astro <= 0:
     print("This is not an unmanned mission. Please enter at least 1 crew member!")
     num_astro = float(input(astro_question))
  else:
     int(num_astro)
     testastro += 1

       
  

  
# c. Use a final loop to monitor the fuel status and the altitude of the shuttle. Each iteration, decrease the fuel level by 100 units for each astronaut aboard. Also, increase the altitude by 50 kilometers.

# while start_fuel >0:
#   altitude += 50
#   start_fuel -= 100 * num_astro
# print("Ran out of fuel at", altitude, "feet.")

# Exercise #2: Print the result with the phrase, The shuttle gained an altitude of ___ km and has ___ kg of fuel left. Fill in the blanks with the altitude and fuel level values.
# If the altitude is 2000 km or higher, add “Orbit achieved!” Otherwise add, “Failed to reach orbit.”

while start_fuel >99 * num_astro and altitude < 2000:
  altitude += 50
  start_fuel -= 100 * num_astro

if altitude >= 2000:
  result = "Orbit achieved!"
else:
  result = "Failed to reach orbit."
print("The shuttle gained an altitude of", altitude, "km and has", start_fuel, "kg of fuel left." , result)