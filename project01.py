# This program prompts for a length of time in seconds. 

total_seconds = int(input("Enter Length of Time in Seconds: "))

seconds_in_minutes = 60 
seconds_in_hour = 3600
seconds_in_day = 86400
seconds_in_year = 31536000

years = total_seconds // seconds_in_year
total_seconds -= years * seconds_in_year

days = total_seconds // seconds_in_day
total_seconds -= days * seconds_in_day

hours = total_seconds // seconds_in_hour
total_seconds -= hours * seconds_in_hour

minutes = total_seconds // seconds_in_minutes
total_seconds -= minutes * seconds_in_minutes

seconds = total_seconds

print("Years:", years)
print("Days:", days)
print("Hours:", hours)
print("Minutes:", minutes)
print("Seconds:", seconds)
