# This program prompts for a length of time in seconds. 

import math

total_seconds = int(input("Enter Length of Time in Seconds: "))

seconds_in_minutes = 60 
seconds_in_hour = 60
seconds_in_day = 86400
seconds_in_year = 31536000

year(s) = total_seconds // seconds_in_year

day(s) = total_seconds // seconds_in_day

hour(s) = total_seconds // seconds_in_hour

minute(s) = total_seconds // seconds_in_minutes

seconds = total_seconds

print("Year(s):", year(s))
print("Day(s0:", day(s))
print("Hour(s):", hour(s))
print("Minute(s):", minute(s))
print("Second(s):", second(s))
