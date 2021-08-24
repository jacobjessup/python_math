# program to find the line of refraction

import math

n:float

sin:float

sin=(math.sin(math.radians(float(input("Input sin angle here: \n")))))

print(sin)

n=(float(input("Input n here: \n")))

total=n*sin

print("The angle of refraction is: \n", total)
