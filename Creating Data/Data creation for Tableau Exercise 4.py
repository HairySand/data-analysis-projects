import pandas as pd
import numpy as np
import random as rd


# print(len(date_series))  == 62
mood_list = []
meditation_list = []
exercise_list = []
sleep_list = []
slept_list = []
i=0
mood = 0


date_series = pd.date_range(start= '07/01/2024', end= '11/01/2024') #Creates series of dates.

print(range(len(date_series)))

#Below is creating data for the dates
for day in range(len(date_series)):
    exercise_time = rd.randrange(0, 121, 30) #These two lines create exercise data: 0, 30, 60, 90, or 120 mins)
    exercise_list.append(exercise_time)
    if day < 31:
        meditation_list.append([False]) #makes meditation False for days under 30
        if mood <= 1: #THis until ENDmood is creating mood random data for days under 30, should skew lower.
            mood = rd.randrange(1, 3)
        elif mood > 1 and mood < 5:
            mood = rd.randrange(2, 7)
        elif mood >= 5:
            mood = rd.randrange(2, 8)
        mood_list.append(mood) #ENDmood
        sleep_hours = rd.randrange(4, 8) #Creates Sleep time data for under 30 days
        sleep_list.append(sleep_hours)
    else:
        meditation_list.append([True]) #makes meditation True for days above 30
        if mood <= 3: # This until ENDmood is creating mood random data for days 30 and above. This should skew slightly positive.
            mood = rd.randrange(1, 11)
        elif mood > 3 and mood < 6:
            mood =rd.randrange(3, 11)
        elif mood >= 6:
            mood = rd.randrange(5, 11)
        mood_list.append(mood) #Endmood
        sleep_hours = rd.randrange(6,9) #Creates sleep time data for 30 days and over.
        sleep_list.append(sleep_hours)


#Creates lists for data
mood_series = pd.Series(mood_list)
meditation_series = pd.Series(meditation_list)
exercise_series = pd.Series(exercise_list)
sleep_series = pd.Series(sleep_list)

df = pd.DataFrame({r'Date': date_series, 'Meditation':meditation_series, 'Sleep Time (Hours)': sleep_series, 'Exercise Time (Minutes)':exercise_series, 'Mood 1(Bad) to 10 (Good)':mood_series})
df.to_csv(r'C:\Users\LC Harrison Sand\OneDrive\Documents\LaunchCode\Data Sets\Data for Tableau Exercise.csv', index=False)

    

        
