# program to find the line of refraction

import math

n1:float

sin1:float

sin1=(math.sin(math.radians(float(input("Input sin1 angle here: \n")))))

print(sin1)

n1=(float(input("Input n1 here: \n")))

total1=n1*sin1

print("The first angle of refraction is: \n", total1)

n2:float

sin2:float

sin2=(math.sin(math.radians(float(input("Input sin2 angle here: \n")))))

print(sin2)

n2=(float(input("Input n2 here: \n")))

total2=n2*sin2

print("The second angle of refraction is: \n", total2)

total1=round(total1, 1)
total2=round(total2, 1)

print("\n")

if total1 == total2:
    print("Snell\'s law is validated!")
else:
    print("Something is wrong with the inputs of sin or n. \n")
    print("Please redo the inputs for this program.")
    
    
