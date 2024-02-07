from dataclasses import dataclass, field

import numpy as np

from .. import pars


@dataclass
class MainOutputs:
    TS_INTENSITY: np.array = field(
        default_factory=lambda: np.zeros(
            (pars.MAX_USER_LEVELS, pars.MAX_GEOMETRIES, pars.MAX_DIRECTIONS)
        )
    )  # Intensity results at all angles and optical depths (MAX_USER_LEVELS, MAX_GEOMETRIES, MAX_DIRECTIONS)

    TS_MEANI_DIFFUSE: np.array = field(
        default_factory=lambda: np.zeros(
            (pars.MAX_USER_LEVELS, pars.MAXBEAMS, pars.MAX_DIRECTIONS)
        )
    )

    TS_FLUX_DIFFUSE: np.array = field(
        default_factory=lambda: np.zeros(
            (pars.MAX_USER_LEVELS, pars.MAXBEAMS, pars.MAX_DIRECTIONS)
        )
    )

    TS_DNMEANI_DIRECT: np.array = field(
        default_factory=lambda: np.zeros((pars.MAX_USER_LEVELS, pars.MAXBEAMS))
    )

    TS_DNFLUX_DIRECT: np.array = field(
        default_factory=lambda: np.zeros((pars.MAX_USER_LEVELS, pars.MAXBEAMS))
    )

    TS_ALBMED_USER: np.array = field(
        default_factory=lambda: np.zeros(pars.MAX_USER_STREAMS)
    )

    TS_TRNMED_USER: np.array = field(
        default_factory=lambda: np.zeros(pars.MAX_USER_STREAMS)
    )

    TS_ALBMED_FLUXES: np.array = field(default_factory=lambda: np.zeros(2))

    TS_TRNMED_FLUXES: np.array = field(default_factory=lambda: np.zeros(2))

    TS_PLANETARY_TRANSTERM: np.array = field(
        default_factory=lambda: np.zeros(pars.MAX_GEOMETRIES)
    )

    TS_PLANETARY_SBTERM: float = 0

    TS_PATHGEOMS: np.array = field(
        default_factory=lambda: np.zeros((2, pars.MAXLAYERS + 1))
    )

    TS_LOSTRANS: np.array = field(
        default_factory=lambda: np.zeros((pars.MAXBEAMS, pars.MAXLAYERS))
    )

    TS_LAYER_MSSTS: np.array = field(
        default_factory=lambda: np.zeros((pars.MAXBEAMS, pars.MAXLAYERS))
    )

    TS_SURF_MSSTS: np.array = field(default_factory=lambda: np.zeros(pars.MAXBEAMS))

    TS_CONTRIBS: np.array = field(
        default_factory=lambda: np.zeros((pars.MAX_GEOMETRIES, pars.MAXLAYERS))
    )

    TS_FOURIER_SAVED: np.array = field(
        default_factory=lambda: np.zeros(pars.MAXBEAMS, dtype=int)
    )

    TS_N_GEOMETRIES: int = 0

    TS_SOLARBEAM_BOATRANS: np.array = field(
        default_factory=lambda: np.zeros(pars.MAXBEAMS)
    )

    TS_SPHERALB: float = 0.0

    TS_TRANS1_USER: np.array = field(
        default_factory=lambda: np.zeros(pars.MAX_USER_STREAMS)
    )

    TS_TRANS1_BEAM: np.array = field(default_factory=lambda: np.zeros(pars.MAXBEAMS))


@dataclass
class Outputs:

    Main: MainOutputs = field(default_factory=MainOutputs)
