# refraction script

import numpy as np


def snell(theta_inc, n1, n2):

    # Incident angle in radians
    theta_inc: float

    # The refractive index of medium of origin and destination medium.
    n1: float
    n2: float

    # return answer
    print(np.arcsin(n1 / n2 * np.sin(theta_inc)))

# Example: A ray enters an air--water boundary at pi/4 radians (45 degrees). Compute exit angle.
snell(np.pi/4, 1.00, 1.33)
