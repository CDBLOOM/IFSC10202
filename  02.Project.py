from math import pi, cos, sin, acos 

r = Radius_of_Sphere = 6371

Starting_Lat = float(input("Enter Latitude Start Point: "))
Starting_Long= float(input("Enter Longitude Start Point: "))
Ending_Lat = float(input("Enter Latitude End Point: "))
Ending_Long =  float(input("Enter Longitude Point: "))

Lat1 = Starting_Lat * pi / 180
Long1= Starting_Long * pi / 180
Lat2 = Ending_Lat * pi / 180
Long2 = Ending_Long * pi / 180

d = r * acos(sin(Lat1) * sin(Lat2) + cos(Lat1) * cos(Lat2) * cos(Long1 - Long2))
d = round(d, 2)

print("The Great Circle Distance is:", d)
