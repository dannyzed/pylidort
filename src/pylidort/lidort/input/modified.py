from dataclasses import dataclass, field

import numpy as np

from .. import pars


@dataclass
class ModifiedBoolean:
    """
    Wrapper around the LIDORT_Modified_Boolean class
    """

    TS_DO_FOCORR: bool = (
        False  # Flag for COmputing the corrected FO solution, if not set then LIDORT will perform a truncated pseudo-spherical SS calculation
    )

    TS_DO_FOCORR_EXTERNAL: bool = (
        False  # Flag for use of externally-derived FO results "DO_FOCORR" must be set first
    )

    TS_DO_FOCORR_NADIR: bool = False  # Sphericity options
    TS_DO_FOCORR_OUTGOING: bool = False

    TS_DO_SSCORR_TRUNCATION: bool = False  # Flag for performing SSCOR Truncation

    TS_DO_SSCORR_USEPHASFUNC: (
        bool  # Flag for using the phase function in the single scatter calulcations
    ) = False

    TS_DO_EXTERNAL_WLEAVE: (
        bool  # additional control for externalized water-leaving inputs
    ) = False

    TS_DO_DOUBLE_CONVTEST: bool = False  # double convergence test flag

    TS_DO_SOLAR_SOURCES: bool = True  # Basic top-level solar beam control

    TS_DO_REFRACTIVE_GEOMETRY: bool = False  # Pesudo-spherical input control
    TS_DO_CHAPMAN_FUNCTION: bool = True  # Pseudo-spherical input control

    TS_DO_RAYLEIGH_ONLY: bool = False
    TS_DO_ISOTROPIC_ONLY: bool = False
    TS_DO_NO_AZIMUTH: bool = False
    TS_DO_ALL_FOURIER: bool = False

    TS_DO_DELTAM_SCALING: bool = False

    TS_DO_SOLUTION_SAVING: bool = False
    TS_DO_BVP_TELESCOPING: bool = False

    TS_DO_USER_STREAMS: bool = True

    TS_DO_ADDITIONAL_MVOUT: bool = False
    TS_DO_MVOUT_ONLY: bool = False

    TS_DO_THERMAL_TRANSONLY: bool = False

    TS_DO_OBSERVATION_GEOMETRY: bool = True
    TS_DO_DOUBLET_GEOMETRY: bool = False


@dataclass
class ModifiedControl:
    """
    Wrapper around the LIDORT_Modified_Control class
    """

    TS_NMOMENTS_INPUT: int = 16  # Number of legentre phase function expansion moments


@dataclass
class ModifiedSunrays:
    """
    Wrapper around the LIDORT_Modified_Sunrays class
    """

    TS_NBEAMS: int = 0  # Number of solar beams to be processed

    TS_BEAM_SZAS: np.array = field(
        default_factory=lambda: np.zeros(pars.MAXBEAMS)
    )  # Bottom-of-atmosphere solar zenith angles, DEGREES


@dataclass
class ModifiedUserValues:
    """
    Wrapper around the LIDORT_Modified_UserValues class
    """

    TS_N_USER_RELAZMS: int = 0  # Number of user-defined relative azimuths
    TS_USER_RELAZMS: np.array = field(
        default_factory=lambda: np.zeros(pars.MAX_USER_RELAZMS)
    )  # User-defined relative azimuths, DEGREES

    TS_N_USER_STREAMS: int = 0  # Number of user-defined zenith angles
    TS_USER_ANGLES_INPUT: np.array = field(
        default_factory=lambda: np.zeros(pars.MAX_USER_STREAMS)
    )  # User-defined zenith angles, DEGREES

    TS_USER_LEVELS: np.array = field(
        default_factory=lambda: np.zeros(pars.MAX_USER_LEVELS)
    )  # User defined vertical level output. from Top-of-atmosphere

    TS_GEOMETRY_SPECHEIGHT: float = 0.0  # Geometry specification height

    TS_N_USER_OBSGEOMS: int = 1  # Observation geometry input control

    TS_USER_OBSGEOMS_INPUT: np.array = field(
        default_factory=lambda: np.zeros((pars.MAX_USER_OBSGEOMS, 3), order="F")
    )  # User-defined observation geometry angle input (MAX_USER_OBSGEOMS, 3)

    TS_N_USER_DOUBLETS: int = 0  # doublet-geometry input control and angles
    TS_USER_DOUBLETS: np.array = field(
        default_factory=lambda: np.zeros((pars.MAX_USER_STREAMS, 2), order="F")
    )  # Doublet geometry input control and angles (MAX_USER_STREAMS, 2)


@dataclass
class ModifiedChapman:
    """
    Wrapper around the LIDORT_Modified_Chapman class
    """

    TS_EARTH_RADIUS: float = (
        6371.0  # Earth radius in [km] for Chapman function calculation of TAUTHICK_INPUT
    )


@dataclass
class ModifiedOptical:
    """
    Wrapper around the LIDORT_Modified_Optical class
    """

    TS_OMEGA_TOTAL_INPUT: np.array = field(
        default_factory=lambda: np.zeros(pars.MAXLAYERS)
    )  # Multilayer optical property (bulk), size (MAXLAYERS)


@dataclass
class ModifiedInputs:
    """
    Wrapper around the LIDORT_Modified_Inputs class
    """

    MBool: ModifiedBoolean = field(default_factory=ModifiedBoolean)
    MCont: ModifiedControl = field(default_factory=ModifiedControl)
    MSunrays: ModifiedSunrays = field(default_factory=ModifiedSunrays)
    MUserVal: ModifiedUserValues = field(default_factory=ModifiedUserValues)
    MChapman: ModifiedChapman = field(default_factory=ModifiedChapman)
    MOptical: ModifiedOptical = field(default_factory=ModifiedOptical)


@dataclass
class ModifiedLinControl:
    """
    Wrapper around the LIDORT_Modified_LinControl class
    """

    TS_DO_COLUMN_LINEARIZATION: bool = False
    TS_DO_PROFILE_LINEARIZATION: bool = False
    TS_DO_ATMOS_LINEARIZATION: bool = False

    TS_DO_SURFACE_LINEARIZATION: bool = False
    TS_DO_LINEARIZATION: bool = False

    TS_DO_SIMULATION_ONLY: bool = False

    TS_DO_ATMOS_LBBF: bool = False
    TS_DO_SURFACE_LBBF: bool = False
    TS_DO_SLEAVE_WFS: bool = False


@dataclass
class ModifiedLinInputs:
    """
    Wrapper around the LIDORT_Modified_LinInputs class
    """

    MCont: ModifiedLinControl = field(default_factory=ModifiedLinControl)
