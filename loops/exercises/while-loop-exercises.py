# Define three variables for the LaunchCode shuttle - one for the starting fuel level, another for the number of astronauts aboard, and the third for the altitude the shuttle reaches.

start_fuel = 1000
top_alt = 2000
altitude = 0
num_astro  = 0
testastro = 0
testnumfuel = 0

# Exercise #1: Construct while loops to do the following:
  # a. Query the user for the starting fuel level. Validate that the user enters a positive, integer value greater than 5000 but less than 30000. 
start_fuel =int(input("What is starting fuel level?  "))


while testnumfuel == 0:
  if start_fuel <5000:
    print("Fuel level too low! Fuel level must be above 5,000 kg.")
    start_fuel =int(input("What is starting fuel level?  "))
  elif start_fuel > 30_000:
    print("Fuel level too high! Fuel must be under 30,000 kg.")
    start_fuel =int(input("What is starting fuel level?  "))
  else:
    testnumfuel += 1



# b. Use a second loop to query the user for the number of astronauts (up to a maximum of 7). Validate the entry.
  
num_astro = int(input("How many astronauts are aboard?  "))

while testastro == 0:
    if num_astro > 7:
      print("Too many Astronauts! Remove someone from the mission. Max Astronauts = 7.")
      num_astro = int(input("How many astronauts are aboard? (Remember 7 or less!)  "))
    elif num_astro <= 0:
      print("This is not an unmanned mission. Please enter at least 1 crew member!")
      num_astro = int(input("How many astronauts are aboard, there must atleast be 1 astronaut for the mission to succeed.  "))
    else:
      testastro += 1
  
  
  
# c. Use a final loop to monitor the fuel status and the altitude of the shuttle. Each iteration, decrease the fuel level by 100 units for each astronaut aboard. Also, increase the altitude by 50 kilometers.

# while start_fuel >0:
#   altitude += 50
#   start_fuel -= 100 * num_astro
# print("Ran out of fuel at", altitude, "feet.")

# Exercise #2: Print the result with the phrase, The shuttle gained an altitude of ___ km and has ___ kg of fuel left. Fill in the blanks with the altitude and fuel level values.
# If the altitude is 2000 km or higher, add “Orbit achieved!” Otherwise add, “Failed to reach orbit.”

while start_fuel >99 * num_astro:
  altitude += 50
  start_fuel -= 100 * num_astro

if altitude >= 2000:
  result = "Orbit achieved!"
else:
  result = "Failed to reach orbit."
print("The shuttle gained an altitude of", altitude, "km and has", start_fuel, "kg of fuel left." , result)