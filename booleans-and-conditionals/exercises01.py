# Assign the variables for exercise 1 here:

# I'm using type annotations to practice. Learned it online. It just is a way of labeling the type in a clear to read way.
engine_indicator_light: str = 'red blinking'
space_suits_on: bool = True
shuttle_cabin_ready: bool = True
crew_status: bool = space_suits_on and shuttle_cabin_ready
computer_status_code: int = 200
shuttle_speed: int = 15000


# Q2 BEFORE running the code, predict what will be printed to the console by the following statements: It will print "enginges are off"

if engine_indicator_light == "green": 
  print("engines have started")
elif engine_indicator_light == "green blinking": 
  print("engines are preparing to start")
else:
  print("engines are off")