from math import pi, cos, sin, acos 

r = Radius_of_Sphere = 6371 

Starting_Point1 = float(input("Enter Latitude Start Point: "))
Starting_Point2 = float(input("Enter Longitude Start Point: "))
Ending_Point1 = float(input("Enter Latitude End Point: "))
Ending_Point2 =  float(input("Enter Longitude Point: "))

x1 = Starting_Point1 * pi / 180
x2 = Starting_Point2 * pi / 180
y1 = Ending_Point1 * pi / 180
y2 = Ending_Point2 * pi / 180

d = r * acos(sin(x1) * sin(x2) + cos(x1) * cos(x2) * cos(y1 - y2))
d = round(d, 2)

print("The Great Circle Distance is:", d)