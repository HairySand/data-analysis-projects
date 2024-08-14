# Assign the variables for exercise 1 here:

# I'm using type annotations to practice. Learned it online. It just is a way of labeling the type in a clear to read way.
engine_indicator_light: str = 'red blinking'
space_suits_on: bool = True
shuttle_cabin_ready: bool = True
crew_status: bool = space_suits_on and shuttle_cabin_ready
computer_status_code: int = 200
shuttle_speed: int = 15000


# Q2 BEFORE running the code, predict what will be printed to the console by the following statements: It will print "enginges are off"

# if engine_indicator_light == "green": 
#   print("engines have started")
# elif engine_indicator_light == "green blinking": 
#   print("engines are preparing to start")
# else:
#   print("engines are off")

# Q3.1
# if crew_status:
#     print("Crew Ready")
# else:
#     print("Crew not Ready")

# Q3.2
# if computer_status_code == 200:
#     print("Please Stand by. Computer is rebooting.")
# elif computer_status_code == 400:
#     print("Success! Computer online.")
# else:
#     print("ALERT: Computer offline!")

# Q3.3
if shuttle_speed > 17_500:
    print("ALERT: Escape velocity reached!")
elif shuttle_speed < 8_000:
    print("Alert: Cannot maintain orbit!")
else:
    print("Stable speed.")