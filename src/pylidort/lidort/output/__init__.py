from dataclasses import dataclass

import numpy as np


@dataclass
class MainOutputs:
    TS_INTENSITY: (
        np.array
    )  # Intensity results at all angles and optical depths (MAX_USER_LEVELS, MAX_GEOMETRIES, MAX_DIRECTIONS)
