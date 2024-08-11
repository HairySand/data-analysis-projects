# 1. Declare and assign the variables here:

Name_of_shuttle = "Determination"
Shuttle_speed_mph = 17500
d_Mars_km = 225 * 10**6
d_Moon_km = 384400
m_p_km = 0.621

# 2. Use print() to print the 'type' each variable. Print one item per line.
print(type(Name_of_shuttle))
print(type(Shuttle_speed_mph))
print(type(d_Mars_km))
print(type(d_Moon_km))
print(type(m_p_km))

# Code your solution to exercises 3 and 4 here:
miles_to_mars = (d_Mars_km * m_p_km)
hours_to_mars = (miles_to_mars / Shuttle_speed_mph)
days_to_mars = (hours_to_mars/24)

print('"'+Name_of_shuttle, "will take", round(days_to_mars, 2), 'days to reach Mars."')

# Code your solution to exercise 5 here
miles_to_moon = (d_Moon_km * m_p_km)
hours_to_moon = (miles_to_moon / Shuttle_speed_mph)
days_to_moon = (hours_to_moon/24)

print('"'+Name_of_shuttle, "will take", round(days_to_moon, 2), 'days to reach the Moon."')