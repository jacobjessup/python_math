# program to find the line of refraction

import math

n1:float

sin1:float

sin1=(math.sin(math.radians(float(input("Input sin1 angle here: \n")))))

print(sin1)

n=(float(input("Input n1 here: \n")))

total1=n1*sin1

print("The first angle of refraction is: \n", total1)

n2:float

sin2:float

sin2=(math.sin(math.radians(float(input("Input sin2 angle here: \n")))))

print(sin2)

n2=(float(input("Input n2 here: \n")))

total2=n2*sin2

print("The second angle of refraction is: \n", total2)



