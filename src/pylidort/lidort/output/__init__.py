from dataclasses import dataclass, field

import numpy as np

from .. import pars


@dataclass
class MainOutputs:
    TS_INTENSITY: np.array = field(
        default_factory=lambda: np.zeros(
            (pars.MAX_USER_LEVELS, pars.MAX_GEOMETRIES, pars.MAX_DIRECTIONS), order="F"
        )
    )  # Intensity results at all angles and optical depths (MAX_USER_LEVELS, MAX_GEOMETRIES, MAX_DIRECTIONS)

    TS_MEANI_DIFFUSE: np.array = field(
        default_factory=lambda: np.zeros(
            (pars.MAX_USER_LEVELS, pars.MAXBEAMS, pars.MAX_DIRECTIONS), order="F"
        )
    )

    TS_FLUX_DIFFUSE: np.array = field(
        default_factory=lambda: np.zeros(
            (pars.MAX_USER_LEVELS, pars.MAXBEAMS, pars.MAX_DIRECTIONS), order="F"
        )
    )

    TS_DNMEANI_DIRECT: np.array = field(
        default_factory=lambda: np.zeros(
            (pars.MAX_USER_LEVELS, pars.MAXBEAMS), order="F"
        )
    )

    TS_DNFLUX_DIRECT: np.array = field(
        default_factory=lambda: np.zeros(
            (pars.MAX_USER_LEVELS, pars.MAXBEAMS), order="F"
        )
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
        default_factory=lambda: np.zeros((2, pars.MAXLAYERS + 1), order="F")
    )

    TS_LOSTRANS: np.array = field(
        default_factory=lambda: np.zeros((pars.MAXBEAMS, pars.MAXLAYERS), order="F")
    )

    TS_LAYER_MSSTS: np.array = field(
        default_factory=lambda: np.zeros((pars.MAXBEAMS, pars.MAXLAYERS), order="F")
    )

    TS_SURF_MSSTS: np.array = field(default_factory=lambda: np.zeros(pars.MAXBEAMS))

    TS_CONTRIBS: np.array = field(
        default_factory=lambda: np.zeros(
            (pars.MAX_GEOMETRIES, pars.MAXLAYERS), order="F"
        )
    )

    # TS_FOURIER_SAVED: np.array = field(
    #     default_factory=lambda: np.zeros(pars.MAXBEAMS, dtype=int)
    # )

    # TS_N_GEOMETRIES: int = 0

    # TS_SOLARBEAM_BOATRANS: np.array = field(
    #     default_factory=lambda: np.zeros(pars.MAXBEAMS)
    # )

    # TS_SPHERALB: float = 0.0

    # TS_TRANS1_USER: np.array = field(
    #     default_factory=lambda: np.zeros(pars.MAX_USER_STREAMS)
    # )

    # TS_TRANS1_BEAM: np.array = field(default_factory=lambda: np.zeros(pars.MAXBEAMS))


@dataclass
class Outputs:
    Main: MainOutputs = field(default_factory=MainOutputs)


@dataclass
class LinAtmosOutput:
    TS_COLUMNWF: np.array = field(
        default_factory=lambda: np.zeros(
            (
                pars.MAX_ATMOSWFS,
                pars.MAX_USER_LEVELS,
                pars.MAX_GEOMETRIES,
                pars.MAX_DIRECTIONS,
            ),
            order="F",
        )
    )

    TS_MEANI_DIFFUSE_COLWF: np.array = field(
        default_factory=lambda: np.zeros(
            (
                pars.MAX_ATMOSWFS,
                pars.MAX_USER_LEVELS,
                pars.MAXBEAMS,
                pars.MAX_DIRECTIONS,
            ),
            order="F",
        )
    )

    TS_FLUX_DIFFUSE_COLWF: np.array = field(
        default_factory=lambda: np.zeros(
            (
                pars.MAX_ATMOSWFS,
                pars.MAX_USER_LEVELS,
                pars.MAXBEAMS,
                pars.MAX_DIRECTIONS,
            ),
            order="F",
        )
    )

    TS_DNMEANI_DIRECT_COLWF: np.array = field(
        default_factory=lambda: np.zeros(
            (pars.MAX_ATMOSWFS, pars.MAX_USER_LEVELS, pars.MAXBEAMS), order="F"
        )
    )

    TS_DNFLUX_DIRECT_COLWF: np.array = field(
        default_factory=lambda: np.zeros(
            (pars.MAX_ATMOSWFS, pars.MAX_USER_LEVELS, pars.MAXBEAMS), order="F"
        )
    )

    TS_PROFILEWF: np.array = field(
        default_factory=lambda: np.zeros(
            (
                pars.MAX_ATMOSWFS,
                pars.MAXLAYERS,
                pars.MAX_USER_LEVELS,
                pars.MAX_GEOMETRIES,
                pars.MAX_DIRECTIONS,
            ),
            order="F",
        )
    )

    TS_MEANI_DIFFUSE_PROFWF: np.array = field(
        default_factory=lambda: np.zeros(
            (
                pars.MAX_ATMOSWFS,
                pars.MAXLAYERS,
                pars.MAX_USER_LEVELS,
                pars.MAXBEAMS,
                pars.MAX_DIRECTIONS,
            ),
            order="F",
        )
    )

    TS_FLUX_DIFFUSE_PROFWF: np.array = field(
        default_factory=lambda: np.zeros(
            (
                pars.MAX_ATMOSWFS,
                pars.MAXLAYERS,
                pars.MAX_USER_LEVELS,
                pars.MAXBEAMS,
                pars.MAX_DIRECTIONS,
            ),
            order="F",
        )
    )

    TS_DNMEANI_DIRECT_PROFWF: np.array = field(
        default_factory=lambda: np.zeros(
            (pars.MAX_ATMOSWFS, pars.MAXLAYERS, pars.MAX_USER_LEVELS, pars.MAXBEAMS),
            order="F",
        )
    )

    TS_DNFLUX_DIRECT_PROFWF: np.array = field(
        default_factory=lambda: np.zeros(
            (pars.MAX_ATMOSWFS, pars.MAXLAYERS, pars.MAX_USER_LEVELS, pars.MAXBEAMS),
            order="F",
        )
    )

    TS_ABBWFS_JACOBIANS: np.array = field(
        default_factory=lambda: np.zeros(
            (
                pars.MAX_USER_LEVELS,
                pars.MAX_USER_STREAMS,
                pars.MAXLAYERS + 1,
                pars.MAX_DIRECTIONS,
            ),
            order="F",
        )
    )

    TS_ABBWFS_FLUXES: np.array = field(
        default_factory=lambda: np.zeros(
            (pars.MAX_USER_LEVELS, 2, pars.MAXLAYERS + 1, pars.MAX_DIRECTIONS),
            order="F",
        )
    )

    TS_ALBMED_USER_PROFWF: np.array = field(
        default_factory=lambda: np.zeros(
            (pars.MAX_USER_STREAMS, pars.MAXLAYERS, pars.MAX_ATMOSWFS), order="F"
        )
    )

    TS_TRNMED_USER_PROFWF: np.array = field(
        default_factory=lambda: np.zeros(
            (pars.MAX_USER_STREAMS, pars.MAXLAYERS, pars.MAX_ATMOSWFS), order="F"
        )
    )

    TS_ALBMED_FLUXES_PROFWF: np.array = field(
        default_factory=lambda: np.zeros(
            (2, pars.MAXLAYERS, pars.MAX_ATMOSWFS), order="F"
        )
    )

    TS_TRNMED_FLUXES_PROFWF: np.array = field(
        default_factory=lambda: np.zeros(
            (2, pars.MAXLAYERS, pars.MAX_ATMOSWFS), order="F"
        )
    )

    TS_TRANSBEAM_PROFWF: np.array = field(
        default_factory=lambda: np.zeros(
            (pars.MAXBEAMS, pars.MAXLAYERS, pars.MAX_ATMOSWFS), order="F"
        )
    )

    TS_ALBMED_USER_COLWF: np.array = field(
        default_factory=lambda: np.zeros(
            (pars.MAX_USER_STREAMS, pars.MAX_ATMOSWFS), order="F"
        )
    )

    TS_TRNMED_USER_COLWF: np.array = field(
        default_factory=lambda: np.zeros(
            (pars.MAX_USER_STREAMS, pars.MAX_ATMOSWFS), order="F"
        )
    )

    TS_ALBMED_FLUXES_COLWF: np.array = field(
        default_factory=lambda: np.zeros((2, pars.MAX_ATMOSWFS), order="F")
    )

    TS_TRNMED_FLUXES_COLWF: np.array = field(
        default_factory=lambda: np.zeros((2, pars.MAX_ATMOSWFS), order="F")
    )

    TS_TRANSBEAM_COLWF: np.array = field(
        default_factory=lambda: np.zeros((pars.MAXBEAMS, pars.MAX_ATMOSWFS), order="F")
    )

    TS_PLANETARY_TRANSTERM_PROFWF: np.array = field(
        default_factory=lambda: np.zeros(
            (pars.MAX_GEOMETRIES, pars.MAXLAYERS, pars.MAX_ATMOSWFS), order="F"
        )
    )

    TS_PLANETARY_SBTERM_PROFWF: np.array = field(
        default_factory=lambda: np.zeros((pars.MAXLAYERS, pars.MAX_ATMOSWFS), order="F")
    )

    TS_PLANETARY_TRANSTERM_COLWF: np.array = field(
        default_factory=lambda: np.zeros(
            (pars.MAX_GEOMETRIES, pars.MAX_ATMOSWFS), order="F"
        )
    )

    TS_PLANETARY_SBTERM_COLWF: np.array = field(
        default_factory=lambda: np.zeros(pars.MAX_ATMOSWFS)
    )

    TS_LC_LOSTRANS: np.array = field(
        default_factory=lambda: np.zeros(
            (pars.MAX_ATMOSWFS, pars.MAXBEAMS, pars.MAXLAYERS), order="F"
        )
    )

    TS_LC_LAYER_MSSTS: np.array = field(
        default_factory=lambda: np.zeros(
            (pars.MAX_ATMOSWFS, pars.MAXBEAMS, pars.MAXLAYERS), order="F"
        )
    )

    TS_LC_SURF_MSSTS: np.array = field(
        default_factory=lambda: np.zeros((pars.MAX_ATMOSWFS, pars.MAXBEAMS), order="F")
    )

    TS_LP_LOSTRANS: np.array = field(
        default_factory=lambda: np.zeros(
            (pars.MAX_ATMOSWFS, pars.MAXBEAMS, pars.MAXLAYERS), order="F"
        )
    )

    TS_LP_LAYER_MSSTS: np.array = field(
        default_factory=lambda: np.zeros(
            (pars.MAX_ATMOSWFS, pars.MAXLAYERS, pars.MAXBEAMS, pars.MAXLAYERS),
            order="F",
        )
    )

    TS_LP_SURF_MSSTS: np.array = field(
        default_factory=lambda: np.zeros(
            (pars.MAX_ATMOSWFS, pars.MAXLAYERS, pars.MAXBEAMS), order="F"
        )
    )


@dataclass
class LinSurfOutput:
    TS_SURFACEWF: np.array = field(
        default_factory=lambda: np.zeros(
            (
                pars.MAX_SURFACEWFS,
                pars.MAX_USER_LEVELS,
                pars.MAX_GEOMETRIES,
                pars.MAX_DIRECTIONS,
            ),
            order="F",
        )
    )

    TS_MEANI_DIFFUSE_SURFWF: np.array = field(
        default_factory=lambda: np.zeros(
            (
                pars.MAX_SURFACEWFS,
                pars.MAX_USER_LEVELS,
                pars.MAXBEAMS,
                pars.MAX_DIRECTIONS,
            ),
            order="F",
        )
    )

    TS_FLUX_DIFFUSE_SURFWF: np.array = field(
        default_factory=lambda: np.zeros(
            (
                pars.MAX_SURFACEWFS,
                pars.MAX_USER_LEVELS,
                pars.MAXBEAMS,
                pars.MAX_DIRECTIONS,
            ),
            order="F",
        )
    )

    TS_SBBWFS_JACOBIANS: np.array = field(
        default_factory=lambda: np.zeros(
            (pars.MAX_USER_LEVELS, pars.MAX_USER_STREAMS, pars.MAX_DIRECTIONS),
            order="F",
        )
    )

    TS_SBBWFS_FLUXES: np.array = field(
        default_factory=lambda: np.zeros(
            (pars.MAX_USER_LEVELS, 2, pars.MAX_DIRECTIONS), order="F"
        )
    )

    TS_LS_LAYER_MSSTS: np.array = field(
        default_factory=lambda: np.zeros(
            (pars.MAX_SURFACEWFS, pars.MAXBEAMS, pars.MAXLAYERS), order="F"
        )
    )

    TS_LS_SURF_MSSTS: np.array = field(
        default_factory=lambda: np.zeros(
            (pars.MAX_SURFACEWFS, pars.MAXBEAMS), order="F"
        )
    )


@dataclass
class LinOutputs:
    Atmos: LinAtmosOutput = field(default_factory=LinAtmosOutput)
    Surf: LinSurfOutput = field(default_factory=LinSurfOutput)
